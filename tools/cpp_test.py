import contextlib
import multiprocessing
import os
import re
import subprocess
import sys
from collections.abc import Generator
from functools import reduce
from pathlib import Path

import joblib


@contextlib.contextmanager
def working_dir(path: Path) -> Generator:
    cwd = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cwd)


def substitute_in_file(
    src_file: Path | str,
    mapping: list[tuple[str, str]],
    *,
    target_file: Path | str | None = None,
    flags: re.RegexFlag = re.NOFLAG,
) -> None:
    src_file = Path(src_file)
    target_file = (
        Path(target_file) if target_file is not None else Path(src_file)
    )
    content = src_file.read_text(encoding="utf-8")
    for key, value in mapping:
        content = re.sub(key, value, content, flags=flags)
    target_file.write_text(content, encoding="utf-8")


def run_command(command: list[str], *, shell: bool = False) -> None:
    try:
        subprocess.run(command, check=False, shell=shell).check_returncode()
    except subprocess.CalledProcessError:
        print(f"command failed: {' '.join(command)}")
        sys.exit(-1)


if __name__ == "__main__":
    version = "34.0.0"
    link_soem_version = "34.0.0"
    print(f"Testing with autd3-cpp {version}")

    base_path = Path(os.getcwd()) / "src" / "codes"

    n_jobs = multiprocessing.cpu_count() // 2
    srcs = sys.argv[1:] if len(sys.argv) > 1 else list(base_path.rglob("*.cpp"))
    print(f"Testing {len(srcs)} files:")
    for src in srcs:
        print(f"{src}")

    N = len(srcs)
    block = N // n_jobs

    base_test_dir = Path(__file__).parent / "test-cpp"
    if not base_test_dir.exists():
        base_test_dir.mkdir()

    def test(i: int, n: int) -> list[Path]:
        error_files = []
        start = i * block
        end = (i + 1) * block if i != n_jobs - 1 else n

        test_dir = base_test_dir / str(i)
        if not test_dir.exists():
            test_dir.mkdir()
        build_dir = test_dir / "build"
        if not build_dir.exists():
            build_dir.mkdir()
        with (test_dir / "CMakeLists.txt").open("w") as f:
            f.write(
                f"""cmake_minimum_required(VERSION 3.21)

project(autd3-doc-test)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(${{CMAKE_VERSION}} VERSION_GREATER_EQUAL "3.24.0")
  cmake_policy(SET CMP0135 NEW)
endif()

include(FetchContent)
if(WIN32)
  FetchContent_Declare(
    autd3
    URL https://github.com/shinolab/autd3-cpp/releases/download/v{version}/autd3-v{version}-win-x64.zip
  )
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v{link_soem_version}/autd3-link-soem-v{link_soem_version}-win-x64.zip
  )
elseif(APPLE)
  FetchContent_Declare(
    autd3
    URL https://github.com/shinolab/autd3-cpp/releases/download/v{version}/autd3-v{version}-macos-aarch64.tar.gz
  )
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v{link_soem_version}/autd3-link-soem-v{link_soem_version}-macos-aarch64.tar.gz
  )
else()
  FetchContent_Declare(
    autd3
    URL https://github.com/shinolab/autd3-cpp/releases/download/v{version}/autd3-v{version}-linux-x64.tar.gz
  )
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v{link_soem_version}/autd3-link-soem-v{link_soem_version}-linux-x64.tar.gz
  )
endif()
set(USE_SYSTEM_EIGEN ON)
FetchContent_MakeAvailable(autd3 autd3-link-soem)

add_executable(main main.cpp)

target_link_libraries(main PRIVATE autd3::autd3)
target_link_libraries(main PRIVATE autd3::link::soem)
target_link_libraries(main PRIVATE autd3::link::twincat)
target_link_libraries(main PRIVATE autd3::link::simulator)
target_link_libraries(main PRIVATE autd3::gain::holo)
target_link_libraries(main PRIVATE autd3::modulation::audio_file)
""",
            )

        with (test_dir / "main.cpp").open("w") as f:
            f.write("""int main() { return 0; }""")
        with working_dir(build_dir):
            run_command(["cmake", ".."])
        for src in srcs[start:end]:
            substitute_in_file(
                src,
                [("//~", "")],
                target_file=test_dir / "main.cpp",
                flags=re.MULTILINE,
            )
            try:
                subprocess.run(
                    ["cmake", "--build", ".", "--config", "release"],
                    cwd=build_dir,
                ).check_returncode()
            except subprocess.CalledProcessError:
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
