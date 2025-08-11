def max_sequence(arr):
    current_sum = 0
    max_sum = 0

    for _, num in enumerate(arr, start=1):
        current_sum = max(num, current_sum + num)

        # If the rule says negatives are not allowed in final answer:
        if current_sum < 0:
            current_sum = 0
        
        max_sum = max(max_sum, current_sum)

    
    return max_sum


# Example
result = max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print("\nFinal result:", result)