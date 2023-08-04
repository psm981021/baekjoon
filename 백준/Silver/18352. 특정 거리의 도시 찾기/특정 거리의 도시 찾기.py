from collections import deque

def find_distance(graph, start, k):
    n = len(graph)
    distance = [-1] * (n+1)
    distance[start] = 0
    queue = deque([(start, 0)])

    while queue:
        current, dist = queue.popleft()
        for next_city in graph[current]:
            if distance[next_city] == -1:
                distance[next_city] = dist + 1
                queue.append((next_city, dist + 1))
    
    result = [city for city in range(1, n+1) if distance[city] == k]

    return result if result else [-1]

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = find_distance(graph, x, k)

for city in result:
    print(city)
