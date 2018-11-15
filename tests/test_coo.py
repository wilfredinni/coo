import pytest
from twitter.error import TwitterError

from coo import Coo
from coo.exceptions import TweetTypeError, ScheduleError


# Coo instances
at_preview = Coo("mock", "mock", "mock", "mock", preview=True)
atc = Coo("mock", "mock", "mock", "mock")

# Mock Update list
m_updates = ["mock", "mock", "mock", "mock", "mock"]


# API
def test_wrong_credentials_TwitterError():
    with pytest.raises(TwitterError):
        atc.verify


# TWEET
@pytest.mark.parametrize(
    "updates, delay, interval, template, time_zone",
    [
        (m_updates, None, None, None, None),
        # One None
        (m_updates, None, "now", "template", "local"),
        (m_updates, "now", None, "template", "local"),
        (m_updates, "now", "now", None, "local"),
        (m_updates, "now", "now", "template", None),
        # Two None
        (m_updates, None, None, "template", "local"),
        (m_updates, "now", None, None, "local"),
        (m_updates, "now", "now", None, None),
        (m_updates, None, "now", "template", None),
        # Delay
        (m_updates, "now", None, None, None),
        (m_updates, 0, None, None, None),
        # Interval
        (m_updates, None, "now", None, None),
        (m_updates, None, 0, None, None),
        # Template
        (m_updates, None, None, "template", None),
        # Time zone
        (m_updates, None, None, None, "local"),
        (m_updates, None, None, None, "America/Santiago "),
    ],
)
def test_tweet(updates, delay, interval, template, time_zone):
    at_preview.tweet(updates, delay, interval, template, time_zone)


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
def test_tweet_TweetTypeError(updates):
    with pytest.raises(TweetTypeError):
        at_preview.tweet(updates)


# SCHEDULE
@pytest.mark.parametrize(
    "updates",
    [
        (
            [
                ("now", "template", "update"),
                (0, "template", "update"),
                ("now", None, "update"),
                (0, None, "update"),
            ]
        )
    ],
)
def test_schedule(updates):
    at_preview.schedule(updates)


@pytest.mark.parametrize(
    "updates",
    [
        ([["update1", "update2"]]),
        ([{"update1", "update2"}]),
        (["update1", "update2"]),
        ([123, 456, 789]),
    ],
)
def test_schedule_ScheduleError(updates):
    with pytest.raises(ScheduleError):
        at_preview.schedule(updates)


# STR UPDATE
@pytest.mark.parametrize(
    "update, template",
    [("My Twitter Update", None), ("My Twitter Update", "myTemplate")],
)
def test_str_update(update, template):
    at_preview.str_update(update, template)


# DELAY
@pytest.mark.parametrize("delay, time_zone", [(0, "local"), ("now", "local")])
def test_delay(delay, time_zone):
    # TODO: test the delay using datetime strings.
    at_preview.delay(delay, time_zone)


# INTERVAL
@pytest.mark.parametrize("interval", [(0), ("now")])
def test_interval(interval):
    at_preview.interval(interval)
