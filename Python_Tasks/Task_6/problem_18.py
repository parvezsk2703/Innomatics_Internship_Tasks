# Problem: Set Mutations
# HackerRank: https://www.hackerrank.com/challenges/py-set-mutations/problem
if __name__ == '__main__':
    n = int(input())
    main_set = set(map(int, input().split()))
    count = int(input())

    for _ in range(count):
        operation, size = input().split()
        other_set = set(map(int, input().split()))

        if operation == 'intersection_update':
            main_set.intersection_update(other_set)
        elif operation == 'update':
            main_set.update(other_set)
        elif operation == 'symmetric_difference_update':
            main_set.symmetric_difference_update(other_set)
        elif operation == 'difference_update':
            main_set.difference_update(other_set)

    print(sum(main_set))
