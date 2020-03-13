# -------------------------------------------------------------------------------------
# IMPORTS
# -------------------------------------------------------------------------------------

import argparse

from typing import List

# -------------------------------------------------------------------------------------
# ARGPY
# -------------------------------------------------------------------------------------


def argpy(options: List[dict]) -> dict:
    """ Uses argparse to retrieve arguments passed in from command line """

    # Initialize parser
    parser = argparse.ArgumentParser()

    # Iterate over args
    for option in options:

        # Extract kwargs
        option_names = option.pop("flags")

        # Determine if argument is boolean
        is_boolean = option.pop("bool", False)

        # Add boolean argument
        if is_boolean:
            parser.add_argument(
                *option_names, default=False, action="store_true", **option
            )

        # Add normal argument
        else:
            parser.add_argument(*option_names, **option)

    # Parse arguments
    return parser.parse_args()
