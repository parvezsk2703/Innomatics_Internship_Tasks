# Problem: Alphabet Rangoli
# HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def print_rangoli(size):
    # your code goes here
    import string
    letters = string.ascii_lowercase

    lines = []
    for i in range(size):
        left = letters[size - 1:size - i - 1:-1]
        right = letters[size - i - 1:size]
        row = '-'.join(left + right)
        lines.append(row.center(4 * size - 3, '-'))

    print('\n'.join(lines + lines[-2::-1]))
