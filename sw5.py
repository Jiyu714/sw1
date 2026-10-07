# 5. [이진탐색] 떡볶이 떡 만들기

n, m = map(int, input().split())
cakes = list(map(int, input().split()))

low, high = 0, max(cakes)      # 변수 설정
ans = 0

while low <= high:
    mid = (low + high) // 2
    cut = sum(x - mid for x in cakes if x > mid)   

    if cut >= m:
        ans = mid   # 충분          
        low = mid + 1         
    else:
        high = mid - 1        

print(ans)
