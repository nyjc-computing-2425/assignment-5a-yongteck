def to_hms(seconds):
    """
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated

    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
    """
    # Type your code below
    if isinstance(seconds, int):
      ls = [0,0,0]
      ls[1],ls[0] = divmod(seconds,60)
      ls[2],ls[1] = divmod(ls[1],60)
      return ls
    else:
      print("Unsupported input type.")

