import pytest

from auto_tweet import AutoTweet
from auto_tweet.time_managment import delay_time_int, DELAY_STR

# TODO: test delay_time_int to assert 'NoneError'


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


@pytest.mark.parametrize(
    "msg, delay",
    [("My Twitter Msg", None), ("My Twitter Msg", 1), ("My Twitter Msg", "half_hour")],
)
def test_tweet(msg, delay):
    at = AutoTweet("mock", "mock", "mock", "mock")
    assert isinstance(at.tweet(msg, delay), str)
