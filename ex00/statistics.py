from typing import Any

STATISTICS = ["mean", "median", "quartile", "std", "var"]


def calculate_mean(numbers: list[int]) -> float:
    """Function to calculate the mean of a list of numbers."""

    return sum(numbers) / len(numbers)


def calculate_median(numbers: list[int]) -> float:
    """Function to calculate the median of a list of numbers."""

    return sorted(numbers)[len(numbers) // 2]


def calculate_quartile(numbers: list[int]) -> float:
    """Function to calculate the quartile of a list of numbers."""

    numbers_sorted = sorted(numbers)
    numbers_length = len(numbers)
    return [
        float(numbers_sorted[numbers_length // 4]),
        float(numbers_sorted[numbers_length // 4 * 3])
    ]


def calculate_std(numbers: list[int]) -> float:
    """Function to calculate the standard deviation of a list of numbers."""

    return calculate_var(numbers) ** 0.5


def calculate_var(numbers: list[int]) -> float:
    """Function to calculate the variance of a list of numbers."""

    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Function to calculate the mean, median, quartile, std, and var of a list
    of numbers.
    """

    for value in kwargs.values():
        if value not in STATISTICS:
            continue

        try:
            match value:
                case "mean":
                    result = calculate_mean(args)
                case "median":
                    result = calculate_median(args)
                case "quartile":
                    result = calculate_quartile(args)
                case "std":
                    result = calculate_std(args)
                case "var":
                    result = calculate_var(args)

            print(f"{value} : {result}")

        except Exception:
            print("ERROR")
            continue
