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
    processed_lines = []
    for line in input_lines:
        if line == "```\n":
            bash = False
            if not output == "\n```output":
                processed_lines.append(line)
                # processed_lines.append(re.sub("\n$", "", output))
                processed_lines.append(output)

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

        processed_lines.append(line)
    return processed_lines


def cli_arg_parser(args=None):
    parser = argparse.ArgumentParser(
        prog="bashdown",
        description="Processes in-line bash in markdown files",
        epilog="For more information please see the docs",
    )
    parser.add_argument("filename")
    return parser.parse_args(args)


def main():
    args = cli_arg_parser(sys.argv[1:])

    with open(args.filename, "r", encoding="utf8") as file:
        content = file.readlines()

    for line in process_content(content):
        print(line, end="")


if __name__ == "__main__":
    main()
