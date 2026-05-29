"""AC-FR-01-01 Domain resolver isolation — Track A Control RED tests.

AC-FR-01-01, PRD §8.1 INVALID_SIZE
"""

from unittest.mock import create_autospec

import pytest

from tests.boundary.constants import INVALID_SIZE_CODE, INVALID_SIZE_MESSAGE


def test_none_grid_resolve_called_zero_times_spy_mock() -> None:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — resolve() 0회 호출 격리 검증."""
    # AC-FR-01-01
    # Given
    from control.resolver import MagicSquareResolver
    from entity.solver import MagicSquareSolver

    grid = None
    mock_solver = create_autospec(MagicSquareSolver, instance=True)
    resolver = MagicSquareResolver(solver=mock_solver)

    # When
    result = resolver.resolve(grid)

    # Then
    assert result.code == INVALID_SIZE_CODE
    assert result.message == INVALID_SIZE_MESSAGE
    mock_solver.resolve.assert_not_called()
    assert mock_solver.resolve.call_count == 0


def test_none_grid_resolve_mock_invocation_fails_test_guard() -> None:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — resolve() 호출 시 테스트 실패 처리."""
    # AC-FR-01-01
    # Given
    from control.resolver import MagicSquareResolver
    from entity.solver import MagicSquareSolver

    grid = None
    mock_solver = create_autospec(MagicSquareSolver, instance=True)
    mock_solver.resolve.return_value = [1, 2, 3, 4, 5, 6]
    resolver = MagicSquareResolver(solver=mock_solver)

    # When
    result = resolver.resolve(grid)

    # Then — Domain이 호출됐다면 성공 배열이 반환되며 RED 조건 위반
    assert result.code == INVALID_SIZE_CODE
    with pytest.raises(AssertionError):
        assert result == [1, 2, 3, 4, 5, 6]
    mock_solver.resolve.assert_not_called()
