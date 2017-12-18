from game_field import  GameField
from kakuro_parser import  Parser
from game_cell import Cell
from cell_type import CellType
from painter import Painter
from solver import Solver


class CommandLineMode:
    def __init__(self, dimension):
        self.game = GameField(dimension, dimension)
        self.dimansion = dimension
        self.all_line = []

    def add_cell(self, line):
        frame = line.split('|')
        if len(frame) != 6:
            print('Incorrect line')
            return
        try:
            pos_x = self.get_frame(frame[0])
            pos_y = self.get_frame(frame[1])
            row_sum = self.get_frame(frame[2])
            row_length = self.get_frame(frame[3])
            column_sum = self.get_frame(frame[4])
            column_length = self.get_frame(frame[5])
        except Exception as e:
            print('incorrect line')
            return
        cell = Cell(CellType.RULES, row_rule=row_sum, column_rule=column_sum,
                    length_row=row_length, length_column=column_length)
        self.game.init_cell(pos_x, pos_y, cell)
        self.all_line.append(line)

    def get_frame(self, frame):
        return int(frame.rstrip().lstrip())

    def interpret(self, line):
        if ':' in line:
            command = line.split(':')[0].lstrip().rstrip()
            date = line.split(':')[1].lstrip().rstrip()
            if command == 'add':
                self.add_cell(date)
                return
            if command == 'save_png':
                self.save_png(date)
                return
            if command == 'save_kk':
                self.save_kk(date)
                return
        if line == 'solve':
            self.solve()
        print('Incorrect command')

    def save_png(self, path):
        if not path.endswith('.png'):
            path += '.png'
        pa = Painter(64)
        pa.paint(self.game.field, path, self.dimansion)

    def save_kk(self, date):
        if not date.endswith('kk'):
            date += '.kk'
        with open(date, 'w') as f:
            f.write(self.dimansion + '\n')
            for line in self.all_line:
                f.write(line + '\n')

    def solve(self):
        solver = Solver(self.game)
        try:
            solver.solve()
            print('Accepted')
        except Exception as e:
            print("Can not find solution")


if __name__ == '__main__':
    dimension = 0
    while True:
        print('Please enter dimension field')
        dimension = input()
        try:
            dimension_int = int(dimension)
            break
        except Exception as e:
            pass
    cl = CommandLineMode(dimension_int)
    line = ""
    while True:
        line = input()
        if line == 'exit':
            break
        cl.interpret(line)
