# super() =  Function used to give access to the methods of a parent class.

class Rectangule:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width  pass

class Square(Rectangule):
    def __init__(self,lenght,width):
        super().__init__(lenght,width)


class Cube(Rectangule):
    def __init__(self,lenght,width,height):
        super().__init__(lenght,width) 
        self.height = height
