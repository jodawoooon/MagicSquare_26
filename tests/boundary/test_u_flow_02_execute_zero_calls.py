"""Track A — U-FLOW-02 extended: invalid input never calls execute.

SSOT: Report/06 §7, AC-FR01-05. Control mock/spy only — Domain mock 금지.
"""

from unittest.mock import MagicMock, patch

from boundary.ui_boundary import UIBoundary


class TestUFlow02ExecuteIsolation:
    """U-FLOW-02 — SolvePartialMagicSquare.execute call_count == 0 on invalid input."""

    def test_u_flow_02_null_matrix_never_calls_execute(self) -> None:
        """U-FLOW-02, AC-FR01-05 — matrix=null 시 execute 0회."""
        ui = UIBoundary()
        execute_spy = MagicMock(return_value=[1, 1, 1, 1, 1, 1])
        ui._pipeline._solve_partial.execute = execute_spy

        ui.solve(None)

        execute_spy.assert_not_called()

    def test_u_flow_02_e002_matrix_never_calls_execute(self) -> None:
        """U-FLOW-02 확장 — INVALID_BLANK_COUNT(빈칸 3개) 실패 시 execute 0회."""
        matrix = [
            [16, 2, 3, 13],
            [5, 11, 10, 8],
            [9, 0, 0, 12],
            [4, 14, 0, 1],
        ]
        ui = UIBoundary()
        execute_spy = MagicMock(return_value=[1, 1, 1, 1, 1, 1])
        ui._pipeline._solve_partial.execute = execute_spy

        ui.solve(matrix)

        execute_spy.assert_not_called()

    def test_u_flow_02_e004_matrix_never_calls_execute(self) -> None:
        """U-FLOW-02 확장 — VALUE_OUT_OF_RANGE 실패 시 execute 0회."""
        matrix = [
            [16, 2, 3, 13],
            [5, 11, 10, 8],
            [9, 0, 17, 12],
            [4, 14, 0, 1],
        ]
        ui = UIBoundary()
        execute_spy = MagicMock(return_value=[1, 1, 1, 1, 1, 1])
        ui._pipeline._solve_partial.execute = execute_spy

        ui.solve(matrix)

        execute_spy.assert_not_called()

    def test_u_flow_02_e005_matrix_never_calls_execute(self) -> None:
        """U-FLOW-02 확장 — DUPLICATE_NON_ZERO_VALUE 실패 시 execute 0회."""
        matrix = [
            [16, 2, 3, 13],
            [5, 11, 10, 8],
            [9, 7, 7, 12],
            [4, 14, 0, 0],
        ]
        ui = UIBoundary()
        execute_spy = MagicMock(return_value=[1, 1, 1, 1, 1, 1])
        ui._pipeline._solve_partial.execute = execute_spy

        ui.solve(matrix)

        execute_spy.assert_not_called()
