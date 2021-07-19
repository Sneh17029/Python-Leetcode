#Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Maximum Number of Words You Can Type.
#Memory Usage: 14.4 MB, less than 66.67% of Python3 online submissions for Maximum Number of Words You Can Type.

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t=text.split(" ")
        b=list(brokenLetters)
        print(t,b)
        ans=[]
        for i in range(len(t)):
            c=0
            for j in range(len(b)):
                if(b[j] in t[i]):
                    c+=1
                    break
            if(c==0):
                ans.append(t[i])
        return len(ans)