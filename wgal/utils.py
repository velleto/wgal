# Copyright (C) 2018 Ryan Rueger

import os


def find(path):

    all_files = []
    for parent, child, files in os.walk(path):
        for file in files:
            all_files.append(os.path.join(parent, file))

    return all_files
