Runtime: 128 ms, faster than 98.47% of Python3 online submissions for Design Parking System.
Memory Usage: 14.9 MB, less than 23.28% of Python3 online submissions for Design Parking System.
```
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.space=[big,medium,small]

    def addCar(self, carType: int) -> bool:
        if(self.space[carType-1]!=0):
            self.space[carType-1]=self.space[carType-1]-1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)