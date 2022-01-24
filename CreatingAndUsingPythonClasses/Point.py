import platform

class Point:
    def __init__(self, x, y ):
        self.x = y
        self.y = y
    
    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] \
        and  lowleft[1] < self.y < upright[1]:
            return True 
        else:
            return False       




class House:

    def __init__(self, wall_area):
        self.wall_area = wall_area
       
        
class Paint:

    def __init__(self, buckets, color):
        self.color = color
        self.buckets = buckets



point1 = Point(1,2)


print(point1.x)
