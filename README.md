<p align="center">
  <img src="coo.png" alt="Logo">
</p>

<h1 align="center">
  coo: schedule Twitter updates with easy
</h1>

<p align="center">
    <a href="https://badge.fury.io/py/coo">
        <img src="https://badge.fury.io/py/coo.svg" alt="PyPI version" height="18">
    </a>
    <a href="https://travis-ci.org/wilfredinni/coo">
        <img src="https://travis-ci.org/wilfredinni/coo.svg?branch=master" alt="Build Status">
    </a>
    <a href="https://codecov.io/gh/wilfredinni/coo">
        <img src="https://codecov.io/gh/wilfredinni/coo/branch/master/graph/badge.svg" alt="codecov">
    </a>
    <a href="https://coo.readthedocs.io/en/latest/?badge=latest">
        <img src="https://readthedocs.org/projects/coo/badge/?version=latest" alt="Docs">
    </a>
    <a href="https://opensource.org/licenses/Apache-2.0">
        <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License">
    </a>
</p>

Coo is an easy to use Python library for scheduling Twitter updates. To use it, you need to first apply for a developer account in the [Twitter Developers Platform](https://developer.twitter.com/) and generate the Keys and Access Tokens.


```shell
pip install coo
```

Initializing

```python
from coo import Coo

at = Coo(
    "consumer_key",
    "consumer_secret",
    "access_token",
    "access_token_secret",
    preview=False
)
```

Alternatively, you can set `preview=True` and print your tweets in the terminal instead to post them on Twitter.

Scheduling Twitter updates:

```python
from coo import Coo

at = Coo(
    "consumer_key",
    "consumer_secret",
    "access_token",
    "access_token_secret"
)

tweets = [
    ("2030-10-28 18:50", template, "My Twitter update with a template."),
    ("2030-10-29 18:15", template2, "Update with a different template."),
    ("2030-11-01 13:45", None, "Awesome Twitter update without a template."),
]

at.schedule(tweets, time_zone="America/Santiago")
```

Or you can use a list of strings and add a `delay`, `interval` and a `template`:

```python
tweets = [
    "My first awesome Twitter Update",
    "My second awesome Twitter Update",
    "My third awesome Twitter Update",
    "My fourth awesome Twitter Update",
    "My fifth awesome Twitter Update",
    "My sixth awesome Twitter Update",
]

at.tweet(tweets, delay="13:45", interval="four_hours", template=my_template)
```

For more detailed options and usage, keep reading or check the [documentation](https://coo.readthedocs.io/en/latest/) :blue_book:.


## Scheduling Twitter Updates

Schedule updates with `datetime` strings or integers and use [custom templates](#Templates) if needed.

```python
Coo.schedule(updates, time_zone, media)
```

Full example:

```python
from coo import Coo

at = Coo(
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

    # date with and without templates
    ("2030-12-25", template3, "Merry christmas!"),
    ("2031-01-01", None, "And a happy new year!"),

    # time with and without templates
    ("18:46", template2, "Will be post today at 18:46."),
    ("23:00", None, "A tweet for today at 23:00."),

    # integer (seconds) with and without templates
    (3600, template, "This tweet will be posted in an hour."),
    (86400, None, "This one, tomorrow at the same hour."),
]

at.schedule(tweets, time_zone="America/Santiago")
```

#### Notes for parsing DateTime strings

- If a time zone is not specified, it will set to `local`.
- The time will be set to 00:00:00 if it's not specified.
- When passing only time information the date will default to today.
- A future date is needed, otherwise a `ScheduleError` is raised.

Here you can find all the [Time Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) available.

#### Media files

There are two ways to add media files to your tweets. The first and easiest is to use one global file for all the updates:

```python
at.schedule(tweets, time_zone="America/Santiago", media="path/to/file.png")
```

Also, an individual file can be set for each one of the updates:

```python
tweets = [
    ("2030-10-28 18:50", template, "Update with an image.", "pics/owl.png"),
    ("2030-10-29 18:15", template, "Update with other media.", "videos/funny_video.mp4"),
    ("2030-11-01 13:45", template, "Tweet without media."),
]
```

Finally, it is possible to combine these to ways. For example, if most of the tweets are gonna use the same media and just a few will have a different or none:

```python
tweets = [
    ("2030-11-01 13:45", template, "Tweet with global media."),
    ("2030-11-02 13:45", template, "Tweet with global media."),
    ("2030-11-03 13:45", template, "Tweet with global media."),
    ("2030-11-04 13:45", template, "Tweet with global media."),
    ("2030-11-05 13:45", template, "Tweet with global media."),
    ("2030-11-06 13:45", template, "Tweet with global media."),
    ("2030-11-07 13:45", template, "Tweet with global media."),
    ("2030-11-08 13:45", template, "Tweet without media.", None),
    ("2030-11-09 13:45", template, "Tweet without media.", None),
    ("2030-12-10 18:50", template, "Update with an image.", "pics/owl.png"),
    ("2030-12-11 18:15", template, "Update with other media.", "videos/funny_video.mp4"),
]

at.schedule(tweets, time_zone="America/Santiago", media="path/to/global_media.png")
```

## Tweet a list of strings

Post ordered updates with `delay`, `interval`, and a [template](#Templates) if needed.

```python
Coo.tweet(updates, delay, interval, template, media, time_zone, aleatory)
```

```python
from coo import Coo

at = Coo(
    "consumer_key",
    "consumer_secret",
    "access_token",
    "access_token_secret"
)

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

#### Delay

You can use `datetime`, `date` and `time` strings, integers as seconds and some strings as [keywords](#Delay-and-Interval-Keywords): `half_hour`, `one_hour`, `one_day` and `one_week` between others to delay the post of your first update.

```python
# datetime, date and time strings
at.tweet(tweets, delay="2030-11-24 13:45", time_zone="America/Santiago")
at.tweet(tweets, delay="2030-11-24", time_zone="Australia/Sydney")
at.tweet(tweets, delay="13:45", time_zone="America/New_York")

# "keywords"
at.tweet(tweets, delay="one_week")

# integer
at.tweet(tweets, delay=604800)
```

Remember to read the [Notes for parsing DateTime strings](#Notes-for-parsing-DateTime-strings).

#### Interval

Use integers as seconds or some strings as [keywords](#Delay-and-Interval-Keywords): `half_hour`, `one_hour`, `one_day` and `one_week` between others.

```python
# "keywords"
at.tweet(tweets, interval="four_hours")

# integers
at.tweet(tweets, interval=14400)
```

#### Template

And of course, you can also set one [template](#Templates) for each one of the updates.

```python
at.tweet(tweets, template=template)
```

#### Media files

Use one media file for all of your updates:

```python
at.tweet(tweets, media="path/to/media.jpeg")
```

#### Random updates

To tweet your updates randomly:

```python
at.tweet(tweets, aleatory=True)
```

#### Delay and Interval Keywords

| Keyword          | Seconds |
| ---------------- | ------- |
| now              | 0       |
| half_hour        | 1800    |
| one_hour         | 3600    |
| two_hours        | 7200    |
| four_hours       | 14400   |
| six_hours        | 21600   |
| eight_hours      | 28800   |
| ten_hours        | 36000   |
| twelve_hours     | 43200   |
| fourteen_hours   | 50400   |
| sixteen_hours    | 57600   |
| eighteen_hours   | 64800   |
| twenty_hours     | 72000   |
| twenty_two_hours | 79200   |
| one_day          | 86400   |
| two_days         | 172800  |
| three_days       | 259200  |
| four_days        | 345600  |
| five_days        | 432000  |
| six_days         | 518400  |
| one_week         | 604800  |


## Templates

Templates are very simple, just use a multiline string and add a `$message` where you want your message to appear.

```python
template = """My awesome header

$message

#python #coding #coo
"""
```

## The Twitter API

Coo is written using the [Python Twitter](https://github.com/bear/python-twitter) wrapper, and through `Coo.api` you gain access to all of his models:

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

## TODO's

- [x] Add support for random updates.
- [x] Add support for media files.
- [x] Add support for multiple media files.
- [ ] Add support for media files from URLs.
- [ ] Add support for one template for all updates on `Coo.schedule`.
- [ ] Add logging.
- [ ] Support `.toml` files for configuration and tweets.
- [ ] Support resume after a process restart (see [apscheduler](https://github.com/agronholm/apscheduler)).
- [ ] Add a CLI.

## Documentation

Documentation available at [coo.readthedocs.io](https://coo.readthedocs.io/en/latest/).
