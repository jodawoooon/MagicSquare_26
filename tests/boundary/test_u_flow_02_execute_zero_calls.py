"""Track A — U-FLOW-02 extended: invalid input never calls execute.

SSOT: Report/06 §7, AC-FR01-05. Control mock/spy only — Domain mock 금지.
"""

import pytest

from boundary.ui_boundary import UIBoundary
from control.solve_partial import SolvePartialMagicSquare


class TestUFlow02ExecuteIsolation:
    """U-FLOW-02 — SolvePartialMagicSquare.execute call_count == 0 on invalid input."""

    def test_u_flow_02_null_matrix_never_calls_execute(self) -> None:
        """U-FLOW-02, AC-FR01-05 — matrix=null 시 execute 0회."""
        # Given
        # matrix = None
        # ui = UIBoundary()
        # # unittest.mock: patch SolvePartialMagicSquare.execute spy

        # When
        # result = ui.solve(matrix)

        # Then — execute.call_count == 0 (GREEN)
        pytest.fail("RED: U-FLOW-02 — null 입력 시 execute 0회")

    def test_u_flow_02_e002_matrix_never_calls_execute(self) -> None:
        """U-FLOW-02 확장 — E002(빈칸 개수) 실패 시 execute 0회."""
        # Given
        # matrix = [[16,2,3,13],[5,11,10,8],[9,0,0,12],[4,14,0,1]]  # 3 blanks
        # ui = UIBoundary()
        # # spy on execute

        # When
        # result = ui.solve(matrix)

        # Then
        pytest.fail("RED: U-FLOW-02 — E002 입력 시 execute 0회")

    def test_u_flow_02_e004_matrix_never_calls_execute(self) -> None:
        """U-FLOW-02 확장 — E004(범위) 실패 시 execute 0회."""
        # Given
        # matrix = [[16,2,3,13],[5,11,10,8],[9,0,17,12],[4,14,0,1]]
        # ui = UIBoundary()
        # # spy on execute

        # When
        # result = ui.solve(matrix)

        # Then
        pytest.fail("RED: U-FLOW-02 — E004 입력 시 execute 0회")

    def test_u_flow_02_e005_matrix_never_calls_execute(self) -> None:
        """U-FLOW-02 확장 — E005(중복) 실패 시 execute 0회."""
        # Given
        # matrix = [[16,2,3,13],[5,11,10,8],[9,7,7,12],[4,14,0,0]]
        # ui = UIBoundary()
        # # spy on execute

        # When
        # result = ui.solve(matrix)

        # Then
        pytest.fail("RED: U-FLOW-02 — E005 입력 시 execute 0회")
