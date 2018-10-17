import pytest
from twitter.error import TwitterError

from auto_tweet import AutoTweet
from auto_tweet.utils import get_time, tweet_template, DELAY_DICT, INTERVAL_DICT
from auto_tweet.exceptions import NoneError, TweetTypeError

at = AutoTweet("mock", "mock", "mock", "mock", debug=True)
atc = AutoTweet("mock", "mock", "mock", "mock")
sigle_list_update = ["update"]
test_updates = ["first", "second", "third"]
test_template = """$message

#test #python #AutoTweet"""


def test_tweet_delay_NoneError():
    # Check the that the 'NoneError' is raised when a wrong
    # 'delay' argument is provided.
    with pytest.raises(NoneError):
        at.tweet("mock_msg", "wrong_delay_time")


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


def test_tweet_TwitterError():
    # Test that TwitterError is raised for wrong credentials
    with pytest.raises(TwitterError):
        atc.tweet("My Twitter Update")


@pytest.mark.parametrize(
    "msgs, delay, interval",
    [
        (test_updates, None, None),
        (test_updates, None, 0.1),
        (test_updates, 0.1, None),
        (test_updates, 0.1, 0.1),
        (test_updates, "test", "test"),
        (test_updates, 0.1, "test"),
        (test_updates, "test", 0.1),
    ],
)
def test_tweets(msgs, delay, interval):
    # This test pass as long as no error is raised
    at.tweet(msgs, delay, interval)


def test_tweets_TwitterError():
    # Test that TwitterError is raised for wrong credentials
    with pytest.raises(TwitterError):
        atc.tweet(test_updates)


def test_tweets_interval_NoneError():
    # Tests that a NoneError is raised when the interval arg
    # is a str that is not in the INTERVAL_DICT.
    with pytest.raises(NoneError):
        at.tweet(test_updates, interval="wrong_interval_time")


def test_tweets_msgs_TweetTypeError():
    # Tests that a TweetTypeError error is raised when
    # 'msg' arg is not a list or str.
    with pytest.raises(TweetTypeError):
        at.tweet({"test": "test"})


def test_utils_tweet_template():
    # Directly test the template module from utils.py.
    template = tweet_template(msg="update", template=test_template)
    assert isinstance(template, str)


@pytest.mark.parametrize("msg", [("update"), (sigle_list_update), (test_updates)])
def test_at_tweet_template(msg):
    # This test pass as long as no error is raised
    at.tweet(msg, template=test_template)
