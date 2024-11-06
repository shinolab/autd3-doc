import pathlib
import re
import subprocess
import sys

from autd3_build_utils.autd3_build_utils import (
    BaseConfig,
    run_command,
    substitute_in_file,
)


class Config(BaseConfig):
    def __init__(self) -> None:
        super().__init__(None)


def python_module(cmd: list[str]) -> list[str]:
    config = Config()
    return ["python" if config.is_windows() else "python3", "-m", *cmd]


def install_pyautd3() -> None:
    version = "29.0.0-rc.5.post1"
    link_soem_version = "29.0.0-rc.5.post1"
    run_command(python_module(["pip", "install", "-U", f"pyautd3=={version}"]))
    run_command(python_module(["pip", "install", "-U", f"pyautd3_link_soem=={link_soem_version}"]))


if __name__ == "__main__":
    install_pyautd3()

    base_path = pathlib.Path(__file__).parent.parent / "src" / "codes"

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
        substitute_in_file(src, [("~", "")], target_file=dst, flags=re.MULTILINE)

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
        print(err.replace("test-python", str(base_path)))
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
        print(err.replace("test-python", str(base_path)))
        sys.exit(1)

    print("All tests passed.")
