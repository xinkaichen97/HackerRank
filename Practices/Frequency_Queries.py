# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    ans = []
    counts = Counter()  # current count of each element
    freq = Counter()  # frequency of counts (e.g. 4: 2 means the frequecy of 4 occurs twice), for faster search
    for query in queries:
        op, num = query
        if op == 1:  # add element
            freq[counts[num]] -= 1  # need to update the freq counter
            counts[num] += 1
            freq[counts[num]] += 1
        elif op == 2:  # delete element (if exists)
            if counts[num] > 0:
                freq[counts[num]] -= 1  # need to update the freq counter
                counts[num] -= 1
                freq[counts[num]] += 1
        elif op == 3:  # find the frequency in freq
            if freq[num] > 0:
                ans.append(1)
            else:
                ans.append(0)
    return ans
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
