"""Capture current solver output for Golden Master scenarios."""

from control.pipeline import MagicSquarePipeline, SolveOutcome

from tests.golden_master.formatter import format_scenario_section
from tests.golden_master.scenarios import SCENARIOS, GoldenMasterScenario


def capture_scenario(
    scenario: GoldenMasterScenario,
    pipeline: MagicSquarePipeline | None = None,
) -> str:
    """Run one scenario and return its Golden Master text block."""
    runner = pipeline or MagicSquarePipeline()
    outcome = runner.solve(scenario.grid)
    return format_scenario_section(scenario.name, scenario.grid, outcome)


def capture_all(pipeline: MagicSquarePipeline | None = None) -> str:
    """Capture all Golden Master scenarios as one document."""
    blocks = [capture_scenario(scenario, pipeline=pipeline) for scenario in SCENARIOS]
    return "\n\n________________________________________\n\n".join(blocks) + "\n"
