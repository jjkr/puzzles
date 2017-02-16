# Given an unsorted array of integers, find a pair with given sum in it .

def find_pair(arr, s):
    hm = {}
    for i in range(len(arr)):
        x = arr[i]
        diff = s - x
        if diff in hm:
            otheri = hm[diff]
            print('Pair found at index', otheri, 'and', i, '(', diff, '+', x, ')')
            return (otheri, i)
        hm[x] = i

find_pair([8, 7, 2, 5, 3, 1], 10)
