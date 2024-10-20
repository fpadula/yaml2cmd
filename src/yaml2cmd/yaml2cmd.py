#!/usr/bin/python3

import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from os import EX_NOINPUT, EX_OK

from yaml import safe_load, YAMLError
from subprocess import run


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

    parser.add_argument("-f", dest="yaml_file_path",
                        help="Yaml file path", default="./command.yaml")

    parser.add_argument(
        "-v",
        dest="verbose",
        help="Enables verbose mode",
        action="store_true",
        default=False
    )

    parsed, _ = parser.parse_known_args()

    command_map = {}
    yaml_file_path = parsed.yaml_file_path
    verbose = parsed.verbose
    try:
        with open(yaml_file_path, "r", encoding="utf-8") as stream:
            try:
                command_map = safe_load(stream)
            except YAMLError:
                print(f"Could not process file '{yaml_file_path}'")
                sys.exit(EX_NOINPUT)
    except FileNotFoundError:
        if yaml_file_path == parser.get_default("yaml_file_path"):
            print(
                "Please specify a yaml file with the -f option or create a "
                f"\'{parser.get_default('yaml_file_path')}\' file"
            )
        print(f"Could not open file '{yaml_file_path}'")
        sys.exit(EX_NOINPUT)

    for command, argument_list in command_map.items():
        full_cmd_str = process_arguments(command, argument_list)
        if verbose:
            print(full_cmd_str)
        run(full_cmd_str.split(), check=False)
    sys.exit(EX_OK)


if __name__ == "__main__":
    main()
