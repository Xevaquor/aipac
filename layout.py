__author__ = 'Xev'


class Tile:
    def __init__(self):
        pass

    Empty, Wall, Start, StartGhost = range(4)


class Layout(object):
    def __init__(self):
        self.grid = []
        self.shape = (0, 0)
        self.food = []

    def load_from_file(self, filename):
        rows = 0
        with open(filename, 'r') as f:
            for line in f:
                self.grid.append([])
                self.food.append([])
                rows += 1
                cols = 0
                for char in line:
                    has_food = False
                    if char == ' ':
                        tile = Tile.Empty
                    elif char == 'X':
                        tile = Tile.Wall
                    elif char == 'S':
                        tile = Tile.Start
                    elif char == '\r' or char == '\n':
                        break
                    elif char == '.':
                        has_food = True
                        tile = Tile.Empty
                    else:
                        raise Exception('Unknown tile type: \'' + char + '\'')
                    self.grid[-1].append(tile)
                    self.food[-1].append(has_food)
                    cols += 1
        self.grid.reverse()
        self.food.reverse()
        self.shape = (rows, cols)
        self.rows = rows
        self.cols = cols

