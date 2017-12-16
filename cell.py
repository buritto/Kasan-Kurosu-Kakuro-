class Cell:

    def __init__(self, type_cell, value=0, row_rule=0, column_rule=0):
        self._type_cell = type_cell
        self._value = value
        self._row_rule = row_rule
        self._column_rule = column_rule

    def get_value(self):
        return self._value

    def get_type(self):
        return self._type_cell

    def get_rules(self):
        return [self._row_rule, self._column_rule]
