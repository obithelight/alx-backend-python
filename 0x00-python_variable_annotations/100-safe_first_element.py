from typing import Sequence, Any, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieves the first element from the input list 'lst' safely.

    Args:
        lst (Sequence[Any]): The input list.

    Returns:
        Union[Any, None]: The first element of the list or 'None' if
        the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
