

class Piece:

    def __init__(self, position):

        self.movement_list = []
        self.movement_limit = 0
        self.position = position

    def move(self, next_position):

        if self.is_legal(next_position):

            self.position = next_position

    def is_legal(self, next_position):
        
        return False


        
