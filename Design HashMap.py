#Runtime: 180 ms, faster than 99.97% of Python3 online submissions for Design HashMap.
#Memory Usage: 17.2 MB, less than 78.72% of Python3 online submissions for Design HashMap.
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d=dict()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.d[key]=value
            

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.d:
            return self.d[key]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.d:
            del self.d[key]
        else:
            pass
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)