# utility function
def jobOffers(scores, lowerLimits, upperLimits):
    answer = []
    for index, item in enumerate(lowerLimits):
        dummy = []
        for score in scores:
            if score >= lowerLimits[index] and score <= upperLimits[index]:
                dummy.append(score)
        if dummy:
            answer.append(len(dummy))
        else:
            answer.append(0)
    return answer


def jobOffers2(scores, lowerLimits, upperLimits):
    answer = []
    rangeList = list(zip(lowerLimits, upperLimits))
    for index, item in enumerate(rangeList):
        dummy = []
        for score in scores:
            if item[0] <= score <= item[1]:
                dummy.append(score)
        if dummy:
            answer.append(len(dummy))
        else:
            answer.append(0)
    return answer


# function to find first index >= x
def lowerIndex(arr, n, x):
    l = 0
    h = n - 1
    while (l <= h):
        mid = int((l + h) / 2)
        if (arr[mid] >= x):
            h = mid - 1
        else:
            l = mid + 1
    return l


# function to find last index <= x
def upperIndex(arr, n, x):
    l = 0
    h = n - 1
    while (l <= h):
        mid = int((l + h) / 2)
        if (arr[mid] <= x):
            l = mid + 1
        else:
            h = mid - 1
    return h


# function to count elements within given range
def countInRange(arr, n, x, y):
    # initialize result
    count = 0;
    count = upperIndex(arr, n, y) - lowerIndex(arr, n, x) + 1;
    return count


def jobOffers3(scores, lowerLimits, upperLimits):
    answer = []
    scores.sort()
    n = len(scores)
    for index, _ in enumerate(lowerLimits):
        answer.append(countInRange(scores, n, lowerLimits[index], upperLimits[index]))
    return answer


# dummy inputs
scores = [1, 3, 5, 6, 8]
lowerLimits = [2]
upperLimits = [6]

print(jobOffers3(scores, lowerLimits, upperLimits))
