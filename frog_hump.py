n = int(input())
height=list(map(int,input().split()))

def solution():
    if n <= 1:
        return 1

    dp = [0] * (n)
    dp[0] = 0
    dp[1] = abs(height[1]-height[0])

    for i in range(2, n):
        cost1=dp[i-1]+abs(height[i]-height[i-1])
        cost2=dp[i-2]+abs(height[i]-height[i-2])
        dp[i]=min(cost1,cost2)
    return dp[-1]

print(solution())
