"""ScreenPresenter contract tests — no PyQt required (Report/12, ECB Screen→UIBoundary)."""

from boundary.schemas import ErrorResponse
from boundary.screen.presenter import ScreenPresenter, SolveSuccess, ValidationSuccess
from tests.boundary.constants import INVALID_SIZE_CODE, INVALID_SIZE_MESSAGE
from tests.entity.grids import D_SOL_01_EXPECTED, GRID_G1, GRID_G1_SOL, GRID_G3


class TestScreenPresenterValidate:
    """Size validation mapping for the GUI adapter."""

    def test_validate_null_grid_returns_invalid_size_envelope(self) -> None:
        """null grid → ErrorResponse(INVALID_SIZE)."""
        presenter = ScreenPresenter()

        result = presenter.validate(None)

        assert isinstance(result, ErrorResponse)
        assert result.code == INVALID_SIZE_CODE
        assert result.message == INVALID_SIZE_MESSAGE

    def test_validate_valid_g1_returns_validation_success(self) -> None:
        """4×4 G1 → ValidationSuccess."""
        presenter = ScreenPresenter()

        result = presenter.validate(GRID_G1)

        assert isinstance(result, ValidationSuccess)


class TestScreenPresenterSolve:
    """Solve outcome mapping for the GUI adapter."""

    def test_solve_g1_sol_returns_solve_success_with_filled_grid(self) -> None:
        """Valid partial grid → SolveSuccess with int[6] and filled grid."""
        presenter = ScreenPresenter()

        result = presenter.solve(GRID_G1_SOL)

        assert isinstance(result, SolveSuccess)
        assert result.solution == D_SOL_01_EXPECTED
        assert result.filled_grid[0][1] == 2
        assert result.filled_grid[0][2] == 3

    def test_solve_g3_returns_no_valid_assignment_envelope(self) -> None:
        """Unsolvable grid → ErrorResponse(NO_VALID_ASSIGNMENT)."""
        presenter = ScreenPresenter()

        result = presenter.solve(GRID_G3)

        assert isinstance(result, ErrorResponse)
        assert result.code == "NO_VALID_ASSIGNMENT"

    def test_solve_null_returns_invalid_size_envelope(self) -> None:
        """null grid → ErrorResponse without calling domain solver."""
        presenter = ScreenPresenter()

        result = presenter.solve(None)

        assert isinstance(result, ErrorResponse)
        assert result.code == INVALID_SIZE_CODE

    def test_solve_invalid_blank_count_returns_input_error_envelope(self) -> None:
        """Three blanks → INVALID_BLANK_COUNT via pipeline."""
        matrix = [
            [16, 2, 3, 13],
            [5, 11, 10, 8],
            [9, 0, 0, 12],
            [4, 14, 0, 1],
        ]
        presenter = ScreenPresenter()

        result = presenter.solve(matrix)

        assert isinstance(result, ErrorResponse)
        assert result.code == "INVALID_BLANK_COUNT"
