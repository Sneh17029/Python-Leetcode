#Runtime: 24 ms, faster than 94.71% of Python3 online submissions for N-th Tribonacci Number.
#Memory Usage: 14.2 MB, less than 71.38% of Python3 online submissions for N-th Tribonacci Number.

class Solution:
    def tribonacci(self, n: int) -> int:
        if(n==0):return 0
        if(n==1):
            return 1
        if(n==2):
            return 1
        l=[0]*(n+1)
        l[0]=0
        l[1]=l[2]=1
        for i in range(3,n+1):
            l[i]=l[i-3]+l[i-1]+l[i-2]
        return l[-1]