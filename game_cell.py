import cell_type


class Cell:

    def __init__(self, type_cell, value=0, row_rule=-1, column_rule=-1, length_row=0, length_column=0):
        self._type_cell = type_cell
        self._value = value
        self._row_rule = row_rule
        self._column_rule = column_rule
        self._length_row = length_row
        self._length_column = length_column

    def get_value(self):
        return self._value

    def get_type(self):
        return self._type_cell

    def get_rules(self):
        return [self._row_rule, self._column_rule]

    def is_rules(self):
        return self._type_cell == cell_type.CellType.RULES

    def get_length_row(self):
        return self._length_row

    def gey_length_column(self):
        return self._length_column
