# Problem: Pangrams
# HackerRank: https://www.hackerrank.com/challenges/pangrams/problem
def pangrams(s):
    # Write your code here
    letters = set(s.lower())

    if len(letters.intersection(set('abcdefghijklmnopqrstuvwxyz'))) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
