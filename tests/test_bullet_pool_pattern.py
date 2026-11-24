import pytest
import gameplay.bullet_pool_pattern as mod

CASES = [
    ("pool_reset", (1,)),
    ("delayed_release", (1,)),
    ("seq_sort", (1,)),
    ("preview_clock", (1,)),
    ("pause_freeze", (1,)),
    ("grow_swap", (1,)),
    ("determinism", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("spawn", (1,)),
    ("metrics", (1,)),
    ("collide", (1,)),
    ("recycle", (1,)),
    ("replay", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
