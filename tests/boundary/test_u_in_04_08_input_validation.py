"""Track A — FR-01 input validation (U-IN-04~08).

U-IN-01~03: Report/08 Full RED — do not duplicate here.
SSOT: Report/06 §7, docs/PRD_MagicSquare.md v0.2 (AC-FR01-02~04).
"""

from boundary.input_validator import InputValidator
from tests.entity.grids import GRID_G1


class TestUIn04ThreeBlanks:
    """U-IN-04 — three blank cells → INVALID_BLANK_COUNT failure envelope."""

    def test_u_in_04_three_blanks_returns_e002(self) -> None:
        """U-IN-04, AC-FR01-02 — 0이 3개이면 INVALID_BLANK_COUNT envelope 반환."""
        matrix = [
            [16, 2, 3, 13],
            [5, 11, 10, 8],
            [9, 0, 0, 12],
            [4, 14, 0, 1],
        ]
        validator = InputValidator()

        result = validator.validate(matrix)

        assert result is not None
        assert result.code == "INVALID_BLANK_COUNT"
        assert result.message == "빈칸(0)은 정확히 2개여야 한다."


class TestUIn05OutOfRange:
    """U-IN-05 — value out of range → VALUE_OUT_OF_RANGE failure envelope."""

    def test_u_in_05_out_of_range_value_returns_e004(self) -> None:
        """U-IN-05, AC-FR01-03 — 범위 외 값(17) 시 VALUE_OUT_OF_RANGE envelope 반환."""
        matrix = [
            [16, 2, 3, 13],
            [5, 11, 10, 8],
            [9, 0, 17, 12],
            [4, 14, 0, 1],
        ]
        validator = InputValidator()

        result = validator.validate(matrix)

        assert result is not None
        assert result.code == "VALUE_OUT_OF_RANGE"
        assert result.message == "값은 0 또는 1~16만 허용된다."


class TestUIn06DuplicateNonZero:
    """U-IN-06 — duplicate non-zero → DUPLICATE_NON_ZERO_VALUE failure envelope."""

    def test_u_in_06_duplicate_non_zero_returns_e005(self) -> None:
        """U-IN-06, AC-FR01-04 — 0 제외 중복(7) 시 DUPLICATE_NON_ZERO_VALUE envelope 반환."""
        matrix = [
            [16, 2, 3, 13],
            [5, 11, 10, 8],
            [9, 7, 7, 12],
            [4, 14, 0, 0],
        ]
        validator = InputValidator()

        result = validator.validate(matrix)

        assert result is not None
        assert result.code == "DUPLICATE_NON_ZERO_VALUE"
        assert result.message == "0을 제외한 숫자는 중복될 수 없다."


class TestUIn07NoBlanks:
    """U-IN-07 — zero blank cells → INVALID_BLANK_COUNT failure envelope."""

    def test_u_in_07_no_blanks_returns_e002(self) -> None:
        """U-IN-07, AC-FR01-02 — 빈칸(0) 0개 시 INVALID_BLANK_COUNT envelope 반환."""
        matrix = [
            [16, 2, 3, 13],
            [5, 11, 10, 8],
            [9, 7, 6, 12],
            [4, 14, 15, 1],
        ]
        validator = InputValidator()

        result = validator.validate(matrix)

        assert result is not None
        assert result.code == "INVALID_BLANK_COUNT"
        assert result.message == "빈칸(0)은 정확히 2개여야 한다."


class TestUIn08ValidG1Passes:
    """U-IN-08 — valid G1 contract passes input verification."""

    def test_u_in_08_valid_g1_passes_input_verification(self) -> None:
        """U-IN-08, FR-01 — G1(빈칸 2개) 입력 검증 통과."""
        validator = InputValidator()

        result = validator.validate(GRID_G1)

        assert result is None
