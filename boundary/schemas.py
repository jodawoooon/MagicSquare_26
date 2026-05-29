"""Boundary response schemas."""

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Standard error response for Boundary validation failures."""

    code: str
    message: str
