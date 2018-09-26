class NoneError(TypeError):
    """
    Raised when the string argument provided to delay or interval
    is not valid.
    """

    delayInfoMessage: str = (
        "'delay' must be an int(secs) or a valid String: "
        "'half_hour', 'one_hour', 'tomorrow' or 'next_week'."
    )

    intervalInfoMessage: str = (
        "'interval' must be an int(secs) or a valid String: "
        "'once_a_day', 'twice_perday' or 'three_times_day'."
    )
