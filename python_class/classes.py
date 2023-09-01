class Point():
    # when I create a point What should happen?
    # magic method __init__
    # Below function automatically be called Whenever we create a new point. 
    # All functions that operate on object themselves are going to take first argument "self"

    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(4, 9)

print(p.x)
print(p.y)