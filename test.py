from coo import Coo

at = Coo(
    "consumer_key",
    "consumer_secret",
    "access_token",
    "access_token_secret",
    preview=True,
)

tweets = [
    "My first awesome Twitter Update",
    "My second awesome Twitter Update",
    "My third awesome Twitter Update",
    "My fourth awesome Twitter Update",
    "My fifth awesome Twitter Update",
    "My sixth awesome Twitter Update",
]

at.tweet(tweets, delay=3, interval=2)
