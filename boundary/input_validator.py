"""FR-01 input contract validation at the Boundary layer."""

from boundary.constants import (
    BLANK_VALUE,
    EXPECTED_BLANK_COUNT,
    MAX_CELL_VALUE,
    MIN_CELL_VALUE,
)
from boundary.schemas import ErrorResponse

_INVALID_BLANK_COUNT_CODE = "INVALID_BLANK_COUNT"
_INVALID_BLANK_COUNT_MESSAGE = "빈칸(0)은 정확히 2개여야 한다."

_VALUE_OUT_OF_RANGE_CODE = "VALUE_OUT_OF_RANGE"
_VALUE_OUT_OF_RANGE_MESSAGE = "값은 0 또는 1~16만 허용된다."

_DUPLICATE_NON_ZERO_CODE = "DUPLICATE_NON_ZERO_VALUE"
_DUPLICATE_NON_ZERO_MESSAGE = "0을 제외한 숫자는 중복될 수 없다."


class InputValidator:
    """Validates blank count and uniqueness for partial magic square grids."""

    def validate(self, grid: list[list[int]]) -> ErrorResponse | None:
        """Return an error response when input contract rules are violated.

        Args:
            grid: 4x4 puzzle matrix that already passed size validation.

        Returns:
            ErrorResponse when validation fails; None when input is valid.
        """
        blank_count = sum(
            1
            for row in grid
            for value in row
            if value == BLANK_VALUE
        )
        if blank_count != EXPECTED_BLANK_COUNT:
            return ErrorResponse(
                code=_INVALID_BLANK_COUNT_CODE,
                message=_INVALID_BLANK_COUNT_MESSAGE,
            )

        seen_non_zero: set[int] = set()
        for row in grid:
            for value in row:
                if value == BLANK_VALUE:
                    continue
                if value < MIN_CELL_VALUE or value > MAX_CELL_VALUE:
                    return ErrorResponse(
                        code=_VALUE_OUT_OF_RANGE_CODE,
                        message=_VALUE_OUT_OF_RANGE_MESSAGE,
                    )
                if value in seen_non_zero:
                    return ErrorResponse(
                        code=_DUPLICATE_NON_ZERO_CODE,
                        message=_DUPLICATE_NON_ZERO_MESSAGE,
                    )
                seen_non_zero.add(value)

        return None
