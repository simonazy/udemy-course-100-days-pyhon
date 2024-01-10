from random import randint
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y 

    def fall_in_rectangle(self, rectangle):
        if rectangle.pointA.x < self.x < rectangle.pointB.x and \
        rectangle.pointA.y < self.y < rectangle.pointB.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point1, point2) -> None:
        self.pointA = point1
        self.pointB = point2 

    def area(self):
        width = self.pointA.y - self.pointB.y
        length = self.pointA.x - self.pointB.x 
        return width*length  
    
#create rectangle object
rec = Rectangle(Point(randint(0,9),randint(0,9)), Point(randint(10,19), randint(10,19)))

print("Rectangle Coordinates: ", rec.pointA.x, ",", rec.pointA.y, ",", rec.pointB.x, ",", rec.pointB.y) 

user_point = Point(float(input("Your X coordinate: ")), float(input("Your Y coordinate")))
user_area = float(input("Guess the rectanlge area: "))
print("Your point was in rectangle: ", user_point.fall_in_rectangle(rec)) 
print("Your area is off the true area: ", rec.area()-user_area)

