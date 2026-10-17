# Problem 18
# HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    stuart = 0
    kevin = 0
    length = len(string)

    for i in range(length):
        points = length - i

        if string[i] in vowels:
            kevin += points
        else:
            stuart += points

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
