def compute_complexity(data):
    """
        For the supplied string `data`, compute the complexity.

        :param data: string, suggested password
        :return complexity: float, complexity rating of the supplied `data`
    """
    # the permitted non-alphanumeric characters
    complexifiers = ['~', '@', '#', '$', '%', '^', '&', '-', '_', '+', '=']

    num_complexifiers = 0

    for char in data:
        if char in complexifiers:
            num_complexifiers = num_complexifiers + 1

    # compute the complexity
    length_of_data = len(data)
    complexity = (num_complexifiers * 100) / length_of_data

    return complexity


def evaluate_strength(password):
    """
        For the supplied `password`, evaluate whether the password is strong enough
        to be acceptable.

        :param password: str, attempted password
        :return: bool, True if acceptable, else False
    """
    if not isinstance(password, str):
        msg = f"Error: Attempted password '{password}' must be a string!."
        raise TypeError(msg)

    strength_threshold = 50.0
    complexity = compute_complexity(password)

    if complexity > strength_threshold:
        return True
    else:
        return False
