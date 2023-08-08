def cut_paper(x, y, size):
    global count_minus, count_zero, count_plus
    
    start_value = paper[x][y]
    same = True
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != start_value:
                same = False
                break
        if not same:
            break
    
    if same:
        if start_value == -1:
            count_minus += 1
        elif start_value == 0:
            count_zero += 1
        else:
            count_plus += 1
    else:
        new_size = size // 3
        for i in range(3):
            for j in range(3):
                cut_paper(x + i * new_size, y + j * new_size, new_size)

# 입력 받기
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# -1, 0, 1의 개수를 담을 변수 초기화
count_minus, count_zero, count_plus = 0, 0, 0

# 함수 호출하여 종이 개수 세기
cut_paper(0, 0, N)

# 결과 출력
print(count_minus)
print(count_zero)
print(count_plus)
