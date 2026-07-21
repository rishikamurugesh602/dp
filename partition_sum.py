nums = list(map(int, input().split()))

def solution():

    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2

    dp = {0}

    for i in range(len(nums) - 1, -1, -1):

        new_dp = set()

        for t in dp:
            new_dp.add(t)
            new_dp.add(t + nums[i])

        dp = new_dp

        if target in dp:
            return True

    return False

print(solution())
