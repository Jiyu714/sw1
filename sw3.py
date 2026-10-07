# 3. [BFS] 미로 탈출

from collections import deque

n, m = input().split()   
n, m = int(n), int(m)            
maze = [input().strip() for _ in range(n)]  # 행씩

dist = [[0] * m for _ in range(n)]         # 방문 여부, 거리 
dist[0][0] = 1

q = deque([(0, 0)])

while q:
    x, y = q.popleft()
    if (x, y) == (n - 1, m - 1):
        break

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '1' and dist[nx][ny] == 0:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

print(dist[n - 1][m - 1])
