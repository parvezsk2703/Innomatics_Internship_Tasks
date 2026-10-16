# Problem 7
# HackerRank: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
def split_and_join(line):
    word=line.split()
    return "-".join(word)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
