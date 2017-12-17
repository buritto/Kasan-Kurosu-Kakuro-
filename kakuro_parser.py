from game_field import Cell
from cell_type import CellType
import kakuro_exxception as exc


class Parser:

    def parse(self, file_name):
        all_cells = []
        with open(file_name, 'r') as f:
            for line in f.readlines():
                despiralized_cell = line
                if len(line.split('|')) != 1:
                    all_cells.append(self.get_cell(despiralized_cell, file_name))
                else:
                    if len(line.replace("\n", "")) != 0 and len(all_cells) == 0:
                        all_cells.append(int(line.replace("\n", "")))
        return all_cells

    def get_cell(self, despiralized_cell, file_name):
        frames = despiralized_cell.split('|')
        try:
            pos_x = self.get_frame(frames[0])
            pos_y = self.get_frame(frames[1])
            row_sum = self.get_frame(frames[2])
            row_length = self.get_frame(frames[3])
            column_sum = self.get_frame(frames[4])
            column_length = self.get_frame(frames[5])
        except Exception as e:
            raise exc.IncorrectFileArgument('Incorrect_argument in file {0}'.format(file_name))
        cell = Cell(CellType.RULES, row_rule=row_sum, column_rule=column_sum,
                    length_row=row_length, length_column=column_length)
        return {tuple([pos_x, pos_y]): cell}

    def get_frame(self, frame):
        return int(frame.rstrip().lstrip().replace('\n', '').replace('\t', ''))
