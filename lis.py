n=int(input())
arr=list(map(int,input().split()))
def solution():
    LIS=[1]*n
    for i in range(n,-1,-1):
        for j in range(i+1,len(arr)):
            if nums[i]<nums[j]:
                LIS[I]=max(LIS[I],1+LIS[j])
    return max(LIS)
print(solution())
