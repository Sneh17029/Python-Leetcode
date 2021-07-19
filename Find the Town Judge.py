#Runtime: 732 ms, faster than 70.61% of Python3 online submissions for Find the Town Judge.
#Memory Usage: 19 MB, less than 64.63% of Python3 online submissions for Find the Town Judge.
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n!=1:
            return -1
        s=set()
        j=0
        for i in (trust):
            s.add(i[0])
        for i in range(1,n+1):
            if(i not in s):
                j=i
                break
        d=dict()
        for i in (trust):
            if i[0] not in d:
                d[i[0]] = list()
            d[i[0]].append(i[1])
        if(len(d)<n-1):
            return -1
        for i,v in d.items():
            if(j not in v):
                return -1
        return j