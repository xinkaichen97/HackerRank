# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

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
