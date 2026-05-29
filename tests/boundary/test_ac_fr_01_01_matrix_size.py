"""AC-FR-01-01 matrix size validation — Track A Boundary RED tests.

AC-FR-01-01, PRD §8.1 INVALID_SIZE
"""

from pydantic import BaseModel

from tests.boundary.constants import INVALID_SIZE_CODE, INVALID_SIZE_MESSAGE

# AC-FR-01-01: 본 모듈이 다루는 유일한 Acceptance Criteria
MODULE_AC_SCOPE = frozenset({"AC-FR-01-01"})

# AC-FR-01-02~05, FR-02~05 — 본 RED 커밋 범위 외
EXCLUDED_AC_IDS = frozenset(
    {
        "AC-FR-01-02",
        "AC-FR-01-03",
        "AC-FR-01-04",
        "AC-FR-01-05",
        "AC-FR-02-01",
        "AC-FR-02-02",
        "AC-FR-03-01",
        "AC-FR-03-02",
        "AC-FR-04-01",
        "AC-FR-04-02",
        "AC-FR-05-01",
        "AC-FR-05-02",
        "AC-FR-05-03",
        "AC-FR-05-04",
    }
)

GRID_3X4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


def test_none_grid_returns_invalid_size_code_message(boundary_validator) -> None:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — grid=None 시 표준 실패 응답 반환."""
    # AC-FR-01-01
    # Given
    grid = None

    # When
    result = boundary_validator.validate(grid)

    # Then
    assert result.code == INVALID_SIZE_CODE
    assert result.message == INVALID_SIZE_MESSAGE


def test_empty_list_grid_returns_invalid_size_code_message(boundary_validator) -> None:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — grid=[] 시 INVALID_SIZE 반환."""
    # AC-FR-01-01
    # Given
    grid: list[list[int]] = []

    # When
    result = boundary_validator.validate(grid)

    # Then
    assert result.code == INVALID_SIZE_CODE
    assert result.message == INVALID_SIZE_MESSAGE


def test_four_empty_rows_grid_returns_invalid_size_code_message(
    boundary_validator,
) -> None:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — grid=[[]]*4 시 INVALID_SIZE 반환."""
    # AC-FR-01-01
    # Given
    grid = [[]] * 4

    # When
    result = boundary_validator.validate(grid)

    # Then
    assert result.code == INVALID_SIZE_CODE
    assert result.message == INVALID_SIZE_MESSAGE


def test_3x4_grid_returns_invalid_size_code_message(boundary_validator) -> None:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 3×4 행렬 시 INVALID_SIZE 반환."""
    # AC-FR-01-01
    # Given
    grid = GRID_3X4

    # When
    result = boundary_validator.validate(grid)

    # Then
    assert result.code == INVALID_SIZE_CODE
    assert result.message == INVALID_SIZE_MESSAGE


def test_none_grid_message_exact_match_prd_section_8_1_string(
    boundary_validator,
) -> None:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — message 문자 단위 동일성 검증."""
    # AC-FR-01-01
    # Given
    grid = None
    expected_message = "Grid must be 4x4."

    # When
    result = boundary_validator.validate(grid)

    # Then
    assert result.message == expected_message
    assert len(result.message) == len(expected_message)
    assert result.message.encode("utf-8") == expected_message.encode("utf-8")


def test_none_grid_returns_error_response_struct_type(boundary_validator) -> None:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 반환 타입이 ErrorResponse 구조체."""
    # AC-FR-01-01
    # Given
    from boundary.schemas import ErrorResponse

    grid = None

    # When
    result = boundary_validator.validate(grid)

    # Then
    assert isinstance(result, ErrorResponse)
    assert isinstance(result, BaseModel)
    validated = ErrorResponse.model_validate(
        {"code": result.code, "message": result.message}
    )
    assert validated.code == INVALID_SIZE_CODE


def test_scope_excludes_ac_fr_01_02_to_05_and_fr_02_to_05_cases() -> None:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — AC-FR-01-02~05·FR-02~05 미포함 확인."""
    # AC-FR-01-01
    # Given
    module_scope = MODULE_AC_SCOPE
    excluded = EXCLUDED_AC_IDS

    # When / Then
    assert module_scope == frozenset({"AC-FR-01-01"})
    assert module_scope.isdisjoint(excluded)
    assert "AC-FR-01-02" not in module_scope
    assert "AC-FR-01-03" not in module_scope
    assert "AC-FR-01-04" not in module_scope
    assert "AC-FR-01-05" not in module_scope
