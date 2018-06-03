# Copyright (C) 2018 Ryan Rueger

import sys
import os


def find(path):
    """Check whether directory exists, recursively list files it contains."""
    try:
        if not os.path.isdir(path):
            raise Exception("No such directory: {}".format(path))
    except Exception as error:
        print("wgal ERROR: find: " + " ".join(error.args))
        sys.exit(1)

    all_files = []
    for parent, child, files in os.walk(path):
        for file in files:
            all_files.append(os.path.join(parent, file))

    return all_files


def up(path):
    """Return parent directory of path."""
    return os.path.abspath(os.path.join(os.path.dirname(path), os.pardir))
