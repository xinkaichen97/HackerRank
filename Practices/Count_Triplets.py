# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
import math
import os
import random
import re
import sys
from collections import Counter

def countTriplets(arr, r):
    arr_count = {}  # for array element counts
    arr_pair = {}  # for pairs (a, a * r)
    triplets = 0
    for a in reversed(arr):
        if a * r in arr_pair:  # (a * r) also in the key, triplet found
            triplets += arr_pair[a * r]
        if a * r in arr_count:  # update arr_pair: increment by the count of (a * r)
            arr_pair[a] = arr_pair.get(a, 0) + arr_count[a * r]
        arr_count[a] = arr_count.get(a, 0) + 1  # update count
    return triplets

# Alternative solution (accepted)
# def countTriplets(arr, r):
#     a = Counter(arr)
#     b = Counter()
#     s = 0
#     for i in arr:  # i serves as the middle number
#         j = i // r
#         k = i * r
#         a[i] -= 1  # decrease count after being examined
#         if b[j] and a[k] and i % r == 0:  # j and k found
#             s += b[j] * a[k]  # count of the first number in the triplet so far * count of the last one in the triplet that haven't been examined
#         b[i]+=1
#     return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
