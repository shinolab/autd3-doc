import os
import pathlib
import platform
import re
import subprocess
import sys
from pathlib import Path


def python_module(cmd: list[str]) -> list[str]:
    return [
        "python" if platform.system() == "Windows" else "python3",
        "-m",
        *cmd,
    ]


def install_pyautd3() -> None:
    version = "29.0.0rc20"
    emulator_version = "29.0.0rc20"
    link_soem_version = "29.0.0rc20"
    subprocess.run(
        python_module(["pip", "install", "-U", f"pyautd3=={version}"]),
    )
    subprocess.run(
        python_module(
            ["pip", "install", "-U", f"pyautd3_emulator=={emulator_version}"],
        ),
    )
    subprocess.run(
        python_module(
            ["pip", "install", "-U", f"pyautd3_link_soem=={link_soem_version}"],
        ),
    )


def substitute_in_file(
    path: str,
    pattern: str,
    repl: str,
    target: Path,
) -> None:
    file = Path(path)
    content = file.read_text(encoding="utf-8")
    content = re.sub(pattern, repl, content, flags=re.MULTILINE)
    target.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    install_pyautd3()

    base_path = pathlib.Path(os.getcwd()) / "src" / "codes"

    srcs = list(base_path.rglob("*.py"))

    test_dir = pathlib.Path(__file__).parent / "test-python"
    if not test_dir.exists():
        test_dir.mkdir()

    for src in srcs:
        dst = test_dir / src.relative_to(base_path)
        if not dst.parent.exists():
            dst.parent.mkdir(parents=True)
            with (dst.parent / "__init__.py").open("w") as f:
                pass
        substitute_in_file(
            src,
            "~",
            "",
            dst,
        )

    r = subprocess.run(
        python_module(["mypy", str(test_dir), "--check-untyped-defs"]),
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    try:
        r.check_returncode()
    except subprocess.CalledProcessError:
        err = r.stdout
        print(
            err.replace(
                str(pathlib.Path(__file__).parent / "test-python"),
                str(base_path),
            ),
        )
        sys.exit(1)

    r = subprocess.run(
        python_module(["ruff", "check", str(test_dir)]),
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    try:
        r.check_returncode()
    except subprocess.CalledProcessError:
        err = r.stdout
        print(
            err.replace(
                str(pathlib.Path(__file__).parent / "test-python"),
                str(base_path),
            ),
        )
        sys.exit(1)

    print("All tests passed.")
