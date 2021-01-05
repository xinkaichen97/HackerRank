# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    words = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]  # get all possible substrings
    word_dict = {}
    count = 0
    for word in words:  # O(nlog(n))
        sorted_word = "".join(sorted(word))  # sort the words so that anagrams become the same
        word_dict[sorted_word] = word_dict.get(sorted_word, 0) + 1  # add to dictionary
    for key in word_dict:
        count += word_dict[key] * (word_dict[key] - 1) // 2  # for each key, possible pairs would be C(word_dict[key], 2)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
