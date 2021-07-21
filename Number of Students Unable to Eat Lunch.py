#Runtime: 28 ms, faster than 98.56% of Python3 online submissions for Number of Students Unable to Eat Lunch.
#Memory Usage: 14.1 MB, less than 77.84% of Python3 online submissions for Number of Students Unable to Eat Lunch.
class Solution:
    def countStudents(self, s: List[int], sa: List[int]) -> int:
        j=0
        while j!=len(s):
            if(s[0]==sa[0]):
                j=0
                s.pop(0)
                sa.pop(0)
            else:
                j+=1
                g=s.pop(0)
                s.append(g)
        return len(s)