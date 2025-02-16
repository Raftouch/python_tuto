class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

# Object is an Instance of a Class

point_one = Point()
point_one.x = 10
point_one.y = 20

point_one.draw()
print(point_one.x)

point_two = Point()