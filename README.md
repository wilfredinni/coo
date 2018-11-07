# AutoTweet: Schedule Twitter Updates with Easy

[![Build Status](https://travis-ci.org/wilfredinni/auto-tweet.svg?branch=master)](https://travis-ci.org/wilfredinni/auto-tweet)
[![codecov](https://codecov.io/gh/wilfredinni/auto-tweet/branch/master/graph/badge.svg)](https://codecov.io/gh/wilfredinni/auto-tweet)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Usage

To use AutoTweet you need to first apply for a developer account in the [Twitter Developers Platform](https://developer.twitter.com/) and generate the Keys and Access Tokens.

**Installing**

```shell
pip install AutoTweet
```

**Initializing**

```python
from auto_tweet import AutoTweet

at = AutoTweet(
    "consumer_key",
    "consumer_secret",
    "access_token",
    "access_token_secret"
)
```

Alternatively, you can set `preview=True` and print your tweets in the terminal instead to post them on Twitter.

### Scheduling Twitter Updates

Schedule updates with `datetime` strings or integers and [custom templates](#Templates) if needed.

```python
AutoTweet.schedule(updates, time_zone)
```

#### Notes for parsing DateTime strings

- If a time zone is not specified, it will set to `local`.
- The time will be set to 00:00:00 if it's not specified.
- When passing only time information the date will default to today.
- A future date is needed, otherwise a `ScheduleError` is raised.

More [Time Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

#### datetime strings

```python
from auto_tweet import AutoTweet

at = AutoTweet(
    "consumer_key",
    "consumer_secret",
    "access_token",
    "access_token_secret"
)

tweets = [
    # datetime with and without templates
    ("2030-10-28 18:50", template, "My Twitter update with a template."),
    ("2030-10-29 18:15", template2, "Update with a different template."),
    ("2030-11-01 13:45", None, "Awesome Twitter update without a template."),
]

at.schedule(tweets, time_zone="America/Santiago")
```

#### date strings

```python
tweets = [
    # date with and without templates
    ("2030-12-25", template3, "Merry christmas!"),
    ("2031-01-01", None, "And a happy new year!"),
]

at.schedule(tweets, time_zone="Australia/Sydney")
```

#### time strings

```python
tweets = [
    # time with and without templates
    ("18:46", template2, "Will be post today at 18:46."),
    ("23:00", None, "A tweet for today at 23:00."),
]

at.schedule(tweets, time_zone="America/Santiago")
```

#### integers

```python
tweets = [
    # integer (seconds) with and without templates
    (3600, template, "This tweet will be posted in an hour."),
    (86400, None, "This one, tomorrow at the same hour."),
]

at.schedule(tweets, time_zone="America/New_York")
```

### Tweet an ordered list of strings

Post ordered updates with `delay`, `interval`, and [templates](#Templates) if needed.

```python
AutoTweet.tweet(updates, delay, interval, template, time_zone)
```

```python
tweets = [
    "My first awesome Twitter Update",
    "My second awesome Twitter Update",
    "My third awesome Twitter Update",
    "My fourth awesome Twitter Update",
    "My fifth awesome Twitter Update",
    "My sixth awesome Twitter Update",
]

# post the twitter updates
at.tweet(tweets)
```

#### Post Twitter Updates with a delay

You can use `datetime`, `date` and `time` strings, integers as seconds and some strings as keywords: `half_hour`, `one_hour`, `tomorrow`, `next_week`.

```python
# datetime, date and time strings
at.tweet(tweets, delay="2030-11-24 13:45", time_zone="America/Santiago")
at.tweet(tweets, delay="2030-11-24", time_zone="Australia/Sydney")
at.tweet(tweets, delay="13:45", time_zone="America/New_York")

# "keywords"
at.tweet(tweets, delay="next_week")

# integer
at.tweet(tweets, delay=3600)
```

Remember to read the [Notes for parsing DateTime strings](#Notes-for-parsing-DateTime-strings).

#### Post Twitter Updates with an interval

Use integers as seconds or some strings as keywords: `once_a_day`, `twice_perday` and `three_times_day`.

```python
# "keywords"
at.tweet(tweets, interval="three_times_day")

# integers
at.tweet(tweets, interval=3600)
```

#### Use a template

```python
at.tweet(tweets, template=template)
```

### Templates

Templates are very simple, just use a multiline string and add a `$message` where you want your message to appear.

```python
template = """My aswesome header

$message

#python #coding #AutoTweet
"""
```

## The Twitter API

AutoTweet is written using the [Python Twitter](https://github.com/bear/python-twitter) wrapper, and through `AutoTweet.api` you gain access to all of his models:

```python
# get your followers
followers = at.api.GetFollowers()

# get your direct messages
d_messages = at.api.GetDirectMessages()

# favorited tweets
favorites = at.api.GetFavorites()

# mentions
mentions = at.api.GetMentions()

# retweets
retweets = at.api.GetRetweets()
```

And a lot more. If you are interested, check their [documentation](https://python-twitter.readthedocs.io/en/latest/index.html).