import math


class MyFirstClass:
    pass


class Point:
    def move(self,x:float,y:float) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0,0)

    def calculate_distance(self,p:"Point") -> float:
        return math.hypot(self.x - p.x,self.y - p.y)

