# https://leetcode.com/problems/design-parking-system/
# 04.04.2026


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.d = {}
        self.d[1] = big
        self.d[2] = medium
        self.d[3] = small


    def addCar(self, carType: int) -> bool:
        if self.d[carType]:
            self.d[carType] -= 1
            return True
        return False
