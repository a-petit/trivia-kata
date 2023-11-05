import random
import sys
from io import StringIO

from trivia import play_game
from trivia_reference import play_game_reference


def test_golden_master():
    for i in range(1000):
        seed = i * 100
        random.seed(seed)
        output = StringIO()
        sys.stdout = output
        play_game()

        random.seed(seed)
        reference = StringIO()
        sys.stdout = reference
        play_game_reference()

        assert output.getvalue() == reference.getvalue()

