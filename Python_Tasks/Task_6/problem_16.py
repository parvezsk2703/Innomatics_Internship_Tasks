# Problem: Check Subset
# HackerRank: https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        a = int(input())
        set_a = set(input().split())

        b = int(input())
        set_b = set(input().split())

        print(set_a.issubset(set_b))
