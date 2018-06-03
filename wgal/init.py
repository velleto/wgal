# wgal initialisation code.
# Copyright (C) 2018 Ryan Rueger and Contributors.

import os
import sys
import argparse

import wgal.utils


class WebGallery(object):
    """The main class that encapsulates the high level use of WebGallery.

    To run wgal, call:

    >>> inmport wgal

    >>> wg = WebGallery()
    >>> wg.run()
    """

    def run(self):
        """Invoke everything."""
        args = self.__parse_options()

        self.__check_paths(args)

    def __parse_options(self):
        """Parse command line options."""
        parser = argparse.ArgumentParser()

        parser.add_argument('source',
                            metavar='SOURCE',
                            help="Specify source directory of images.")

        parser.add_argument("web",
                           metavar="WEB",
                           help="Specify destination directory for the website.")

        args = parser.parse_args()

        return args

    def __check_paths(self, paths):
        """Check whether configuration paths are read-/writable."""

        try:
            for file in wgal.utils.find(paths.source):
                if not os.access(file, os.R_OK):
                    raise Exception(
                        "Source path not readable: {}".format(paths.source))
            for file in wgal.utils.find(paths.web):
                if not os.access(file, os.R_OK | os.W_OK):
                    raise Exception(
                        "Source path not writable: {}".format(paths.source))
        except Exception as error:
            print("wgal ERROR: " + " ".join(error.args))
            sys.exit(1)

    def __todo(self):
        """Check differences between current source and active album."""

    def __process_images(self):
        """Create derivatives of the source files and create thumbnails."""

    def __make_html(self):
        """Write HTML."""
