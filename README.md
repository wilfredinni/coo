# auto-tweet

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

# Tweet now
at.tweet("my Twitter Update")

# Tweet with a time delay using seconds
at.tweet("my Twitter Update", delay=10)

# Tweet with a time delay using a string:
# "half_hour", "one_hour", "tomorrow" and
# "next_week"
at.tweet("my Twitter Update", delay="half_hour")
```

## TODO

- Multiple Twitter Updates with delay and interval options (list)
- Multiple Twitter Updates with delay and single interval option for each one (dict)
