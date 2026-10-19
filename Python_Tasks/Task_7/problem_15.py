# Problem: Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

def gameOfThrones(s):
    odd = sum(1 for count in Counter(s).values() if count % 2 != 0)

    if odd <= 1:
        return "YES"
    return "NO"
