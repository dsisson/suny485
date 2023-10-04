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
        print(f"char --> {char}")
        if char in complexifiers:
            num_complexifiers = num_complexifiers + 1

    # compute the complexity
    length_of_data = len(data)
    print(f"length --> {length_of_data}")

    complexity = (num_complexifiers * 100) / length_of_data
    print(f"num_complexifiers --> {num_complexifiers}")
    print(f"length_of_data --> {length_of_data}")
    print(f"complexity --> {complexity}")
    print(f"num/length --> {num_complexifiers/length_of_data}")

    return complexity
