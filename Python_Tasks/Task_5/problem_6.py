# Problem 6
# HackerRank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    # your code goes here
    uni=set(array)
    return sum(uni)/len(uni)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
