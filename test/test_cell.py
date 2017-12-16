import unittest
import sys
print(sys.path)
sys.path.append('C:\\Programm\\KasanKurosu\\Kasan-Kurosu-Kakuro-')

from cell_type import CellType
from game_cell import Cell


class CellTest(unittest.TestCase):

    def test_get_value(self):
        value = 10
        c = Cell(CellType.PLAY, value)
        self.assertEqual(value, c.get_value())

    def test_get_type(self):
        type = CellType.NO_ACTIVE
        c = Cell(type)
        self.assertEqual(type, c.get_type())

    def test_get_rule(self):
        rule_row = 10
        rule_column = 10
        c = Cell(CellType.RULES, column_rule=rule_column, row_rule=rule_row)
        self.assertEqual([rule_row, rule_column], c.get_rules())


if __name__ == '__main__':
    unittest.main()
