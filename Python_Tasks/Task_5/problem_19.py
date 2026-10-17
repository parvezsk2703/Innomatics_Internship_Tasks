# Problem 19
# HackerRank: https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        uni = ""

        for char in substring:
            if char not in uni:
                uni += char

        print(uni)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
