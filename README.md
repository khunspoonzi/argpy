# argpy

A high-level shorthand argument parser for Python 3 or above

---

## Overview

The objective of argpy is simply to strengthen one's propensity to utilize argparsing in Python scripts by making the definition of command line arguments slightly less tedious.

---

## Installation

Run `pip3 install argpy`

---

## Arguments

|   var   |                    name                     | type | default |
| :-----: | :-----------------------------------------: | :--: | :-----: |
| options | [Options](#defining-and-retrieving-options) | list |  n / a  |

---

## Examples

### Importing the Module

```
from argpy import argpy
```

### Defining and Retrieving Options

Options are passed into argpy in the form of a list of dictionaries. Here each item or element within the list represents one option. In the example below, option one is defined as name with a short form flag of -n and a long form flag of --name. The "dest" key defines how the passed in option will be accessed from within the program while the "help" key defines any additional help text that will be accessible by the user passing in the option via the command line. The second option demonstrates how to pass in a boolean argument, which defaults to False.

```
# Define options
options = [
      {"flags": ("-n", "--name"), "dest": "name", "help": "The object's name"},
      {
          "flags": ("-a", "--activate"),
          "dest": "activate",
          "bool": True,
          "help": "Whether to activate the object",
      },
  ]
```

The above options can be implemented and retrieved by continuing the script as follows:

```
# Get arguments
arguments = argpy(options)

# Get name, activate
name = arguments.name
activate = arguments.activate
```

In case you're wondering what this would look like from that command line, see below.

```
python3 my_script.py --name OptimusPrime --activate
```

or

```
python3 my_script.py -n OptimusPrime -a
```
