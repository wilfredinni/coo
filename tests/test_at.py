import pytest

from twitter.error import TwitterError

from auto_tweet import AutoTweet
from auto_tweet.time_managment import get_time, DELAY_DICT, INTERVAL_DICT
from auto_tweet.exceptions import NoneError

at = AutoTweet("mock", "mock", "mock", "mock")


def test_auto_tweet_verify():
    # Test that the wrong credentials raises a TwitterError
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
def test_get_time_DELAY_DICT(t_str, t_int):
    # Test get_time() to assert the int values
    # of the 'DELAY_STR' dictionary.
    assert get_time(t_str, DELAY_DICT) == t_int


@pytest.mark.parametrize(
    "t_str, t_int",
    [
        ("once_a_day", 2),  # 86400
        ("twice_perday", 4),  # 43200
        ("three_times_day", 6),  # 28800
    ],
)
def test_get_time_INTERVAL_DICT(t_str, t_int):
    # Test get_time() to assert the int values
    # of the 'INTERVAL_DICT' dictionary.
    assert get_time(t_str, INTERVAL_DICT) == t_int


def test_get_time_NoneError_DELAY_DICT():
    # Directly check that the 'NoneError' is raised.
    with pytest.raises(NoneError):
        get_time("wrong_delay_time", DELAY_DICT)


def test_get_time_NoneError_INTERVAL_DICT():
    # Directly check that the 'NoneError' is raised.
    with pytest.raises(NoneError):
        get_time("wrong_delay_time", INTERVAL_DICT)


@pytest.mark.parametrize(
    "msg, delay",
    [("My Twitter Msg", None), ("My Twitter Msg", 1), ("My Twitter Msg", "half_hour")],
)
def test_tweet(msg, delay):
    # Assert correct tweet updates.
    assert isinstance(at.tweet(msg, delay), str)


def test_tweet_delay_NoneError():
    # Check the that the 'NoneError' is raised when a wrong
    # 'delay' argument is provided.
    with pytest.raises(NoneError):
        at.tweet("mock_msg", "wrong_delay_time")
