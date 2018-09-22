# from auto_tweet import AutoTweet
import pytest
from auto_tweet import delay_time_int, DELAY_STR


@pytest.mark.parametrize(
    "t_str, t_int",
    [
        ("half_hour", 2),  # 1800
        ("one_hour", 4),  # 3600
        ("tomorrow", 6),  # 86400
        ("next_week", 8),  # 604800
    ],
)
def test_delay_tweet(t_str, t_int):
    assert delay_time_int(t_str, DELAY_STR) == t_int
