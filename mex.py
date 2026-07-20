n = int(input())
arr=[int(input()) for _ in range(m)]

def solution():
    dp=[0]*n
    freq=[0]*n+1
    for i in range(n):
        mex=0
        freq=[0]*n+2
        for j in range(i,-1,-1):
            x=arr[j]
            if x<=n:
                freq[x]+=1
            while freq[mex]>0:
                mex+=1
            if j==0:
                dp[i]=max(dp[i],mex)
            else:
                dp[i]=max(dp[i],dp[j-1]+mex)
    return dp[n-1]
print(solution())
        
                
                
