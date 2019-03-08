import pytest

from coo._utils import parse_time, parse_or_get, zzz, tweet_template, TIME_DICT
from coo._exceptions import ScheduleError, TemplateError


# DICTIONARIES
@pytest.mark.parametrize(
    "time_delay, int_value",
    [
        ("now", 0),
        ("half_hour", 1800),
        ("one_hour", 3600),
        ("two_hours", 7200),
        ("four_hours", 14400),
        ("six_hours", 21600),
        ("eight_hours", 28800),
        ("ten_hours", 36000),
        ("twelve_hours", 43200),
        ("fourteen_hours", 50400),
        ("sixteen_hours", 57600),
        ("eighteen_hours", 64800),
        ("twenty_hours", 72000),
        ("twenty_two_hours", 79200),
        ("one_day", 86400),
        ("two_days", 172800),
        ("three_days", 259200),
        ("four_days", 345600),
        ("five_days", 432000),
        ("six_days", 518400),
        ("one_week", 604800),
    ],
)
def test_TIME_DICT(time_delay, int_value):
    assert TIME_DICT.get(time_delay) == int_value


# PARSE TIME
@pytest.mark.parametrize(
    "date_time, time_zone",
    [("2040-10-28 18:46", "America/Santiago"), ("2040-10-28", "America/Santiago")],
)
def test_parse_time(date_time, time_zone):
    secs = parse_time(date_time, time_zone)
    assert isinstance(secs, int)


@pytest.mark.parametrize(
    "schedule_time, time_zone",
    [("2015-10-28 18:46", "America/Santiago"), ("2002-10-28", "America/Santiago")],
)
def test_parse_time_ScheduleError(schedule_time, time_zone):
    with pytest.raises(ScheduleError):
        parse_time(schedule_time, time_zone)


# PARSE OR GET
@pytest.mark.parametrize(
    "schedule_time, time_zone",
    [
        (20, None),
        ("now", None),
        ("2040-10-28", "America/Santiago"),
        ("2040-10-28 18:46", "America/Santiago"),
    ],
)
def test_parse_or_get(schedule_time, time_zone):
    seconds = parse_or_get(schedule_time, time_zone)
    assert isinstance(seconds, int)


@pytest.mark.parametrize(
    "schedule_time, time_zone",
    [
        ("wrong_delay_time", "America/Santiago"),
        ("wrong_delay_time", "America/Santiago"),
    ],
)
def test_parse_or_get_TypeError(schedule_time, time_zone):
    with pytest.raises(TypeError):
        parse_or_get(schedule_time, time_zone)


# ZZZ
@pytest.mark.parametrize("sleep_time, time_zone", [(0, None), ("now", None)])
def test_zzz_INT(sleep_time, time_zone):
    zzz(sleep_time, time_zone)


# TEMPLATE
def test_tweet_template():
    assert isinstance(tweet_template("msg", "$message"), str)


@pytest.mark.parametrize(
    "update, template",
    [
        ("msg", None),
        ("msg", (1, 2, 3)),
        ("msg", [1, 2, 3]),
        ("msg", {1, 2, 3}),
        ("msg", {1: 2}),
    ],
)
def test_tweet_template_TemplateError(update, template):
    with pytest.raises(TemplateError):
        tweet_template(update, template)


def test_message_template_TemplateError():
    with pytest.raises(TemplateError):
        tweet_template("update", "template")
