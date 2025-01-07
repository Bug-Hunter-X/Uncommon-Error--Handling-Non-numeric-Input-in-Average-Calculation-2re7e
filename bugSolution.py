def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 # Handle case where no numeric values are present
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage
print(calculate_average([1, 2, 3, 4, 5]))  # Output: 3.0
print(calculate_average([]))  # Output: 0
print(calculate_average([1, 2, 'a', 4, 5])) # Output: 0
print(calculate_average(['a', 'b', 'c'])) # Output: 0