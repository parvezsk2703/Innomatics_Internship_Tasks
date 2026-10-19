# Problem: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        num = first
        result = ""

        while len(result) < len(s):
            result += str(num)
            num += 1

        if result == s:
            print("YES", first)
            return

    print("NO")
