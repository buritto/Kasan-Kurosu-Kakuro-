import argparse
from tkinter import *
from graphical_mode import GUI
from command_line_mode import CommandLineMode
from kakuro_parser import Parser
from painter import Painter
from game_field import GameField
from solver import Solver
import kakuro_exxception as exc


def GUI_main():
    root = Tk()
    root.geometry('800x600')
    a = GUI(root, 4)


def com_line_main():
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


def get_solve(input_file, output_file):
    parser = Parser()
    try:
        pairs = parser.parse(input_file)
    except exc.IncorrectFileArgument as e:
        print('Incorrect file{0}'.format(input_file))
        return
    except Exception as fe:
        print('Unrecognized error in file')
        return
    dimension = pairs[0]
    game = GameField(dimension, dimension)
    for cells in pairs[1:]:
        for key in cells.keys():
            game.init_cell(key[0], key[1], cells[key])
    solver = Solver(game)
    painter = Painter(64)
    try:
        solution = solver.solve()
    except exc.KakuroNotSolution as e:
        print('Not solution')
        return
    painter.paint(solution, output_file, dimension)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gui', help="Start kakuro editor in graphics user interface", action='store_true')
    parser.add_argument('--com_line', help="Start kakuro editor in command-line mode", action='store_true')
    parser.add_argument('--solve', metavar=("input_file", "output_file"),
                        help='from input.kk get image solution of kakuro', nargs=2)
    args = parser.parse_args()
    if args.gui:
        GUI_main()

    if args.com_line:
        com_line_main()

    if args.solve:
        get_solve(args.solve[0], args.solve[1])
