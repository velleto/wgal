# wgal initialisation code.
# Copyright (C) 2018 Ryan Rueger and Contributors.


class WebGallery(object):
    """The main class that encapsulates the high level use of WebGallery.

    To run wgal, call:

        import wgal

        wg = WebGallery()
        wg.run()
    """

    def run(self):
        """Invoke everything."""

    def __parse_options(self):
        """Parse command line options."""

    def __check_paths(self):
        """Check whether configuration paths are read-/writable."""

    def __todo(self):
        """Check differences between current source and active album."""

    def __process_images(self):
        """Create derivatives of the source files and create thumbnails."""

    def __make_html(self):
        """Write HTML."""
