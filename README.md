# yaml2cmd

Parses yaml files to generate (usually long) shell commands.

# Installation

Clone this repo:
```bash
git clone https://github.com/fpadula/yaml2cmd.git
```
Navigate into the cloned folder and install it using `pip`:
```bash
cd yaml2cmd
pip install -e .
```
If you get the error `externally-managed-environment`, append `--break-system-packages` to the installation command:
```bash
pip install -e . --break-system-packages
```

# Usage

The script can be run with:
```bash
y2c -f <yaml file path>
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
