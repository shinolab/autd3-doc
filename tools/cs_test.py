import multiprocessing
import os
import pathlib
import re
import subprocess
import sys
from functools import reduce
from pathlib import Path

import joblib


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
    version = "35.0.1.1"
    link_soem_version = "35.0.1.1"
    print(f"Testing with AUTD3Sharp {version}")

    base_path = pathlib.Path(os.getcwd()) / "src" / "codes"

    n_jobs = multiprocessing.cpu_count()

    cs_srcs = (
        sys.argv[1:] if len(sys.argv) > 1 else list(base_path.rglob("*.cs"))
    )
    print(f"Testing {len(cs_srcs)} files:")
    for src in cs_srcs:
        print(f"{src}")
    N = len(cs_srcs)
    block = N // n_jobs

    base_test_dir = pathlib.Path(__file__).parent / "test-cs"
    if not base_test_dir.exists():
        base_test_dir.mkdir()

    def test(i: int, n: int) -> list[pathlib.Path]:
        error_files = []
        start = i * block
        end = (i + 1) * block if i != n_jobs - 1 else n

        test_dir = base_test_dir / str(i)
        if not test_dir.exists():
            test_dir.mkdir()
        with (test_dir / "test.csproj").open("w") as f:
            f.write(
                f"""<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <OutputType>Exe</OutputType>
        <TargetFramework>net8.0</TargetFramework>
        <ImplicitUsings>enable</ImplicitUsings>
        <Nullable>enable</Nullable>
        <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
        <EmitCompilerGeneratedFiles>true</EmitCompilerGeneratedFiles>
    </PropertyGroup>

    <ItemGroup>
        <PackageReference Include="AUTD3Sharp" Version="{version}" />
        <PackageReference Include="AUTD3Sharp.Link.SOEM" Version="{link_soem_version}" />
    </ItemGroup>

    </Project>""",
            )

        for cs_src in cs_srcs[start:end]:
            substitute_in_file(
                cs_src,
                "~",
                "",
                test_dir / "test.cs",
            )

            r = subprocess.run(
                ["dotnet", "build"],
                cwd=test_dir,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )
            try:
                r.check_returncode()
            except subprocess.CalledProcessError:
                err = ""
                src_file = str(pathlib.Path(cs_src).absolute())
                test_file = str((test_dir / "test.cs").absolute())
                for line in r.stdout.split("\n"):
                    print(line)
                    if line.startswith(test_file):
                        err = line.replace(test_file, src_file).split("[")[0]
                        break
                error_files.append((cs_src, err))
        return error_files

    result = joblib.Parallel(n_jobs=n_jobs)(
        joblib.delayed(test)(i, len(cs_srcs)) for i in range(n_jobs)
    )
    err_files = reduce(lambda a, b: a + b, result)
    if len(err_files) == 0:
        print("All files are OK")
    else:
        print("Error files:")
        for cs_src, err in err_files:
            print(f"{cs_src}")
            print(f"\t{err}")
        sys.exit(1)
