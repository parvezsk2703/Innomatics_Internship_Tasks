# Problem: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
    weights = set()
    prev = ''
    count = 0

    for char in s:
        if char == prev:
            count += 1
        else:
            count = 1
            prev = char

        weights.add((ord(char) - ord('a') + 1) * count)

    return ['Yes' if q in weights else 'No' for q in queries]
