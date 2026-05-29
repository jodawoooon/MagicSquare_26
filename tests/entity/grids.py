"""Report/06 §5 grid SSOT for Entity Track B tests."""

from typing import Final

GRID_G0: Final[list[list[int]]] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# Report/06 G1 — D-LOC-01, D-MIS-01, U-IN-08 (빈칸 (2,2)·(3,3), 누락 {7,10})
GRID_G1: Final[list[list[int]]] = [
    [16, 2, 3, 13],
    [5, 0, 6, 8],
    [9, 11, 0, 12],
    [4, 14, 15, 1],
]

# GM-TC-01 / small-first solvable — D-SOL-01, D-SOL-04 (Golden Master SSOT)
GRID_G1_SOL: Final[list[list[int]]] = [
    [16, 0, 0, 13],
    [5, 11, 10, 8],
    [9, 7, 6, 12],
    [4, 14, 15, 1],
]

# GM-TC-02 / reverse fallback — D-SOL-02 (Report/06 G2)
GRID_G2: Final[list[list[int]]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 0, 0, 12],
    [4, 14, 15, 1],
]

# GM-TC-05 / unsolvable — D-SOL-03, U-OUT-03 (양 조합 실패)
GRID_G3: Final[list[list[int]]] = [
    [16, 2, 3, 13],
    [5, 0, 6, 8],
    [9, 11, 0, 12],
    [4, 14, 15, 1],
]

D_SOL_01_EXPECTED: Final[list[int]] = [1, 2, 2, 1, 3, 3]
D_SOL_02_EXPECTED: Final[list[int]] = [3, 2, 7, 3, 3, 6]
