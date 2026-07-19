m, n = map(int, input().split())
grid=[]
for _ in range(m):
    row=list(map(int,input().split()))
    grid.append(row)

def solution():
    dp = [[0] * n for _ in range(m)]
    if grid[0][0]==1:
        return 0
    dp =[[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                dp[i][j]=0
            else:
                if i==0 and j==0:
                    dp[0][0]=1
                    continue
                up=0
                left=0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
    return dp[m-1][n-1]
    

print(solution())
