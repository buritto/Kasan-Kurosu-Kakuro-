import unittest
from cell import Cell
from cell_type import CellType


class CellTest(unittest):

    def test_get_value(self):
        value = 10
        cell = Cell(CellType.PLAY, value)
        self.assertEqual(value, cell.get_value())

    def test_get_type(self):
        type = CellType.NO_ACTIVE
        cell = Cell(type)
        self.assertEquale(type, cell.get_type())

    def test_get_rule(self):
        rule_row = 10
        rule_column = 10
        cell = Cell(CellType.RULES, column_rule=rule_column, row_rule=rule_row)
        self.assertEquale([rule_row, rule_column], cell.get_rules())
