import pytest

from twitter.error import TwitterError

from auto_tweet import AutoTweet
from auto_tweet.time_managment import delay_time_int, DELAY_STR
from auto_tweet.exceptions import NoneError


def test_auto_tweet_verify():
    # Test that the wrong credentials raises a TwitterError
    at = AutoTweet("mock", "mock", "mock", "mock")
    with pytest.raises(TwitterError):
        at.verify


@pytest.mark.parametrize(
    "t_str, t_int",
    [
        ("half_hour", 2),  # 1800
        ("one_hour", 4),  # 3600
        ("tomorrow", 6),  # 86400
        ("next_week", 8),  # 604800
    ],
)
def test_delay_time_int(t_str, t_int):
    # Test delay_time_int() to assert the int values
    # of the 'DELAY_STR' dictionary.
    assert delay_time_int(t_str, DELAY_STR) == t_int


def test_delay_time_int_NoneError():
    # Directly check the that the 'NoneError' is raised.
    with pytest.raises(NoneError):
        delay_time_int("wrong_delay_time", DELAY_STR)


@pytest.mark.parametrize(
    "msg, delay",
    [("My Twitter Msg", None), ("My Twitter Msg", 1), ("My Twitter Msg", "half_hour")],
)
def test_tweet(msg, delay):
    # Assert correct tweets updates.
    at = AutoTweet("mock", "mock", "mock", "mock")
    assert isinstance(at.tweet(msg, delay), str)


def test_tweet_delay_NoneError():
    # Check the that the 'NoneError' is raised when a wrong
    # 'delay' argument is provided.
    at = AutoTweet("mock", "mock", "mock", "mock")
    with pytest.raises(NoneError):
        at.tweet("mock_msg", "wrong_delay_time")
