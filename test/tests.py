import unittest
import sys
import os
sys.path.append('C:\\Programm\\KasanKurosu\\Kasan-Kurosu-Kakuro-')

from cell_type import CellType
from game_cell import Cell
from game_field import GameField
from solver import Solver
import kakuro_exxception as exc
from kakuro_parser import Parser

class SolverTest(unittest.TestCase):
    def setUp(self):
        self.game = GameField(4, 4)
        self.game.init_cell(0, 1, Cell(CellType.RULES, column_rule=16, length_column=2))
        self.game.init_cell(0, 2, Cell(CellType.RULES, column_rule=15, length_column=3))
        self.game.init_cell(1, 0, Cell(CellType.RULES, row_rule=17, length_row=2))
        self.game.init_cell(2, 0, Cell(CellType.RULES, row_rule=15, length_row=3))
        self.game.init_cell(3, 1, Cell(CellType.RULES, row_rule=3, length_row=2))
        self.game.init_cell(1, 3, Cell(CellType.RULES, column_rule=4, length_column=2))

    def test_get_list(self):
        solver = Solver(self.game)
        expected = [self.game.field[1][1], self.game.field[1][2], self.game.field[2][1], self.game.field[2][2],
                    self.game.field[2][3], self.game.field[3][2], self.game.field[3][3]]
        solver.get_list()
        self.assertEqual (expected, solver.all_cells)

    def test_correct_solve(self):
        solver = Solver(self.game)
        self.game.field[1][1].set_value(9)
        self.game.field[1][2].set_value(8)
        self.game.field[2][1].set_value(7)
        self.game.field[2][2].set_value(5)
        self.game.field[2][3].set_value(3)
        self.game.field[3][2].set_value(2)
        self.game.field[3][3].set_value(1)
        self.assertTrue(solver.is_correct_solve())

    def test_kakuro_not_solution(self):
        game = GameField(3, 3)
        cell_column = Cell(CellType.RULES, column_rule=3, length_column=2)
        cell_row = Cell(CellType.RULES, row_rule=17, length_row=2)
        game.init_cell(0, 1, cell_column)
        game.init_cell(1, 0, cell_row)
        solver = Solver(game)
        with self.assertRaises(exc.KakuroNotSolution):
            self.assertRaises(solver.solve())


class FieldTest(unittest.TestCase):
    def test_init_put_play_cell(self):
        game = GameField(10, 10)
        cell = Cell(CellType.PLAY, value=10)
        game.init_cell(5, 5, cell)
        self.assertEqual(cell, game.field[5][5])

    def test_init_put_rule_cell_row(self):
        game = GameField(10, 10)
        cell = Cell(CellType.RULES, row_rule=10, length_row=2)
        game.init_cell(5, 5, cell)
        self.assertEqual(CellType.PLAY, game.field[5][6].get_type())
        self.assertEqual(CellType.PLAY, game.field[5][7].get_type())

    def test_init_put_rule_cell_column(self):
        game = GameField(10, 10)
        cell = Cell(CellType.RULES, column_rule=10, length_column=2)
        game.init_cell(5, 5, cell)
        self.assertEqual(CellType.PLAY, game.field[6][5].get_type())
        self.assertEqual(CellType.PLAY, game.field[7][5].get_type())


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

    def test_is_rule(self):
        c = Cell(CellType.RULES)
        self.assertTrue(c.is_rules())


class TestParser(unittest.TestCase):
    def test_get_cell(self):
        date = '0|1|0|0|16|2'
        parser = Parser()
        actual = parser.get_cell(date, 'fake_file')
        cell = Cell(CellType.RULES, row_rule=0, length_row=0, column_rule=16, length_column=2)
        expected = [16, 2]
        for key in actual:
            self.assertEqual(tuple([0, 1]), key)
            self.assertTrue(actual[key].get_length_column() in expected)
            self.assertTrue(actual[key].get_rules()[1] in expected)

    def test_parse(self):
        parser = Parser()
        actual = parser.parse('1.kk')
        list_position = []
        self.assertEqual(7, len(actual))
        for cell in actual[1:]:
            for key in cell:
                list_position.append(key)
        self.assertTrue(tuple([0, 1]) in list_position)
        self.assertTrue(tuple([0, 2]) in list_position)
        self.assertTrue(tuple([1, 0]) in list_position)
        self.assertTrue(tuple([2, 0]) in list_position)
        self.assertTrue(tuple([3, 1]) in list_position)
        self.assertTrue(tuple([1, 3]) in list_position)


if __name__ == '__main__':
    unittest.main()
