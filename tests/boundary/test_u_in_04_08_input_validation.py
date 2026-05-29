"""Track A — FR-01 input validation RED skeletons (U-IN-04~08).

U-IN-01~03: Report/08 Full RED — do not duplicate here.
SSOT: Report/06 §7, docs/PRD_MagicSquare.md v0.2 (AC-FR01-02~04).
"""

import pytest

from boundary.input_validator import InputValidator


class TestUIn04ThreeBlanks:
    """U-IN-04 — three blank cells → E002 failure envelope."""

    def test_u_in_04_three_blanks_returns_e002(self) -> None:
        """U-IN-04, AC-FR01-02 — 0이 3개이면 E002 envelope 반환."""
        # Given
        # matrix = [
        #     [16, 2, 3, 13],
        #     [5, 11, 10, 8],
        #     [9, 0, 0, 12],
        #     [4, 14, 0, 1],
        # ]
        # validator = InputValidator()

        # When
        # result = validator.validate(matrix)

        # Then — success==false; code==E002; message exact (GREEN)
        pytest.fail("RED: U-IN-04 — 빈칸(0) 3개 시 E002 failure envelope")


class TestUIn05OutOfRange:
    """U-IN-05 — value out of range → E004 failure envelope."""

    def test_u_in_05_out_of_range_value_returns_e004(self) -> None:
        """U-IN-05, AC-FR01-03 — 범위 외 값(17) 시 E004 envelope 반환."""
        # Given
        # matrix = [
        #     [16, 2, 3, 13],
        #     [5, 11, 10, 8],
        #     [9, 0, 17, 12],
        #     [4, 14, 0, 1],
        # ]
        # validator = InputValidator()

        # When
        # result = validator.validate(matrix)

        # Then
        pytest.fail("RED: U-IN-05 — 값 0 또는 1~16 외 시 E004 failure envelope")


class TestUIn06DuplicateNonZero:
    """U-IN-06 — duplicate non-zero → E005 failure envelope."""

    def test_u_in_06_duplicate_non_zero_returns_e005(self) -> None:
        """U-IN-06, AC-FR01-04 — 0 제외 중복(7) 시 E005 envelope 반환."""
        # Given
        # matrix = [
        #     [16, 2, 3, 13],
        #     [5, 11, 10, 8],
        #     [9, 7, 7, 12],
        #     [4, 14, 0, 0],
        # ]
        # validator = InputValidator()

        # When
        # result = validator.validate(matrix)

        # Then
        pytest.fail("RED: U-IN-06 — 0 제외 중복 시 E005 failure envelope")


class TestUIn07NoBlanks:
    """U-IN-07 — zero blank cells → E002 failure envelope."""

    def test_u_in_07_no_blanks_returns_e002(self) -> None:
        """U-IN-07, AC-FR01-02 — 빈칸(0) 0개 시 E002 envelope 반환."""
        # Given
        # matrix = [
        #     [16, 2, 3, 13],
        #     [5, 11, 10, 8],
        #     [9, 7, 6, 12],
        #     [4, 14, 15, 1],
        # ]
        # validator = InputValidator()

        # When
        # result = validator.validate(matrix)

        # Then
        pytest.fail("RED: U-IN-07 — 빈칸(0) 0개 시 E002 failure envelope")


class TestUIn08ValidG1Passes:
    """U-IN-08 — valid G1 contract passes input verification."""

    def test_u_in_08_valid_g1_passes_input_verification(self) -> None:
        """U-IN-08, FR-01 — G1(빈칸 2개) 입력 검증 통과."""
        # Given
        # matrix = [
        #     [16, 2, 3, 13],
        #     [5, 0, 6, 8],
        #     [9, 11, 0, 12],
        #     [4, 14, 15, 1],
        # ]
        # validator = InputValidator()

        # When
        # result = validator.validate(matrix)

        # Then — success==true (GREEN)
        pytest.fail("RED: U-IN-08 — G1 유효 입력 시 검증 통과(success envelope)")
