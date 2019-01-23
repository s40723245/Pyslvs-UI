# -*- coding: utf-8 -*-

"""'info' module contains Pyslvs program information."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from .info import (
    INFO,
    ARGUMENTS,
    __version__,
    check_update
)
from .about import (
    Splash,
    PyslvsAbout,
    html
)

__all__ = [
    'INFO',
    'ARGUMENTS',
    '__version__',
    'check_update',
    'Splash',
    'PyslvsAbout',
    'html'
]
