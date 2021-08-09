import pytest as pytest

from main import digit_factorials

@pytest.mark.benchmark(
    min_rounds=2
)
def test_factorials(benchmark):
    result = benchmark(digit_factorials)
    assert result is not None
