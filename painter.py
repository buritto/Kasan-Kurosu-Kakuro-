from PIL import Image, ImageDraw
from cell_type import CellType


class Painter:
    
    def __init__(self, cell_size):
        self.cell_size = cell_size
    
    def paint(self, field, path, dimension):
        if not path.endswith('.png'):
            path += '.png'
        img = Image.new('RGB', (dimension * self.cell_size, dimension * self.cell_size), 'white')
        drawer = ImageDraw.Draw(img)
        for x in range(0, dimension):
            for y in range(0, dimension):
                drawer.line([x * self.cell_size, y * self.cell_size, x * self.cell_size,
                             (y + 1) * self.cell_size], fill='black')
                drawer.line([x * self.cell_size, y * self.cell_size, (x + 1) * self.cell_size,
                             y * self.cell_size], fill='black')
                if field[x][y].get_type() == CellType.RULES:
                    row = field[x][y].get_rules()[1]
                    column = field[x][y].get_rules()[0]
                    if row > 0:
                        to_str = str(int(row))
                        numbers = self.count_number(row)
                        drawer.text([x * self.cell_size + self.cell_size // 2, self.cell_size * y],
                                    text=to_str[0:numbers], fill='black', align='center')
                    if column > 0:
                        to_str = str(int(column))[0:3]
                        numbers = self.count_number(column)
                        drawer.text([self.cell_size * x, y * self.cell_size + self.cell_size // 2],
                                    text=to_str[0:numbers], fill='black')
                    drawer.line([x * self.cell_size, y * self.cell_size,
                                 (x + 1) * self.cell_size, (y + 1) * self.cell_size], 'black')
                if field[x][y].get_type() == CellType.PLAY:
                    drawer.text([self.cell_size * x + self.cell_size // 2, self.cell_size * y +
                                 self.cell_size // 2],
                                text=str(field[x][y].get_value()), fill='black', align='center')
                if field[x][y].get_type() == CellType.NO_ACTIVE:
                    drawer.rectangle([x * self.cell_size, y * self.cell_size,
                                      (x + 1) * self.cell_size, (y + 1) * self.cell_size], fill='black')
                img.save(path)

    def count_number(self, n):
        i = 0
        while n > 0:
            n = n // 10
            i += 1
        return i
