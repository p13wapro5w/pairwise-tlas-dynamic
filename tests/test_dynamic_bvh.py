import pytest
from render import dynamic_bvh as mod

CASES = [
    ("union", 'm.bounds_union((0, 0, 0, 1, 1, 1), (2, 2, 2, 3, 3, 3)) == (0, 0, 0, 3, 3, 3)'),
    ("leaf", 'm.node_is_leaf(4, 4) is True'),
    ("refit", 'm.refit_threshold(0.5, 1000) == "rebuild"'),
    ("ancestors", 'm.update_ancestors([5, 3, 5, 1]) == [1, 3, 5]'),
    ("mask", 'm.instance_mask(0b1011, 0b0110) == 0b0010'),
    ("stack", 'm.traversal_stack_limit(5, 8) == 40'),
    ("reclaim", 'm.node_pool_reclaim(10, 4) == 6'),
    ("buffer", 'm.blas_double_buffer("a", "b") == ("b", "a")'),
    ("fence", 'm.fence_required("compute", "render") is True'),
    ("align", 'm.frame_align(7, 7) is True'),
    ("key", 'm.instance_key(3, 8) == "3:8"'),
    ("capacity", 'm.leaf_capacity(10, 4) == 3'),
    ("overlap", 'm.box_overlap((0, 0, 0, 2, 2, 2), (1, 1, 1, 3, 3, 3)) is True'),
    ("root", 'm.refit_root([(0, 0, 0, 1, 1, 1), (2, 2, 2, 3, 3, 3)]) == (0, 0, 0, 3, 3, 3)'),
    ("rebuild", 'm.tlas_rebuild_needed(0, 0, 0) is False')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
