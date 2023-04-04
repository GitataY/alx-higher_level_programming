def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or a float.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.

    """
    # Check if size is an integer or a float
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    
    # If size is a float, check if it's less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # If size is less than 0, raise ValueError
    if size < 0:
        raise ValueError("size must be >= 0")
    
    # Convert size to integer if it's a float
    size = int(size)

    # Print the square with #
    for i in range(size):
        print('#' * size)
