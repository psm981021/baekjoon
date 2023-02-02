#https://www.acmicpc.net/problem/1107

def DFS(numS):
    defNum = abs(int(n) - int(numS))
    if defNum+len(str(numS)) < minDef[1]+len(str(minDef[0])):
        minDef[0] = numS
        minDef[1] = defNum
        minDef[2] = len(str(int(numS)))  # 숫자 첫 번째에 0이 붙으면 제거하기 위해

    if len(numS) > len(n):
        return True
    else:
        for i in btn:
            DFS(numS + i)


global n
start = 100
n = input()  # 이동하려는 채널
m = int(input())  # 고장난 버튼 개수
broke = []
if m > 0:
    broke = list(map(int, input().split()))

btn = []  # 사용 가능 버튼
for i in range(0, 10):
    if i not in broke:
        btn.append(str(i))

# 입력 가능한 버튼을 DFS 방식으로 탐색
#  index 0: n과의 차이가 가장 적은 값의 수
#  index 1: n과의 차가 가장 작은값
#  index 2: 수를 만들기 위해 눌러야 하는 횟수
minDef = [100, 500000, 0]
for i in btn:
    DFS(i)

res = []
# n을 만들기 위해 최소한을 눌러야 하는 총 횟수
res.append(minDef[1] + minDef[2])

# 만약 +, - 만 누르는 것이 숫자를 누르는 횟수보다 빠른지 확인
res.append(abs(int(n) - start))

# 최솟값 출력
print(min(res))