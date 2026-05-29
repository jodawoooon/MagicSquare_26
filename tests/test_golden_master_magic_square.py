"""GM-2 — Golden Master per-scenario tests for Magic Square solver output."""

from __future__ import annotations

import pytest

from control.pipeline import MagicSquarePipeline
from tests.golden_master.approve import DEFAULT_GOLDEN_PATH, approve, approve_scenario
from tests.golden_master.capture import capture_scenario
from tests.golden_master.contract import assert_error_contract, assert_success_contract
from tests.golden_master.scenarios import SCENARIOS, GoldenMasterScenario

pytestmark = pytest.mark.golden_master


@pytest.fixture
def solve_pipeline() -> MagicSquarePipeline:
    """Shared pipeline for API result serialization."""
    return MagicSquarePipeline()


def _fail_with_diff(test_id: str, message: str) -> None:
    pytest.fail(f"{test_id} Golden Master mismatch:\n{message}")


@pytest.mark.parametrize(
    "scenario",
    SCENARIOS,
    ids=[scenario.test_id for scenario in SCENARIOS],
)
def test_golden_master_scenario_matches_baseline(scenario: GoldenMasterScenario) -> None:
    """[TAG][GoldenMaster] each scenario block matches golden_master_expected.txt."""
    passed, diff = approve_scenario(scenario, path=DEFAULT_GOLDEN_PATH, auto_create=False)
    if not passed:
        _fail_with_diff(scenario.test_id, diff)


@pytest.mark.parametrize(
    "scenario",
    [item for item in SCENARIOS if item.outcome_kind == "success"],
    ids=[scenario.test_id for scenario in SCENARIOS if scenario.outcome_kind == "success"],
)
def test_golden_master_success_output_contract(
    scenario: GoldenMasterScenario,
    solve_pipeline: MagicSquarePipeline,
) -> None:
    """[TAG][GoldenMaster] verify int[6], 1-index, row-major, combination rules."""
    outcome = solve_pipeline.solve(scenario.grid)
    assert outcome.kind == "success", f"{scenario.test_id}: expected success outcome"
    assert outcome.solution is not None
    assert scenario.expect_small_first is not None
    assert_success_contract(
        scenario.grid,
        outcome.solution,
        expect_small_first=scenario.expect_small_first,
    )


@pytest.mark.parametrize(
    "scenario",
    [item for item in SCENARIOS if item.outcome_kind == "error"],
    ids=[scenario.test_id for scenario in SCENARIOS if scenario.outcome_kind == "error"],
)
def test_golden_master_error_output_contract(
    scenario: GoldenMasterScenario,
    solve_pipeline: MagicSquarePipeline,
) -> None:
    """[TAG][GoldenMaster] verify standard error code contract."""
    outcome = solve_pipeline.solve(scenario.grid)
    assert outcome.kind == "error", f"{scenario.test_id}: expected error outcome"
    assert outcome.error_code is not None
    assert scenario.expected_error_code is not None
    assert_error_contract(outcome.error_code, scenario.expected_error_code)


def test_gm_tc_01_normal_combination_success(solve_pipeline: MagicSquarePipeline) -> None:
    """GM-TC-01 — 정상 조합 성공 (small-first)."""
    scenario = SCENARIOS[0]
    outcome = solve_pipeline.solve(scenario.grid)
    assert outcome.solution == [1, 2, 2, 1, 3, 3]
    actual = capture_scenario(scenario)
    expected = open(DEFAULT_GOLDEN_PATH, encoding="utf-8").read()  # noqa: SIM115
    section_marker = f"[{scenario.name}]"
    assert section_marker in expected
    assert "[1, 2, 2, 1, 3, 3]" in actual


def test_gm_tc_02_reverse_combination_success(solve_pipeline: MagicSquarePipeline) -> None:
    """GM-TC-02 — reverse 조합 성공."""
    scenario = SCENARIOS[1]
    outcome = solve_pipeline.solve(scenario.grid)
    assert outcome.solution == [3, 2, 7, 3, 3, 6]


def test_gm_tc_03_invalid_blank_count(solve_pipeline: MagicSquarePipeline) -> None:
    """GM-TC-03 — INVALID_BLANK_COUNT."""
    scenario = SCENARIOS[2]
    outcome = solve_pipeline.solve(scenario.grid)
    assert outcome.error_code == "INVALID_BLANK_COUNT"


def test_gm_tc_04_duplicate_number(solve_pipeline: MagicSquarePipeline) -> None:
    """GM-TC-04 — DUPLICATE_NON_ZERO_VALUE."""
    scenario = SCENARIOS[3]
    outcome = solve_pipeline.solve(scenario.grid)
    assert outcome.error_code == "DUPLICATE_NON_ZERO_VALUE"


def test_gm_tc_05_no_valid_magic_square(solve_pipeline: MagicSquarePipeline) -> None:
    """GM-TC-05 — NO_VALID_MAGIC_SQUARE (PRD code: NO_VALID_ASSIGNMENT)."""
    scenario = SCENARIOS[4]
    outcome = solve_pipeline.solve(scenario.grid)
    assert outcome.error_code == "NO_VALID_ASSIGNMENT"


def test_golden_master_full_document_matches_baseline() -> None:
    """GM-1 — full golden_master_expected.txt approve comparison."""
    passed, message = approve(path=DEFAULT_GOLDEN_PATH, auto_create=False)
    if not passed:
        _fail_with_diff("GM-FULL", message)


def test_golden_master_baseline_file_exists() -> None:
    """GM-1 — version-controlled baseline must be present."""
    assert DEFAULT_GOLDEN_PATH.is_file(), (
        f"Missing Golden Master baseline: {DEFAULT_GOLDEN_PATH}. "
        "Run `python scripts/generate_golden_master.py` first."
    )
