"""CadQuery - A parametric 3D CAD scripting framework built on top of OCCT.

This module exposes the primary CadQuery API for creating 3D models
using a fluent, chainable interface.

Personal fork notes:
- Using this for learning OCCT and parametric modeling
- Main branch tracks upstream CadQuery/cadquery
- Added cq_version helper for quick version checks in scripts
- Added cq_version() return value so it can be used in assertions/tests
"""

from .cq import CQ, Workplane
from .occ_impl.geom import Vector, Matrix, Plane, Location
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
    CompSolid,
)
from .occ_impl.assembly import (
    Assembly,
    Constraint,
)
from .selectors import (
    Selector,
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    DirectionMinMaxSelector,
    RadiusNthSelector,
    CenterNthSelector,
    DirectionNthSelector,
    LengthNthSelector,
    AreaNthSelector,
    BinarySelector,
    AndSelector,
    SumSelector,
    SubtractSelector,
    InverseSelector,
    StringSyntaxSelector,
)
from .sketch import Sketch
from .cq_types import Real, VectorLike
from . import exporters, importers

# Package metadata
__version__ = "2.4.0"
__author__ = "CadQuery Contributors"
__license__ = "Apache License 2.0"


def cq_version():
    """Quick helper to print version info - handy when jumping between envs.

    Returns the version string so it can also be used programmatically,
    e.g. assert '2.4' in cq_version()
    """
    version_str = f"CadQuery {__version__} | {__license__}"
    print(version_str)
    return version_str


__all__ = [
    # Core workplane
    "CQ",
    "Workplane",
    # Geometry primitives
    "Vector",
    "Matrix",
    "Plane",
    "Location",
    # Shapes
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    "CompSolid",
    # Assembly
    "Assembly",
    "Constraint",
    # Selectors
    "Selector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "DirectionMinMaxSelector",
    "RadiusNthSelector",
    "CenterNthSelector",
    "DirectionNthSelector",
    "LengthNthSelector",
    "AreaNthSelector",
    "BinarySelector",
    "AndSelector",
    "SumSelector",
    "SubtractSelector",
    "InverseSelector",
    "StringSyntaxSelector",
    # Sketch
    "Sketch",
    # Types
    "Real",
    "VectorLike",
    # Submodules
    "exporters",
    "importers",
    # Helpers
    "cq_version",
]
