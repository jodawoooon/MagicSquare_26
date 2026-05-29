"""FR-01 matrix size validation at the Boundary layer."""

from dataclasses import dataclass

_INVALID_SIZE_CODE = "INVALID_SIZE"
_INVALID_SIZE_MESSAGE = "Grid must be 4x4."


@dataclass(frozen=True)
class _SizeErrorResponse:
    """Minimal failure payload for AC-FR-01-01 green-1 (TA-RED-001)."""

    code: str
    message: str


class BoundaryValidator:
    """Validates 4x4 grid dimensions before Control/Entity processing."""

    def validate(self, grid: list[list[int]] | None) -> _SizeErrorResponse:
        """Return INVALID_SIZE when grid is None.

        Args:
            grid: Puzzle matrix or None when input is missing.

        Returns:
            Size error response when grid is None.

        Raises:
            NotImplementedError: For non-None inputs (later RED bundles).
        """
        if grid is None:
            return _SizeErrorResponse(
                code=_INVALID_SIZE_CODE,
                message=_INVALID_SIZE_MESSAGE,
            )
        raise NotImplementedError("Non-None grid is out of AC-FR-01-01 green-1 scope.")
