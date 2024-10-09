def add(numbers):
    if numbers == "":
        return 0
    
    # Handle custom delimiter
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split('\n', 1)
        numbers = numbers.replace(delimiter, ',')
    
    # Split numbers and check for negative numbers
    nums = list(map(int, numbers.split(',')))
    negatives = [num for num in nums if num < 0]
    
    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")
    
    return sum(nums)
