class NoneError(TypeError):
    """
    Raised when the string provided to delay or interval
    is not valid.
    """

    delayInfoMessage = (
        "'delay' must be an int or a valid String: "
        "'half_hour', 'one_hour', 'tomorrow' or 'next_week'."
    )

    intervalInfoMessage = (
        "'interval' must be an int or a valid String: "
        "'once_a_day', 'twice_perday' or 'three_times_day'."
    )


class TweetTypeError(TypeError):
    """
    Raised when the argument provided to 'msg' is not a list.
    """

    tweetInfoMsg = "'msg' must be a list."


class TemplateError(TypeError):
    """ Raised when the wrong data type is provided in a template. """

    templateInfoMsg = "template must be a string."
