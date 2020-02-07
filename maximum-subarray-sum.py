def maxSequence(arr):
    max_sum = 0
    for start_i in range(len(arr)):
        if arr[start_i] > 0:
            for end_i in range(start_i + 1, len(arr)):
                max_sum = max(max_sum, sum(arr[start_i:end_i+1]))
    return max_sum
