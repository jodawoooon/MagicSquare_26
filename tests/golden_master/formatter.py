"""Format solve outcomes for Golden Master comparison."""

from control.pipeline import SolveOutcome


def format_grid(grid: list[list[int]]) -> str:
    """Render a 4x4 grid as space-separated rows."""
    return "\n".join(" ".join(str(value) for value in row) for row in grid)


def format_outcome(outcome: SolveOutcome) -> str:
    """Serialize a solve outcome for Golden Master sections."""
    if outcome.kind == "success":
        if outcome.solution is None:
            msg = "success outcome requires solution"
            raise ValueError(msg)
        rendered = ", ".join(str(value) for value in outcome.solution)
        return f"[{rendered}]"

    if outcome.error_code is None:
        msg = "error outcome requires error_code"
        raise ValueError(msg)
    return f"Error:\n{outcome.error_code}"


def format_scenario_section(name: str, grid: list[list[int]], outcome: SolveOutcome) -> str:
    """Render one Golden Master scenario block."""
    lines = [f"[{name}]", "Input:", format_grid(grid)]
    if outcome.kind == "success":
        lines.extend(["Output:", format_outcome(outcome)])
    else:
        lines.append(format_outcome(outcome))
    return "\n".join(lines)
