"""
Takes a markdown file with bash code blocks, executes the bash commands and
returns the original markdown content with output blocks containing the
executed command's results
"""

import argparse
import re
import subprocess
import sys


def process_content(input_lines):
    """
    Parses input lines looking for code blocks to execute.

    Keyword Arguments:
    input_lines -- takes a list of strings and looks for bash code blocks in
                   them. If it finds one, it executes the code from that block
                   and outputs the result in an output block underneath the code.
    """
    bash = False
    for line in input_lines:
        if line == "```\n":
            bash = False
            if not output == "\n```output":
                print(line, end="")
                print(re.sub("\n$", "", output))

        if bash:
            if not line.startswith("#"):
                cmd = line.split()
                result = subprocess.run(
                    cmd, check=True, stdout=subprocess.PIPE
                ).stdout.decode("utf-8")
                output = "\n".join([output, result])

        if line == "```bash\n":
            bash = True
            output = "\n```output"

        print(line, end="")


def cli_arg_parser(args=None):
    parser = argparse.ArgumentParser(
        prog="bashdown",
        description="Processes in-line bash in markdown files",
        epilog="For more information please see the docs",
    )
    parser.add_argument("filename")
    return parser.parse_args()


def main():
    args = cli_arg_parser(sys.argv[1:])

    with open(args.filename, "r", encoding="utf8") as file:
        content = file.readlines()

    process_content(content)


if __name__ == "__main__":
    main()
