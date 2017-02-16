# Given an array of integers, find contiguous subarray within it which has the largest sum.

# For example,

# Input:  {-2, 1, -3, 4, -1, 2, 1, -5, 4}
# Output: Subarray with the largest sum is {4, -1, 2, 1} with sum 6.

def kadane(arr):
    assert(len(arr) > 0)

    max_start = 0
    max_end = 0
    max_sum = arr[0]

    current_start = 0
    current_sum = arr[0]

    for i, x in enumerate(arr[1:]):
        if (x + current_sum > x):
            current_sum += x
        else:
            current_sum = x
            current_start = i + 1

        if current_sum > max_sum:
            max_start = current_start
            max_end = i + 1
            max_sum = current_sum

    print('Subarray with the largets sum is', arr[max_start:max_end+1], 'with sum', max_sum)

kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])
