"""Entity Track B grid fixtures — RED skeleton placeholders.

SSOT: Report/06 §5. Import from tests.conftest when GREEN wires fixtures.
"""

# G0 — complete magic square
# @pytest.fixture
# def grid_g0() -> list[list[int]]:
#     return [
#         [16, 3, 2, 13],
#         [5, 10, 11, 8],
#         [9, 6, 7, 12],
#         [4, 15, 14, 1],
#     ]

# G1 — partial; blanks (2,2), (3,3) 1-index; missing 7, 10
# @pytest.fixture
# def grid_g1() -> list[list[int]]:
#     return [
#         [16, 2, 3, 13],
#         [5, 0, 6, 8],
#         [9, 11, 0, 12],
#         [4, 14, 15, 1],
#     ]

# G2 — reverse-order success path (D-SOL-02)
# @pytest.fixture
# def grid_g2() -> list[list[int]]:
#     return [
#         [16, 2, 3, 13],
#         [5, 11, 10, 8],
#         [9, 0, 0, 12],
#         [4, 14, 15, 1],
#     ]

# G3 — unsolvable (placeholder)
# @pytest.fixture
# def grid_g3() -> list[list[int]]:
#     raise NotImplementedError("G3 TBD")
