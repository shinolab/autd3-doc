import os
import pathlib
import re
import subprocess
import sys
from functools import reduce
from pathlib import Path

import joblib
import requests


def get_latest_version(crate: str) -> str:
    res = requests.get(f"https://crates.io/api/v1/crates/{crate}")
    return res.json()["crate"]["newest_version"]


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
    autd3_version = "32.0.0"
    autd3_emulator_version = "32.0.0"
    autd3_link_soem_version = "32.0.0"
    itertools_version = get_latest_version("itertools")
    tokio = get_latest_version("tokio")
    print(f"Testing with autd3-rs {autd3_version}")

    base_path = pathlib.Path(os.getcwd()) / "src" / "codes"
    print(base_path)

    n_jobs = 1
    srcs = sys.argv[1:] if len(sys.argv) > 1 else list(base_path.rglob("*.rs"))
    print(f"Testing {len(srcs)} files:")
    for src in srcs:
        print(f"{src}")
    N = len(srcs)
    block = N // n_jobs

    base_test_dir = pathlib.Path(__file__).parent / "test-rs"
    if not base_test_dir.exists():
        base_test_dir.mkdir()

    def test(i: int, n: int) -> list[str]:
        error_files = []
        start = i * block
        end = (i + 1) * block if i != n_jobs - 1 else n

        test_dir = base_test_dir / str(i)
        if not test_dir.exists():
            test_dir.mkdir()
        src_dir = test_dir / "src"
        if not src_dir.exists():
            src_dir.mkdir()
        with (test_dir / "Cargo.toml").open("w") as f:
            f.write(
                f"""[package]
name = "thirdparties"
version = "{autd3_version}"
edition = "2021"

[dependencies]
autd3 = {{ version = "{autd3_version}", features = ["async", "async-trait"] }}
autd3-gain-holo = {{ version = "{autd3_version}" }}
autd3-link-simulator = {{ version = "{autd3_version}", features = ["blocking", "async-trait"] }}
autd3-link-soem = {{ version = "{autd3_link_soem_version}", features = ["remote", "blocking", "async-trait"] }}
autd3-link-twincat = {{ version = "{autd3_version}", features = ["remote", "async-trait"] }}
autd3-modulation-audio-file = {{ version = "{autd3_version}" }}
autd3-protobuf = {{ version = "{autd3_version}", features = ["lightweight"] }}
autd3-emulator = {{ version = "{autd3_emulator_version}", features = ["gpu"] }}
itertools = {{ version = "{itertools_version}" }}
tokio = {{ version = "{tokio}", features = ["rt-multi-thread", "macros"] }}
""",
            )

        for src in srcs[start:end]:
            substitute_in_file(
                src,
                "# ",
                "",
                src_dir / "main.rs",
            )
            try:
                subprocess.run(
                    ["cargo", "rustc", "--", "-D", "warnings"],
                    cwd=test_dir,
                ).check_returncode()
            except subprocess.CalledProcessError:
                print(f"Error: {src}")
                error_files.append(src)

        return error_files

    result = joblib.Parallel(n_jobs=n_jobs)(
        joblib.delayed(test)(i, len(srcs)) for i in range(n_jobs)
    )
    err_files = reduce(lambda a, b: a + b, result)
    if len(err_files) == 0:
        print("All files are OK")
    else:
        print("Error files:")
        for src in err_files:
            print(f"{src}")
        sys.exit(1)
