from pathlib import Path

import pytest
from twitter.error import TwitterError

from coo import Coo
from coo._exceptions import TweetTypeError, ScheduleError


# Mock Update list
m_updates = ["mock1", "mock2", "mock3", "mock4", "mock5"]


def test_input_types():
    with pytest.raises(TypeError):
        Coo([1], [1], [1], [1])

    with pytest.raises(TypeError):
        Coo({1: 5}, {1: 5}, {1: 5}, {1: 5})

    with pytest.raises(TypeError):
        Coo(1, 2, 3, 4)

    # correct construction. no error
    Coo("mock", "mock", "mock", "mock")


@pytest.fixture
def coo_preview_instance():
    yield Coo("mock", "mock", "mock", "mock", preview=True)


@pytest.fixture
def coo_mock_instance():
    yield Coo("mock1", "mock2", "mock3", "mock4")


# API
def test_wrong_credentials_TwitterError(coo_mock_instance):
    with pytest.raises(TwitterError):
        coo_mock_instance.verify


# TWEET
@pytest.mark.parametrize(
    "updates, delay, interval, template, time_zone",
    [
        (m_updates, None, None, None, None),
        # One None
        (m_updates, None, "now", "$message", "local"),
        (m_updates, "now", None, "$message", "local"),
        (m_updates, "now", "now", None, "local"),
        (m_updates, "now", "now", "$message", None),
        # Two None
        (m_updates, None, None, "$message", "local"),
        (m_updates, "now", None, None, "local"),
        (m_updates, "now", "now", None, None),
        (m_updates, None, "now", "$message", None),
        # _delay
        (m_updates, "now", None, None, None),
        (m_updates, 0, None, None, None),
        # _interval
        (m_updates, None, "now", None, None),
        (m_updates, None, 0, None, None),
        # Template
        (m_updates, None, None, "$message", None),
        # Time zone
        (m_updates, None, None, None, "local"),
        (m_updates, None, None, None, "America/Santiago "),
    ],
)
def test_tweet(coo_preview_instance, updates, delay, interval, template, time_zone):
    coo_preview_instance.tweet(updates, delay, interval, template, time_zone)


@pytest.mark.parametrize(
    "tz",
    [
        ("Canada/Yukon"),
        ("Brazil/Acre"),
        ("Australia/Tasmania"),
        ("America/Santiago"),
        ("America/Detroit"),
        ("Asia/Atyrau"),
    ],
)
def test_tweet_time_zone(coo_preview_instance, tz):
    coo_preview_instance.tweet(["mock"], time_zone=tz)
    assert coo_preview_instance.time_zone == tz


def test_tweet_random(coo_preview_instance):
    updates = ["mock1", "mock2", "mock3", "mock4", "mock5"]
    coo_preview_instance.tweet(m_updates, aleatory=True)
    assert updates != m_updates


def test_tweet_media_update(coo_preview_instance):
    coo_preview_instance.tweet(["mock"], media="../coo.png")
    assert coo_preview_instance.media == Path("../coo.png")


@pytest.mark.parametrize(
    "updates",
    [
        # update is not a instance of list:
        ((1, 2, 3)),
        ({1, 2, 3}),
        (123),
        ("string"),
        # The instances 'in' the list are no strings:
        ([(1, 2, 3)]),
        ([{1, 2, 3}]),
        ([[1, 2, 3]]),
        ([1, 2, 3]),
    ],
)
def test_tweet_TweetTypeError(coo_preview_instance, updates):
    with pytest.raises(TweetTypeError):
        coo_preview_instance.tweet(updates)


def test_tweet_media_FileNotFoundError(coo_mock_instance):
    with pytest.raises(FileNotFoundError):
        coo_mock_instance.tweet(["mock"], media="coo_.png")


def test_tweet_media_TwitterError(coo_mock_instance):
    with pytest.raises(TwitterError):
        coo_mock_instance.tweet(["mock"], media="coo.png")


def test_tweet_none_media_TwitterError(coo_mock_instance):
    with pytest.raises(TwitterError):
        coo_mock_instance.tweet(["mock"], media=None)


# SCHEDULE
def test_schedule_time_zone_media(coo_preview_instance):
    updates = [
        ("now", "template", "update"),
        (0, "template", "update"),
        ("now", None, "update"),
        (0, None, "update"),
        (0, None, "update", "../coo.png"),
    ]
    coo_preview_instance.schedule(updates, time_zone="Canada/Yukon", media="../coo.png")
    assert coo_preview_instance.time_zone == "Canada/Yukon"
    assert coo_preview_instance.media == Path("../coo.png")
    assert coo_preview_instance.global_media == Path("../coo.png")


@pytest.mark.parametrize(
    "updates",
    [
        ([["update1", "update2"]]),
        ([{"update1", "update2"}]),
        (["update1", "update2"]),
        ([123, 456, 789]),
        # len tuple
        ([("now")]),
    ],
)
def test_schedule_ScheduleError(coo_preview_instance, updates):
    with pytest.raises(ScheduleError):
        coo_preview_instance.schedule(updates)


# STR UPDATE
@pytest.mark.parametrize(
    "update, template", [("My Twitter Update", None), ("My Twitter Update", "$message")]
)
def test__str_update(coo_preview_instance, update, template):
    coo_preview_instance._str_update(update, template)


# _delay
@pytest.mark.parametrize("delay", [(0), ("now")])
def test_delay(coo_preview_instance, delay):
    coo_preview_instance._delay(delay)


# _interval
@pytest.mark.parametrize("_interval", [(0), ("now")])
def test__interval(coo_preview_instance, _interval):
    coo_preview_instance._interval(_interval)
