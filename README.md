# AutoTweet

[![Build Status](https://travis-ci.org/wilfredinni/auto-tweet.svg?branch=master)](https://travis-ci.org/wilfredinni/auto-tweet)
[![codecov](https://codecov.io/gh/wilfredinni/auto-tweet/branch/master/graph/badge.svg)](https://codecov.io/gh/wilfredinni/auto-tweet)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Work in Progress

```python
from auto_tweet import AutoTweet

at = AutoTweet(
    "consumer_key",
    "consumer_secret",
    "token",
    "token_secret",
)

# verify the connection
at.verify

# WORK WITH A SINGLE TWEET
at.tweet(["my Twitter Update"])

# Tweet with a time delay option using seconds or a string:
# "half_hour", "one_hour", "tomorrow" and "next_week" for now.
at.tweet("my Twitter Update", delay=10)
at.tweet("my Twitter Update", delay="half_hour")


# WORK WITH A LIST OF TWEETS
my_posts = ["this is my first post", "this is my sencond one", "and the last one"]

# Post them all at once:
at.tweet(my_posts)

# With delay in seconds or strings:
# "half_hour", "one_hour", "tomorrow" and "next_week" for now.
at.tweet(my_posts, delay=4)
at.tweet(my_posts, delay="tomorrow")

# With an interval between updates in seconds or string:
# "once_a_day", "twice_perday", "three_times_day"
at.tweet(my_posts, delay="next_week", interval=3600)
at.tweet(my_posts, interval="twice_perday")

# TEMPLATES
# $message will be replaced with your messages:
my_template = """My Message Header

$message

#AutoTweet #python"""

at.tweet(my_posts, delay=4, template=my_template)
at.tweet(my_posts, delay="tomorrow", template=my_template)
at.tweet(my_posts, interval="twice_perday", template=my_template)
at.tweet(my_posts, delay="next_week", interval=3600, template=my_template)
```

## TODO

- Multiple Twitter Updates with delay and interval options for each one (dict)
