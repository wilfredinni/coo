import pytest
from twitter.error import TwitterError

from coo import Coo
from coo.exceptions import TweetTypeError, ScheduleError


# Mock Update list
m_updates = ["mock1", "mock2", "mock3", "mock4", "mock5"]


@pytest.fixture
def coo_preview_instance():
    return Coo("mock", "mock", "mock", "mock", preview=True)


@pytest.fixture
def coo_mock_instance():
    return Coo("mock", "mock", "mock", "mock")


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
        # Delay
        (m_updates, "now", None, None, None),
        (m_updates, 0, None, None, None),
        # Interval
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


def test_tweet_random():
    # TODO: test aleatory=True (coo.tweet)
    pass


def test_tweet_media_update():
    # TODO: test tweet media updates
    pass


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
def test_schedule(coo_preview_instance, updates):
    coo_preview_instance.schedule(updates)


@pytest.mark.parametrize(
    "updates",
    [
        ([["update1", "update2"]]),
        ([{"update1", "update2"}]),
        (["update1", "update2"]),
        ([123, 456, 789]),
    ],
)
def test_schedule_ScheduleError(coo_preview_instance, updates):
    with pytest.raises(ScheduleError):
        coo_preview_instance.schedule(updates)


def test_schedule_len_tuple_ScheduleError():
    # TODO: write a test for ScheduleError for the wrong len(tuple).
    pass


def test_schedule_global_media_update():
    # TODO: test schedule global media updates
    pass


def test_schedule_single_media_update():
    # TODO: test schedule single media updates
    pass


# STR UPDATE
@pytest.mark.parametrize(
    "update, template", [("My Twitter Update", None), ("My Twitter Update", "$message")]
)
def test_str_update(coo_preview_instance, update, template):
    coo_preview_instance.str_update(update, template)


def test_str_update_media():
    # TODO: test string update with media file
    pass


# DELAY
@pytest.mark.parametrize("delay", [(0), ("now")])
def test_delay(coo_preview_instance, delay):
    # TODO: test the delay using datetime strings.
    coo_preview_instance.delay(delay)


# INTERVAL
@pytest.mark.parametrize("interval", [(0), ("now")])
def test_interval(coo_preview_instance, interval):
    coo_preview_instance.interval(interval)
