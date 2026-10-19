# Problem: Making Anagrams
# HackerRank: https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

def makingAnagrams(s1, s2):
    count1 = Counter(s1)
    count2 = Counter(s2)

    return sum((count1 - count2).values()) + sum((count2 - count1).values())
