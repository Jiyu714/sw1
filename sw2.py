# 2. [DFS] 음료수 얼려먹기

n, m = input().split()   
n, m = int(n), int(m)               
ice = [list(input().strip()) for _ in range(n)]     # 하나씩

def dfs(sx, sy):

    stack = [(sx, sy)]                      # 시작 좌표
    ice[sx][sy] = '1'       

    while stack:
        x, y = stack.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == '0':
                ice[nx][ny] = '1'          
                stack.append((nx, ny))

count = 0

for i in range(n):
    for j in range(m):
        if ice[i][j] == '0':
            dfs(i, j)
            count += 1

print(count)