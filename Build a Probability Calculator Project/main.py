import copy
import random

class Hat:
    def __init__(self, **args):
        self.contents = []
        for value in args:
            for _ in range(args[value]):
                self.contents.append(value)
    def draw(self, amount_of_balls_to_drawn):
        drawn_balls = []
        if amount_of_balls_to_drawn >= len(self.contents):
            temporary_copy = copy.deepcopy(self.contents)
            self.contents.clear()
            return temporary_copy
        
        for _ in range(amount_of_balls_to_drawn):
            index_to_be_removed = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(index_to_be_removed))        
        return drawn_balls

    def __str__(self):
        return f'{self.contents}'

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        freq = {color: drawn_balls.count(color) for color in drawn_balls}
        count_color = 0 
        for index in expected_balls.keys():
            if drawn_balls.count(index)>= expected_balls[index]:
                count_color +=1 
   
        if count_color == len(expected_balls):
            count+=1
        

    return count/num_experiments
