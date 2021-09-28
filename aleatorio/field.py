class Field:
    def __init__(self):
        self.coord_borracho = {}

    def add_borracho(self,borracho,coord):
        self.coord_borracho[borracho] = coord

    def move_borracho(self, borracho):
        delta_x, delta_y = borracho.walk()
        coord = self.coord_borracho[borracho]
        new_coord = coord.move(delta_x, delta_y)

        self.coord_borracho[borracho] = coord

    
    def get_coord(self, borracho):
        return self.coord_borracho[borracho]