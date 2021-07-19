#Runtime: 764 ms, faster than 96.66% of Python3 online submissions for Find Center of Star Graph.
#Memory Usage: 50.4 MB, less than 21.36% of Python3 online submissions for Find Center of Star Graph.
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        f=edges[0][0] 
        s=edges[0][1]
        if(f in edges[1]):
            return f
        else:
            return s