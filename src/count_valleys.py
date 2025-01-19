def countingValleys(steps, path):
    level = 0
    valleys = 0
    for i in range(steps):
        current = path[i]
        if current == "U":
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    return valleys


def jumpingOnClouds(c):
    last_cloud_idx = len(c) - 1
    num_jumps = 0
    cur_pos = 0
    while cur_pos < last_cloud_idx:
        if c[min(cur_pos + 2, last_cloud_idx)] == 0:
            cur_pos += 2
        elif c[cur_pos + 1] == 0:
            cur_pos += 1
        else:
            raise Exception("no jump possible")
        num_jumps += 1
    return num_jumps


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    count_substring = len([1 for c in s if c == 'a'])
    factor = n // len(s)
    count = count_substring * factor
    count += len([1 for c in s[:(n % len(s))] if c == 'a'])
    return int(count)


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    hourglass_sums = []
    for row in range(4):
        for col in range(4):
            cur_sum = sum(arr[row][col:col+3])\
                + arr[row+1][col+1]\
                + sum(arr[row+2][col:col+3])
            hourglass_sums.append(cur_sum)
    print(hourglass_sums)
    return max(hourglass_sums)


#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    split_index = d % len(a)
    return a[split_index:] + a[:split_index]


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    num_swaps = 0
    for i in range(len(q) - 1):
        tmp_swaps = 0
        partial_agg_swaps = 0
        for j in range(len(q) - 1 - i):
            if q[j] > q[j + 1]:
                tmp = q[j]
                q[j] = q[j + 1]
                q[j + 1] = tmp
                tmp_swaps += 1
                if tmp_swaps > 2:
                    return "Too chaotic"
            else:
                partial_agg_swaps += tmp_swaps
                tmp_swaps = 0
        partial_agg_swaps += tmp_swaps
        if partial_agg_swaps == 0:
            break
        num_swaps += partial_agg_swaps
    return num_swaps


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    events = []
    for (start, end, value) in queries:
        events.append((start, -1, value))
        events.append((end, 1, -value))
    events.sort(key=lambda x: (x[0], x[1]))

    current_agg = 0
    max_agg = 0
    for (t, _, value) in events:
        current_agg += value
        max_agg = max(max_agg, current_agg)
    return max_agg



