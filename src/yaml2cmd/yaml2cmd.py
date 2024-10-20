#!/usr/bin/python3

import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from os import EX_NOINPUT, EX_OK

import yaml
from subprocess import run
# import re


def process_arguments(command: str, argument_list: list) -> str:
    """Process arguments for a given command

    Args:
        command (str): Command
        argument_list (list): List of arguments. Can be either a str or a dict for multi valued
        arguments

    Returns:
        str: A single string with the command and the arguments separated by spaces
    """
    arg_list = []
    for argument in argument_list:
        if isinstance(argument, str):
            arg_list.append(argument)
        elif isinstance(argument, dict):
            for dict_arg_name, dict_arg_values in argument.items():
                # Check if this is a script argument or not
                # script_arg_pattern = r'\$\d+([: ]|$)'
                # matched_pattern = re.match(script_arg_pattern, )
                # if script_arg_pattern:
                #     arg_list.append()
                # else:
                arg_list.append(process_arguments(dict_arg_name, dict_arg_values))

    return f"{command} {' '.join(arg_list)}"


def main():
    """
    Script entrypoint
    """

    parser = ArgumentParser(
        description="Run long commands from yaml files.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("yaml_file", nargs=1, default="command.yaml")

    parser.add_argument(
        "-v",
        dest="verbose",
        help="Enables verbose mode",
        action="store_true",
        default=False
    )

    parsed, unparsed = parser.parse_known_args()

    command_map = {}
    yaml_file_path = parsed.yaml_file[0]
    with open(yaml_file_path, "r", encoding="utf-8") as stream:
        try:
            command_map = yaml.safe_load(stream)
        except yaml.YAMLError:
            print(f"Could not load file {yaml_file_path}")
            sys.exit(EX_NOINPUT)

    for command, argument_list in command_map.items():
        full_cmd_str = process_arguments(command, argument_list)
        if parsed.verbose:
            print(full_cmd_str)
        run(full_cmd_str.split(), check=False)
    # print(unparsed)
    sys.exit(EX_OK)


if __name__ == "__main__":
    main()
