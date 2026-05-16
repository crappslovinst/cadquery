"""Geometry primitives and transformations for CadQuery.

This module provides core geometric types including vectors, matrices,
and transformation objects used throughout CadQuery.
"""

import math
from typing import overload, Sequence, Tuple, Union

from OCP.gp import (
    gp_Vec,
    gp_Pnt,
    gp_Dir,
    gp_Ax1,
    gp_Ax2,
    gp_Ax3,
    gp_Trsf,
    gp_GTrsf,
    gp_XYZ,
    gp_EulerSequence,
)

VectorLike = Union["Vector", Tuple[float, float, float], Sequence[float]]


class Vector:
    """A 3D vector with common geometric operations.

    Wraps OCC gp_Vec for use in CadQuery operations.

    Examples:
        >>> v = Vector(1, 0, 0)
        >>> v.Length()
        1.0
        >>> v.normalized()
        Vector(1.0, 0.0, 0.0)
    """

    def __init__(self, *args):
        if len(args) == 3:
            self._wrapped = gp_Vec(*args)
        elif len(args) == 1:
            if isinstance(args[0], gp_Vec):
                self._wrapped = args[0]
            elif isinstance(args[0], gp_Pnt):
                self._wrapped = gp_Vec(args[0].XYZ())
            elif isinstance(args[0], gp_Dir):
                self._wrapped = gp_Vec(args[0])
            elif isinstance(args[0], (list, tuple)) and len(args[0]) == 3:
                self._wrapped = gp_Vec(*args[0])
            elif isinstance(args[0], Vector):
                self._wrapped = args[0]._wrapped
            else:
                raise TypeError(f"Cannot construct Vector from {type(args[0])}")
        elif len(args) == 2:
            # 2D vector, z=0
            self._wrapped = gp_Vec(args[0], args[1], 0)
        else:
            raise TypeError(f"Expected 1, 2, or 3 arguments, got {len(args)}")

    @property
    def x(self) -> float:
        return self._wrapped.X()

    @property
    def y(self) -> float:
        return self._wrapped.Y()

    @property
    def z(self) -> float:
        return self._wrapped.Z()

    def Length(self) -> float:
        """Return the length (magnitude) of the vector."""
        return self._wrapped.Magnitude()

    def normalized(self) -> "Vector":
        """Return a unit vector in the same direction."""
        return Vector(self._wrapped.Normalized())

    def dot(self, other: "Vector") -> float:
        """Dot product with another vector."""
        return self._wrapped.Dot(other._wrapped)

    def cross(self, other: "Vector") -> "Vector":
        """Cross product with another vector."""
        return Vector(self._wrapped.Crossed(other._wrapped))

    def add(self, other: "Vector") -> "Vector":
        return Vector(self._wrapped.Added(other._wrapped))

    def sub(self, other: "Vector") -> "Vector":
        return Vector(self._wrapped.Subtracted(other._wrapped))

    def multiply(self, scale: float) -> "Vector":
        return Vector(self._wrapped.Multiplied(scale))

    def toPnt(self) -> gp_Pnt:
        return gp_Pnt(self._wrapped.XYZ())

    def toDir(self) -> gp_Dir:
        return gp_Dir(self._wrapped)

    def getAngle(self, other: "Vector") -> float:
        """Angle in radians between this vector and another."""
        return self._wrapped.Angle(other._wrapped)

    def getAngleDegrees(self, other: "Vector") -> float:
        """Angle in degrees between this vector and another. More convenient than getAngle."""
        return math.degrees(self._wrapped.Angle(other._wrapped))

    def __a