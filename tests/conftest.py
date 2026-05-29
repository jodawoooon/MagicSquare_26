"""Shared grid fixtures (G0~G3) — RED skeleton placeholders.

SSOT: Report/06 §5 (G0~G3). G2/G3 values fixed in entity conftest when used.
"""

# G0 — complete magic square (D-VAL-01)
# GRID_G0 = [
#     [16, 3, 2, 13],
#     [5, 10, 11, 8],
#     [9, 6, 7, 12],
#     [4, 15, 14, 1],
# ]

# G1 — small-first success; blanks (2,2), (3,3); missing {7, 10}
# GRID_G1 = [
#     [16, 2, 3, 13],
#     [5, 0, 6, 8],
#     [9, 11, 0, 12],
#     [4, 14, 15, 1],
# ]

# G2 — Step A fail, Step B success (PRD §16.4 reverse)
# GRID_G2 = [
#     [16, 2, 3, 13],
#     [5, 11, 10, 8],
#     [9, 0, 0, 12],
#     [4, 14, 15, 1],
# ]

# G3 — unsolvable partial grid (TBD before GREEN)
# GRID_G3 = None  # placeholder — confirm before D-SOL-03 GREEN
