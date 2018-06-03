# wgal initialisation code.
# Copyright (C) 2018 Ryan Rueger and Contributors.

import os
import sys
import argparse
import pathlib
import shutil

import wgal.utils


class WebGallery(object):
    """The main class that encapsulates the high level use of WebGallery.

    To run wgal, call:

    >>> import wgal

    >>> wg = WebGallery()
    >>> wg.run()
    """

    def run(self):
        """Invoke everything."""
        args = self.__parse_options()

        self.__check_paths(args)
        self.__todo(args)

    def __parse_options(self):
        """Parse command line options."""
        parser = argparse.ArgumentParser()

        parser.add_argument('source',
                            metavar='SOURCE',
                            help="Specify source directory of images.")

        parser.add_argument("web",
                           metavar="WEB",
                           help="Specify destination \
                                directory for the website.")

        args = parser.parse_args()

        return args

    def __check_paths(self, paths):
        """Check whether configuration paths are read-/writable."""
        try:
            for file in wgal.utils.find(paths.source):
                if not os.access(file, os.R_OK):
                    raise Exception(
                        "Source path not readable: {}".format(paths.source))

            if not os.path.isdir(paths.web):
                print("wgal WARNING: Creating website directory: {}"
                        .format(paths.web))

            pathlib.Path(paths.web).mkdir(exist_ok=True)

            for file in wgal.utils.find(paths.web):
                if not os.access(file, os.R_OK | os.W_OK):
                    raise Exception(
                        "Source path not writable: {}".format(paths.source))
        except Exception as error:
            print("wgal ERROR: " + " ".join(error.args))
            sys.exit(1)

    def __todo(self, args):
        """Check differences between current source and active album.

        Firstly, check whether args.web points to an existing instance
        of a web gallery. If not create a new one.
        Then go through each source image, and note those who's
        derivatives have not been created.

        The tree of a web gallery instance looks like this
        .
        ├── m
        │   ├── f
        │   ├── p
        │   └── t
        ├── r
        │   ├── css
        │   │   ├── progressive-image.css
        │   │   ├── progressive-image.min.css
        │   │   ├── single.css
        │   │   └── tiled.css
        │   └── js
        │       ├── progressive-image.js
        │       └── progressive-image.min.js
        └── s
        """
        # Where the templates are kept.
        root = os.path.dirname(wgal.__file__)
        originals = os.path.join(root, "website")
        # First, define where we expect all the resource/media files
        # to be relative to the root of any generic web album instance.
        # Then check if the instance defined by paths.web contains these
        # files.
        rel_resources_root = "r"
        # Resource directories for CSS and JS.
        rel_resources_types = ["css", "js"]
        rel_resources = [os.path.join(rel_resources_root, typ)
                    for typ in rel_resources_types]
        rel_media_root = "m"
        # Media directories for Full, Preview and Thumbnail quality images.
        rel_media_types = ["f", "p", "t"]
        rel_media = [os.path.join(rel_media_root, typ)
                    for typ in rel_media_types]
        # Directory containing single photo html files.
        rel_single = "s"

        css = [os.path.join(rel_resources[0], css_file)
                for css_file in
                ["progressive-image.css",
                "progressive-image.min.css",
                "single.css",
                "tiled.css"]]
        js = [os.path.join(rel_resources[1], js_file)
                for js_file in
                ["progressive-image.js",
                "progressive-image.min.js"]]

        # Paths of directories in the current instance as
        # specified in args.web.
        web_resources = [os.path.join(args.web, typ) for typ in rel_resources]
        web_media = [os.path.join(args.web, typ) for typ in rel_media]
        web_single = os.path.join(args.web, rel_single)

        for dir in [*web_resources, *web_media, web_single]:
            if not os.path.isdir(dir):
                print("wgal WARNING: Creating directory: {}".format(dir))
            pathlib.Path(dir).mkdir(exist_ok=True, parents=True)

        for file in [*css, *js]:
            web_file = os.path.join(args.web, file)
            original_file = os.path.join(originals, file)
            if not os.path.isfile(web_file):
                print("wgal WARNING: Creating file: {}".format(file))
                shutil.copy2(original_file, web_file)

    def __process_images(self):
        """Create derivatives of the source files and create thumbnails."""

    def __make_html(self):
        """Write HTML."""
