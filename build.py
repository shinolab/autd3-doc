#!/usr/bin/env python3

import argparse
import datetime
import pathlib
import re

from tools.autd3_build_utils.autd3_build_utils import (
    remove,
    run_command,
    substitute_in_file,
    with_env,
    working_dir,
)


def doc_build(args) -> None:  # noqa: ANN001
    command = ["mdbook", "build", "--dest-dir", f"book/{args.target}"]
    if args.open:
        command.append("--open")
    with with_env(MDBOOK_BOOK__src=f"src/{args.target}"):
        run_command(command)


def doc_serve(args) -> None:  # noqa: ANN001
    command = ["mdbook", "serve", "--dest-dir", f"book/{args.target}"]
    if args.open:
        command.append("--open")
    with with_env(MDBOOK_BOOK__src=f"src/{args.target}"):
        run_command(command)


def doc_clear(_) -> None:  # noqa: ANN001
    remove("book")
    remove("tools/.mypy_cache")
    remove("tools/.ruff_cache")
    remove("tools/test-cs")
    remove("tools/test-python")
    remove("tools/test-rs")
    remove("tools/test-cpp")


def util_update_ver(args) -> None:  # noqa: ANN001
    version = args.version

    substitute_in_file(
        "src/codes/Users_Manual/Tutorial/CMakeLists.txt",
        [
            (
                r"v.*/autd3-v.*-(win|macos|linux)",
                rf"v{version}/autd3-v{version}-\1",
            ),
        ],
        flags=re.MULTILINE,
    )

    now = datetime.datetime.now().strftime("%Y/%m/%d")  # noqa: DTZ005

    def update_release_note(path: str) -> None:
        f = pathlib.Path(path)
        content = f.read_text().strip()
        lines = content.split("\n")
        content: list[str] = []
        i = 0
        for _ in range(4):
            content.append(lines[i])
            i += 1
        last_firm_ver = lines[i].split("|")[3].strip()
        content.append(f"| {now}  | {version:16} | {last_firm_ver:16} |")
        for line in lines[i:]:
            content.append(line)
        f.write_text("\n".join(content))

    update_release_note("src/en/Users_Manual/release_notes.md")
    update_release_note("src/jp/Users_Manual/release_notes.md")

    def update_document_history(path: str, text: str) -> None:
        f = pathlib.Path(path)
        content = f.read_text(encoding="utf-8").strip()
        lines = content.split("\n")
        content: list[str] = []
        i = 0
        for _ in range(4):
            content.append(lines[i])
            i += 1
        content.append(f"| {now} | Version {version} {text}|")
        for line in lines[i:]:
            content.append(line)
        f.write_text("\n".join(content), encoding="utf-8")

    update_document_history("src/en/document_history.md", "Initial release                ")
    update_document_history("src/jp/document_history.md", "初版                           ")

    substitute_in_file(
        "book.toml",
        [
            (
                r'^title = "AUTD3 Developers Manual v(.*)"',
                f'title = "AUTD3 Developers Manual v{version}"',
            ),
        ],
        flags=re.MULTILINE,
    )

    substitute_in_file(
        "tools/rs_test.py",
        [
            (
                r'autd3_version = "(.*)"',
                f'autd3_version = "{version}"',
            ),
            (
                r'autd3_emulator_version = "(.*)"',
                f'autd3_emulator_version = "{version}"',
            ),
            (
                r'autd3_link_soem_version = "(.*)"',
                f'autd3_link_soem_version = "{version}"',
            ),
        ],
    )

    substitute_in_file(
        "tools/cpp_test.py",
        [
            (
                r'version = "(.*)"',
                f'version = "{version}"',
            ),
        ],
        flags=re.MULTILINE,
    )

    substitute_in_file(
        "tools/cs_test.py",
        [
            (
                r'version = "(.*)"',
                f'version = "{version}"',
            ),
        ],
        flags=re.MULTILINE,
    )

    substitute_in_file(
        "tools/python_test.py",
        [
            (
                r'version = "(.*)"',
                f'version = "{version}"',
            ),
        ],
        flags=re.MULTILINE,
    )


def command_help(args) -> None:  # noqa: ANN001
    print(parser.parse_args([args.command, "--help"]))


if __name__ == "__main__":
    with working_dir(pathlib.Path(__file__).parent):
        parser = argparse.ArgumentParser(description="autd3 library build script")
        subparsers = parser.add_subparsers()

        # build
        parser_doc_build = subparsers.add_parser("build", help="see `build -h`")
        parser_doc_build.add_argument("target", help="build target [jp|en]")
        parser_doc_build.add_argument("--open", help="open browser after build", action="store_true")
        parser_doc_build.set_defaults(handler=doc_build)

        # serve
        parser_doc_serve = subparsers.add_parser("serve", help="see `serve -h`")
        parser_doc_serve.add_argument("target", help="build target [jp|en]")
        parser_doc_serve.add_argument("--open", help="open browser after build", action="store_true")
        parser_doc_serve.set_defaults(handler=doc_serve)

        # clear
        parser_doc_clear = subparsers.add_parser("clear", help="see `clear -h`")
        parser_doc_clear.set_defaults(handler=doc_clear)

        # util
        parser_util = subparsers.add_parser("util", help="see `util -h`")
        subparsers_util = parser_util.add_subparsers()

        # util update version
        parser_util_upver = subparsers_util.add_parser("upver", help="see `util upver -h`")
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
