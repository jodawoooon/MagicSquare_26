"""UI boundary facade — validate/solve envelope contract (FR-01, FR-05)."""

from boundary.constants import INVALID_SIZE_CODE
from boundary.error_messages import message_for_code
from boundary.pipeline import MagicSquarePipeline, SolveOutcome
from boundary.schemas import ErrorResponse
from boundary.validator import BoundaryValidator


class UIBoundary:
    """Single entry point for UI and integration solve flows."""

    def __init__(
        self,
        size_validator: BoundaryValidator | None = None,
        pipeline: MagicSquarePipeline | None = None,
    ) -> None:
        self._size_validator = size_validator or BoundaryValidator()
        self._pipeline = pipeline or MagicSquarePipeline(
            size_validator=self._size_validator,
        )

    def validate(self, grid: list[list[int]] | None) -> ErrorResponse | None:
        """Run matrix size validation for the UI contract.

        Args:
            grid: Puzzle matrix or None.

        Returns:
            ErrorResponse when size validation fails; None when size is valid.
        """
        try:
            return self._size_validator.validate(grid)
        except NotImplementedError:
            return None

    def solve(self, grid: list[list[int]] | None) -> SolveOutcome | ErrorResponse:
        """Validate and solve, returning a pipeline outcome or size error envelope.

        Args:
            grid: Puzzle matrix or None.

        Returns:
            SolveOutcome on success or input-rule failure; ErrorResponse for null
            or invalid matrix size.
        """
        size_error = self.validate(grid)
        if size_error is not None:
            return size_error
        if grid is None:
            return ErrorResponse(
                code=INVALID_SIZE_CODE,
                message=message_for_code(INVALID_SIZE_CODE),
            )
        return self._pipeline.solve(grid)
