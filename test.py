
def function(number, kwarg = 3):
    """This is a function

    Args:
        number (integer): A number
        kwarg (integer, optional): Another integer. Defaults to 3.

    Raises:
        TypeError: Typer Error

    Returns:
        [type]: [description]
    """
    if number < 2:
        raise TypeError
    return kwarg
