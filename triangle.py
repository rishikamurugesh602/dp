n = int(input())

triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

def solution():
    dp = [[0] * len(row) for row in triangle]

    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(len(triangle[i])):

            # First element
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]

            # Last element
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]

            # Middle elements
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

    return min(dp[n-1])

print(solution())
