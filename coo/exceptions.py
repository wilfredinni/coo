class TweetTypeError(TypeError):
    """
    Raised when the argument provided to 'msg' is not a list.
    """

    tweetInfoMsg = "A list is required."
    wrongListMsg = "A list of strings is required."


class TemplateError(TypeError):
    """ Raised when the wrong data type is provided in a template. """

    templateInfoMsg = "template must be a string."


class ScheduleError(TypeError):

    wrongListMsg = "A list of tuples is required."
    tupleLenError = "Every tuple need a length of 3."
    pastDateError = "A future date is needed."
