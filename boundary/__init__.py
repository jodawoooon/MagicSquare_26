"""Boundary layer — input validation and error response contracts."""

from boundary.schemas import ErrorResponse
from boundary.validator import BoundaryValidator

__all__ = ["BoundaryValidator", "ErrorResponse"]
