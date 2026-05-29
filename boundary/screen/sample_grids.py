"""Sample grids for GUI demonstration (SSOT: Report/06 §5)."""

from typing import Final

GRID_SIZE: Final[int] = 4

GRID_G0: Final[list[list[int]]] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

GRID_G1: Final[list[list[int]]] = [
    [16, 2, 3, 13],
    [5, 0, 6, 8],
    [9, 11, 0, 12],
    [4, 14, 15, 1],
]

GRID_G2: Final[list[list[int]]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 0, 0, 12],
    [4, 14, 15, 1],
]

GRID_EMPTY: Final[list[list[int]]] = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

SAMPLE_GRIDS: Final[dict[str, list[list[int]]]] = {
    "G0 — 완성 마방진": GRID_G0,
    "G1 — small-first": GRID_G1,
    "G2 — reverse-order": GRID_G2,
    "빈 격자 (4×4)": GRID_EMPTY,
}
