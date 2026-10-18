# Problem: Check Strict Superset
# HackerRank: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

if __name__ == '__main__':
    main_set = set(input().split())
    n = int(input())
    result = True

    for _ in range(n):
        other_set = set(input().split())

        if not (main_set > other_set):
            result = False
            break

    print(result)
