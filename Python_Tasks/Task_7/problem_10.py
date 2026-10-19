# Problem: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(s):
    return 1 + sum(1 for char in s if char.isupper())
