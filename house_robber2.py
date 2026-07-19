nums = list(map(int, input().split()))

def rob(arr):
    n = len(arr)

    if n == 1:
        return arr[0]

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])

    return dp[-1]


def solution():
    n = len(nums)

    if n == 1:
        return nums[0]

    # Case 1: Don't rob last house
    case1 = rob(nums[:-1])

    # Case 2: Don't rob first house
    case2 = rob(nums[1:])

    return max(case1, case2)


print(solution())
