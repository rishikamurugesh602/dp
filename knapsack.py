n = int(input())

weights = list(map(int, input().split()))
values = list(map(int, input().split()))

capacity = int(input())

dp = [0] * (capacity + 1)

for i in range(n):
    for w in range(capacity, weights[i] - 1, -1):
        dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

print(dp[capacity])
