import itertools

import pytest as pytest

from main import digit_factorials

def tri_words(word_list: list) ->int:
    triangles = [int((x*.5)*(x+1)) for x in itertools.takewhile(lambda x: (x*.5)*(x+1) < 2600, itertools.count())]
    letter_value = {}
    for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        letter_value[letter] = i+1
    return sum(1 for word in word_list if sum(map(lambda a: letter_value[a], word)) in triangles)

@pytest.mark.benchmark(
    min_rounds=2
)
def test_factorials(benchmark):
    result = benchmark(digit_factorials)
    assert result is not None
