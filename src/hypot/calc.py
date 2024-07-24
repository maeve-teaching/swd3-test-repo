# we want:
# h = sqrt(opp^2 + adj^2)
# we are going to use pure python

# calc the square of the value
def square(value):
    """Calculate the square of a number

    Args:
        value (int, float): Numerical value to be squared

    Returns:
        int, float: Squared value
    """
    squared = value * value
    return squared

# calc the addition of two values

def add(value_1, value_2):
    """Calculate the sum of two numbers

    Args:
        value_1 (int, float): First numerical value to be added
        value_2 (int, float): Second numerical value to be added

    Returns:
        int, float: Sum of both values
    """
    summed = value_1 + value_2
    return summed


# calc the squareroot of a value

def square_root(value):
    """calculate the square root of a number

    Args:
        value (int, float): Value to be square-rooted

    Returns:
        float: Square root of the argument value
    """
    root = value**(0.5)
    return root

# calc the hypot using pythagoras

def pythag(opp, adj):
    """Calculate the hypotenuse of a right angled triangle
    
    Given the lengths of theopposite and adjacent sides of a right-angled
    triangle, calculate the length of the hypotenuse using
    Pythagoras' theorem

    Args:
        opp (int, float): Opposite side of right-angled triangle
        adj (int, float): Adjacent side of right-angled triangle

    Returns:
        float: Hypotenuse of right-angled triangle
    """
    squared_opp = square(opp)
    squared_adj = square(adj)
    summed = add(squared_opp, squared_adj)
    hypot = square_root(summed)
    return hypot