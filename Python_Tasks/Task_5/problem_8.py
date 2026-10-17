# Problem 8
# HackerRank: https://www.hackerrank.com/challenges/py-set-add/problem
if __name__ == '__main__':
    n = int(input())
    countr = set()
    for _ in range(n):
        countr.add(input().strip())
    print(len(countr))
