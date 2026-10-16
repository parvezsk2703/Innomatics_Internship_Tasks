# Problem 6
# HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    score=sorted(set(arr))
    print(score[-2])
