#!/usr/bin/env python3

import argparse
import contextlib
import datetime
import os
import re
import subprocess


def err(msg: str):
    print("\033[91mERR \033[0m: " + msg)


def warn(msg: str):
    print("\033[93mWARN\033[0m: " + msg)


def info(msg: str):
    print("\033[92mINFO\033[0m: " + msg)


@contextlib.contextmanager
def set_env(key, value):
    env = os.environ.copy()
    os.environ[key] = value
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(env)


@contextlib.contextmanager
def working_dir(path):
    cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cwd)


def env_exists(value):
    return value in os.environ and os.environ[value] != ""


def doc_build(args):
    with working_dir("."):
        command = ["mdbook", "build", "--dest-dir", f"book/{args.target}"]
        if args.open:
            command.append("--open")
        with set_env("MDBOOK_BOOK__src", f"src/{args.target}"):
            subprocess.run(command).check_returncode()


def doc_serve(args):
    with working_dir("."):
        command = ["mdbook", "serve", "--dest-dir", f"book/{args.target}"]
        if args.open:
            command.append("--open")
        with set_env("MDBOOK_BOOK__src", f"src/{args.target}"):
            subprocess.run(command).check_returncode()


def util_update_ver(args):
    version = args.version

    with working_dir("."):
        with open("src/codes/Users_Manual/Tutorial/CMakeLists.txt", "r") as f:
            content = f.read()
            content = re.sub(
                r"v(.*)/autd3-v(\d*\.\d*\.\d*)",
                f"v{version}/autd3-v{version}",
                content,
                flags=re.MULTILINE,
            )
        with open("src/codes/Users_Manual/Tutorial/CMakeLists.txt", "w") as f:
            f.write(content)

        now = datetime.datetime.now().strftime("%Y/%m/%d")

        with open("src/en/Users_Manual/release_notes.md", "r") as f:
            content = f.read().rstrip()
        with open("src/en/Users_Manual/release_notes.md", "w") as f:
            lines = content.split("\n")
            i = 0
            for _ in range(4):
                f.write(lines[i] + "\n")
                i += 1
            last_firm_ver = lines[i].split("|")[3].strip()
            f.write(f"| {now}  | {version:16} | {last_firm_ver:16} |\n")
            for line in lines[i:]:
                f.write(line + "\n")

        with open("src/jp/Users_Manual/release_notes.md", "r") as f:
            content = f.read().rstrip()
        with open("src/jp/Users_Manual/release_notes.md", "w") as f:
            lines = content.split("\n")
            i = 0
            for _ in range(4):
                f.write(lines[i] + "\n")
                i += 1
            last_firm_ver = lines[i].split("|")[3].strip()
            f.write(f"| {now}  | {version:16} | {last_firm_ver:16} |\n")
            for line in lines[i:]:
                f.write(line + "\n")

        with open("src/en/document_history.md", "r") as f:
            content = f.read().rstrip()
        with open("src/en/document_history.md", "w") as f:
            lines = content.split("\n")
            i = 0
            for _ in range(4):
                f.write(lines[i] + "\n")
                i += 1
            f.write(f"| {now} | Version {version} Initial release                |\n")
            for line in lines[i:]:
                f.write(line + "\n")

        with open("src/jp/document_history.md", "r", encoding="utf-8") as f:
            content = f.read().rstrip()
        with open("src/jp/document_history.md", "w", encoding="utf-8") as f:
            lines = content.split("\n")
            i = 0
            for _ in range(4):
                f.write(lines[i] + "\n")
                i += 1
            f.write(f"| {now} | Version {version} 初版                           |\n")
            for line in lines[i:]:
                f.write(line + "\n")

        with open("book.toml", "r") as f:
            content = f.read()
            content = re.sub(
                r'^title = "AUTD3 Developers Manual v(.*)"',
                f'title = "AUTD3 Developers Manual v{version}"',
                content,
                flags=re.MULTILINE,
            )
        with open("book.toml", "w") as f:
            f.write(content)

        with open("tools/rs_test.py", "r") as f:
            content = f.read()
            content = re.sub(
                r'autd3_version = "(.*)"',
                f'autd3_version = "{version}"',
                content,
                flags=re.MULTILINE,
            )
            content = re.sub(
                r'autd3_link_vis_version = "(.*)"',
                f'autd3_link_vis_version = "{version}"',
                content,
                flags=re.MULTILINE,
            )
        with open("tools/rs_test.py", "w") as f:
            f.write(content)

        with open("tools/cpp_test.py", "r") as f:
            content = f.read()
            content = re.sub(
                r'version = "(.*)"',
                f'version = "{version}"',
                content,
                flags=re.MULTILINE,
            )
        with open("tools/cpp_test.py", "w") as f:
            f.write(content)

        with open("tools/cs_test.py", "r") as f:
            content = f.read()
            content = re.sub(
                r'version = "(.*)"',
                f'version = "{version}"',
                content,
                flags=re.MULTILINE,
            )
        with open("tools/cs_test.py", "w") as f:
            f.write(content)

        with open("tools/python_test.py", "r") as f:
            content = f.read()
            content = re.sub(
                r'version = "(.*)"',
                f'version = "{version}"',
                content,
                flags=re.MULTILINE,
            )
        with open("tools/python_test.py", "w") as f:
            f.write(content)


def command_help(args):
    print(parser.parse_args([args.command, "--help"]))


if __name__ == "__main__":
    with working_dir(os.path.dirname(os.path.abspath(__file__))):
        parser = argparse.ArgumentParser(description="autd3 library build script")
        subparsers = parser.add_subparsers()

        # build
        parser_doc_build = subparsers.add_parser("build", help="see `build -h`")
        parser_doc_build.add_argument("target", help="build target [jp|en]")
        parser_doc_build.add_argument(
            "--open", help="open browser after build", action="store_true"
        )
        parser_doc_build.set_defaults(handler=doc_build)

        # serve
        parser_doc_serve = subparsers.add_parser("serve", help="see `serve -h`")
        parser_doc_serve.add_argument("target", help="build target [jp|en]")
        parser_doc_serve.add_argument(
            "--open", help="open browser after build", action="store_true"
        )
        parser_doc_serve.set_defaults(handler=doc_serve)

        # util
        parser_util = subparsers.add_parser("util", help="see `util -h`")
        subparsers_util = parser_util.add_subparsers()

        # util update version
        parser_util_upver = subparsers_util.add_parser(
            "upver", help="see `util upver -h`"
        )
        parser_util_upver.add_argument("version", help="version")
        parser_util_upver.set_defaults(handler=util_update_ver)

        # help
        parser_help = subparsers.add_parser("help", help="see `help -h`")
        parser_help.add_argument("command", help="command name which help is shown")
        parser_help.set_defaults(handler=command_help)

        args = parser.parse_args()
        if hasattr(args, "handler"):
            args.handler(args)
        else:
            parser.print_help()
