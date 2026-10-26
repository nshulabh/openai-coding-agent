def calculate_average(numbers):
    """Return the arithmetic mean of a list of numbers.

    Args:
        numbers: A non-empty list of numbers.

    Returns:
        The sum of the numbers divided by the length of the list.

    Raises:
        ValueError: If numbers is an empty list.
    """
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    values = [10, 20, 30]
    print(calculate_average(values))  # Expected output: 20.0
