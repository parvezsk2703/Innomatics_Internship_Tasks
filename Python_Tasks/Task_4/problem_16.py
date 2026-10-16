# Problem 16
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    stu=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu.append([name, score])

    scores = sorted(set(student[1] for student in stu))
    second_lowest = scores[1]

    names = sorted(
        student[0] for student in stu
        if student[1] == second_lowest
    )

    for name in names:
        print(name)
