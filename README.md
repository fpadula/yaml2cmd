# yaml2cmd

Parses yaml files to generate (usually long) shell commands.

# Installation

Clone this repo and run `yaml2cmd.py`

# Usage

The script can be run with:
```bash
yaml2cmd.py yaml_file
```

Where `yaml_file` is a path to a `YAML` file that has to follow the structure:

```YAML
command:
  - argument_0
  - argument_1
  - argument_2
  .
  .
  .
  - argument_N-1
    - argument_N-1 value 1
    - argument_N-1 value 2
    - argument_N-1 value 3
  - argument_N
```

An example file can be found at `examples/rocker.yaml`

# Roadmap
- [ ] Add support for environment variables 
- [ ] Add support for dynamic yaml files (that accept parameters from the command line) 
