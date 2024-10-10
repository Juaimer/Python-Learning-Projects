class Rectangle:
    type_square = 'Rectangle'
    def __init__(self, *args):
            if len(args) > 1:
                self.width = args[0]
                self.height = args[1]
            else:
                self.width = args[0]
                self.height = args[0]
    
    def set_width(self, width):

        if isinstance(self, Square):
            self.width = width
            self.height = width
        else:
            self.width = width
    
    def set_height(self, height):
        if isinstance(self, Square):
            self.width = height
            self.height = height
        else:
            self.height = height
        
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width **2 + self.height**2) ** 0.5
    
    def get_amount_inside(self, other):
        return self.width // other.width * (self.height // other.height)
    
    def get_picture(self):
        if self.width > 50 or self.height> 50:
            return 'Too big for picture.'
        
        shape_result = '\n'.join('*'* self.width for _ in range(self.height))

        return shape_result + '\n'
    
    def __str__(self):
        return f'{self.type_square}(width={self.width}, height={self.height})' if self.type_square == "Rectangle" else f'{self.type_square}(side={self.width})'
 
    
    
class Square(Rectangle):
    type_square = 'Square'
    def __init__(self, *args):
        super().__init__(*args)
        self.width = args[0]
        self.height = args[0]

    def set_side(self, side):
        self.width = side
        self.height = side