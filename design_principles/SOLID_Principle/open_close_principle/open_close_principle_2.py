"""
SOLID Principles: Open Close Principle
Example 2
"""


class Piece:
    def __init__(self, color):
        self.color = color
    
    def move(self):
        raise Exception("Not Implemented")


class Horse(Piece):
    
    def move(self):
        # move logic
        pass


class Tower(Piece):
    
    def move(self):
        # move logic
        pass