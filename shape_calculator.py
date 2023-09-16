class Rectangle:

    def __init__(self, w=0, h=0):
        self.width = w
        self.height = h

    def __str__(self):
        return (("Rectangle(width={0}, height={1})").format(self.width, self.height))

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self): 
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            pic = ('*' * self.width + '\n') * self.height
            return pic

    def get_amount_inside(self, obj):
        amount = (self.width // obj.width) * (self.height // obj.height)
        return int(amount)
        

        




class Square(Rectangle):

    def __init__(self, side=0):
        self.width = side
        self.height = side

    # String representation of Object
    def __str__(self):
        return (("Square(side={0})").format(self.width))

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side

    def set_height(self, side):
        self.height = side