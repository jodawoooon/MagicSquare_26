"""Golden Master scenario definitions (GM-1 / GM-2)."""

from dataclasses import dataclass
from typing import Final, Literal

OutcomeKind = Literal["success", "error"]

GRID_NORMAL_SUCCESS: Final[list[list[int]]] = [
    [16, 0, 0, 13],
    [5, 11, 10, 8],
    [9, 7, 6, 12],
    [4, 14, 15, 1],
]

GRID_REVERSE_SUCCESS: Final[list[list[int]]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 0, 0, 12],
    [4, 14, 15, 1],
]

GRID_INVALID_BLANK_COUNT: Final[list[list[int]]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 0, 0, 12],
    [4, 14, 0, 1],
]

GRID_DUPLICATE_NUMBER: Final[list[list[int]]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 7, 12],
    [4, 14, 0, 0],
]

GRID_NO_VALID_SOLUTION: Final[list[list[int]]] = [
    [16, 2, 3, 13],
    [5, 0, 6, 8],
    [9, 11, 0, 12],
    [4, 14, 15, 1],
]


@dataclass(frozen=True)
class GoldenMasterScenario:
    """Single Golden Master input scenario with contract metadata."""

    test_id: str
    name: str
    grid: list[list[int]]
    outcome_kind: OutcomeKind
    expect_small_first: bool | None = None
    expected_error_code: str | None = None


SCENARIOS: Final[tuple[GoldenMasterScenario, ...]] = (
    GoldenMasterScenario(
        test_id="GM-TC-01",
        name="normal_success",
        grid=GRID_NORMAL_SUCCESS,
        outcome_kind="success",
        expect_small_first=True,
    ),
    GoldenMasterScenario(
        test_id="GM-TC-02",
        name="reverse_success",
        grid=GRID_REVERSE_SUCCESS,
        outcome_kind="success",
        expect_small_first=False,
    ),
    GoldenMasterScenario(
        test_id="GM-TC-03",
        name="invalid_blank_count",
        grid=GRID_INVALID_BLANK_COUNT,
        outcome_kind="error",
        expected_error_code="INVALID_BLANK_COUNT",
    ),
    GoldenMasterScenario(
        test_id="GM-TC-04",
        name="duplicate_number",
        grid=GRID_DUPLICATE_NUMBER,
        outcome_kind="error",
        expected_error_code="DUPLICATE_NON_ZERO_VALUE",
    ),
    GoldenMasterScenario(
        test_id="GM-TC-05",
        name="no_valid_solution",
        grid=GRID_NO_VALID_SOLUTION,
        outcome_kind="error",
        expected_error_code="NO_VALID_ASSIGNMENT",
    ),
)

SCENARIOS_BY_ID: Final[dict[str, GoldenMasterScenario]] = {
    scenario.test_id: scenario for scenario in SCENARIOS
}
