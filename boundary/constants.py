"""Boundary-layer constants for input contract and size validation."""

from typing import Final

GRID_SIZE: Final[int] = 4
BLANK_VALUE: Final[int] = 0
MIN_CELL_VALUE: Final[int] = 1
MAX_CELL_VALUE: Final[int] = 16
EXPECTED_BLANK_COUNT: Final[int] = 2
MAGIC_CONSTANT: Final[int] = 34

INVALID_SIZE_CODE: Final[str] = "INVALID_SIZE"
INVALID_SIZE_MESSAGE: Final[str] = "Grid must be 4x4."
