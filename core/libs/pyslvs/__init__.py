# -*- coding: utf-8 -*-

"""'pyslvs' module contains

+ Algorithm libraries to do triangular formula and dimentional synthesis.
+ Number synthesis and type synthesis libraries.
"""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from .rga import Genetic
from .firefly import Firefly
from .de import DiffertialEvolution
from .tinycadlib import (
    Coordinate,
    PLAP,
    PLLP,
    PLPP,
    expr_parser,
    expr_solving,
    expr_path,
    VPoint,
    VLink,
)
from .planarlinkage import build_planar
from .number import NumberSynthesis
from .topologic import topo, Graph
from .triangulation import vpoints_configure

__all__ = [
    'Genetic',
    'Firefly',
    'DiffertialEvolution',
    'Coordinate',
    'PLAP',
    'PLLP',
    'PLPP',
    'expr_parser',
    'expr_solving',
    'expr_path',
    'VPoint',
    'VLink',
    'build_planar',
    'NumberSynthesis',
    'topo',
    'Graph',
    'vpoints_configure',
]