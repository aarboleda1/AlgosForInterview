from test_framework import generic_test
import heapq
import itertools
"""10.3 Sort an almost-sorted array

Often data is almost-sorted, for example a server receives timestamped stock
quotes and earlier quotes may arrive slightly after later quotes because of
differences in server loads and network routes. In this problem we address
efficient ways to sort such data.

Write a program which takes as input a very long sequence of numbers and prints
the numbers in sorted order. Each number is at most k away from its correctly
sorted position. (Such an array is sometimes referred to as being k-sorted).
For example, no number in the sequence [3,-1,2,6,4,5,8] is more than 2 away
from its final sorted position

Hint: How many numbers must you read after reading the ith number to be sure
you can place it in the correct location?

NOTE create your own test case, the test cases here aren't correct
(ATTEMPTED, 6/18)


[3,-1,2,6,4,5,8], k = 2, heap = []
[-1, 2,3,6,4,5,8]
write_idx, j, heap
0          2   [-1, 2, 3]
1          3   [6, 2, 3]
2          4   [6, 3, 4]

"""
def sort_approximately_sorted_array(A, k):
    heap = []
    for i in range(k):
        heapq.heappush(heap, A[i])

    write_idx = 0
    for j in range(k, len(A)):
        heapq.heappush(heap, A[j])
        val = heapq.heappop(heap)
        A[write_idx] = val
        write_idx += 1

    while heap:
        val = heapq.heappop(heap)
        A[write_idx] = val
    print(A)
    return A





def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    A, k = [3,-1,2,6,4,5,8], 2
    sort_approximately_sorted_array(A, k)
    # exit(
        # generic_test.generic_test_main(
            # "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            # sort_approximately_sorted_array_wrapper))
