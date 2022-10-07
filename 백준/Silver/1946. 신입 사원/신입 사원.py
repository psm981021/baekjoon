import sys

test_case = int(sys.stdin.readline())
for i in range(test_case):
    n = int(sys.stdin.readline())
    employee = []
    cnt = 1
    for j in range(n):
        employee.append(list(map(int,sys.stdin.readline().split())))

    employee.sort()


    score = employee[0][1]
    for _ in range(1,n):
        if score > employee[_][1] :
            cnt+=1
            score = employee[_][1]

    print(cnt)