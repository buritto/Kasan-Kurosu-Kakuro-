from cell import Cell
from cell_type import CellType


class GameField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.filed = []
        for x in range(0, width):
            self.filed[x] = []
            for y in range(0, height):
                self.filed[x][y] = Cell(CellType.NO_ACTIVE)
