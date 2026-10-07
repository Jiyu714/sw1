# 1. [구현] 상하좌우
 
n = int(input())
plan = input().replace(" ", "")   
 
x, y = 1, 1                        
move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
 
for p in plan:
    dx, dy = move[p]
    nx, ny = x + dx, y + dy
    if 1 <= nx <= n and 1 <= ny <= n:  
        x, y = nx, ny
 
print(x, y)