import pytest
from twitter.error import TwitterError

from auto_tweet import AutoTweet
from auto_tweet.utils import (
    get_time,
    tweet_template,
    parse_or_get,
    parse_time,
    DELAY_DICT,
    INTERVAL_DICT,
)
from auto_tweet.exceptions import (
    NoneError,
    TweetTypeError,
    TemplateError,
    ScheduleError,
)

at = AutoTweet("mock", "mock", "mock", "mock", preview=True)
atc = AutoTweet("mock", "mock", "mock", "mock")
sigle_list_update = ["update"]
test_updates = ["first", "second", "third"]
test_template = """$message"""
test_template2 = """$message"""
test_custom_posts = [
    (5, None, "4rt print."),
    ("now", None, "1st print."),
    (8, None, "5ve print."),
    ("half_hour", None, "2nd print."),
    (0, None, "1st last print"),
    (3, test_template2, "3rd print."),
    ("next_week", test_template, "Last print."),
]


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
        ("next_week", 10),  # 604800
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
def test_tweet(msgs, delay, interval):
    # This test pass as long as no error is raised
    at.tweet(msgs, delay, interval)


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
def test_tweet_and_templates(msgs, delay, interval):
    # This test pass as long as no error is raised
    at.tweet(msgs, delay, interval, template=test_template)


def test_tweet_TwitterError():
    # Test that TwitterError is raised for wrong credentials
    with pytest.raises(TwitterError):
        atc.tweet(test_updates)


def test_tweet_interval_NoneError():
    # Tests that a NoneError is raised when the interval arg
    # is a str that is not in the INTERVAL_DICT.
    with pytest.raises(NoneError):
        at.tweet(test_updates, interval="wrong_interval_time")


@pytest.mark.parametrize(
    "msg", [({"mock": "mock"}), ([{"mock", "mocks"}]), ([123, 123, 123])]
)
def test_tweet_msg_TweetTypeError(msg):
    # Tests that a TweetTypeError error is raised when
    # 'msg' arg is not a list or str.
    with pytest.raises(TweetTypeError):
        at.tweet(msg)


def test_utils_tweet_template():
    # Directly test the template module from utils.py.
    template = tweet_template(msg="update", template=test_template)
    assert isinstance(template, str)


@pytest.mark.parametrize("msg", [(sigle_list_update), (test_updates)])
def test_at_tweet_template(msg):
    # This test pass as long as no error is raised.
    at.tweet(msg, template=test_template)


@pytest.mark.parametrize(
    "msg, template", [(sigle_list_update, list), (test_updates, dict)]
)
def test_template_TemplateError(msg, template):
    # Tests that a TemplateError error is raised when
    # 'template' arg is not a str.
    with pytest.raises(TemplateError):
        at.tweet(msg, template=template)


def test_custom_tweets():
    # This test pass as long as no error is raised.
    at.schedule(test_custom_posts)


@pytest.mark.parametrize(
    "schedule_time, time_zone",
    [
        ("2040-10-28 18:46", "America/Santiago"),
        ("2040-10-28", "America/Santiago"),
        ("2040-10-28 18:46", "local"),
        ("2040-10-28", "local"),
    ],
)
def test_parse_or_get(schedule_time, time_zone):
    time = parse_or_get(schedule_time, time_zone)
    assert isinstance(time, int)


@pytest.mark.parametrize(
    "schedule_time, time_zone",
    [("wrong_delay_time", "local"), ("wrong_delay_time", None)],
)
def test_parse_or_get_TypeError(schedule_time, time_zone):
    with pytest.raises(TypeError):
        parse_or_get(schedule_time, time_zone)


@pytest.mark.parametrize(
    "schedule_time, time_zone",
    [
        ("2040-10-28 18:46", "America/Santiago"),
        ("2040-10-28", "America/Santiago"),
        ("2040-10-28 18:46", "local"),
        ("2040-10-28", "local"),
    ],
)
def test_parse_time(schedule_time, time_zone):
    secs = parse_time(schedule_time, time_zone)
    assert isinstance(secs, int)


@pytest.mark.parametrize(
    "schedule_time, time_zone",
    [
        ("2015-10-28 18:46", "America/Santiago"),
        ("2002-10-28", "America/Santiago"),
        ("1995-10-28 18:46", "local"),
        ("1984-10-28", "local"),
    ],
)
def test_parse_time_ScheduleError(schedule_time, time_zone):
    with pytest.raises(ScheduleError):
        parse_time(schedule_time, time_zone)


@pytest.mark.parametrize(
    "tweets", [(["mock"]), ([{"mock": "mock"}]), ([{"mock"}]), ([123]), (["mock"])]
)
def test_schedule_ScheduleError(tweets):
    with pytest.raises(ScheduleError):
        at.schedule(tweets)


@pytest.mark.parametrize(
    "tweets",
    [
        (("2040-10-28 18:46")),
        (("2040-10-28 18:46", "mock")),
        (("2040-10-28 18:46", "mock", "mock", "mock")),
    ],
)
def test_schedule_tupleLen_ScheduleError(tweets):
    with pytest.raises(ScheduleError):
        at.schedule(tweets)
