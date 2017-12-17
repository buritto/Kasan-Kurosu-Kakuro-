from tkinter import *
from game_field import GameField
from functools import partial
from game_cell import Cell
from cell_type import CellType
import kakuro_exxception as exc
from PIL import ImageTk
from PIL import Image, ImageDraw
import os
from solver import Solver
from tkinter import messagebox


class GUI:
    def __init__(self, root, dimension):
        self.root = root
        self.dimension = dimension
        self.img_for_button = PhotoImage(file=os.path.join(os.getcwd(), 'img', 'cell.gif'))
        self.list_button = []
        self.size_button = 64
        self.all_img = []
        self.draw_menu()
        self.root.mainloop()

    def draw_field(self):
        for x in range(0, self.dimension):
            line_button = []
            for y in range(0, self.dimension):
                line_button.append(Button(self.root))
                line_button[y]['command'] = partial(self.open_setting_window, x, y)
                line_button[y]['image'] = self.img_for_button
                line_button[y].grid(row=x, column=y)
            self.list_button.append(line_button)

    def open_setting_window(self, x, y):
        setting_root = Tk()
        self.setting_new_root(setting_root, x, y)

    def setting_new_root(self, setting_root, x, y):
        width = 10
        height = 2
        row_label = Label(setting_root, width=width, height=height, text="Row")
        column_label = Label(setting_root, width=width, height=height, text="Column")
        sum_label = Label(setting_root, width=width, height=height, text="Sum")
        length_label = Label(setting_root, width=width, height=height, text="Length")
        sum_row = Entry(setting_root, width=width)
        sum_column = Entry(setting_root, width=width)
        length_row = Entry(setting_root, width=width)
        length_column = Entry(setting_root, width=width)
        apply = Button(setting_root, width=width, height=height, text='Apply')
        apply['command'] = partial(self.put_cell, sum_row, length_row, sum_column, length_column, x, y, setting_root)
        cancel = Button(setting_root, width=width, height=height, text='Cancel')
        cancel['command'] = partial(self.close_window, setting_root)
        row_label.grid(row=1, column=0)
        column_label.grid(row=2, column=0)
        sum_label.grid(row=0, column=1)
        length_label.grid(row=0, column=2)
        sum_row.grid(row=1, column=1)
        sum_column.grid(row=2, column=1)
        length_row.grid(row=1, column=2)
        length_column.grid(row=2, column=2)
        apply.grid(row=3, column=0)
        cancel.grid(row=3, column=2)
        setting_root.mainloop()

    def close_window(self, side_root):
        side_root.destroy()
        side_root.quit()

    def put_cell(self, sum_row, length_row, sum_column, length_column, x, y, root):
        try:
            row_rule = int(sum_row.get())
            column_rule = int(sum_column.get())
            row = int(length_row.get())
            column = int(length_column.get())
        except Exception as e:
            self.throw_exception('Argument error', 'One or more argument are NaN', root)
            return
        if not self.check_arguments(row_rule, column_rule, row, column, x, y, root):
            return
        self.close_window(root)
        print('Correct')
        cell = Cell(CellType.RULES, row_rule=row_rule, column_rule=column_rule, length_row=row, length_column=column)
        self.game_field.init_cell(x, y, cell)
        self.redraw()

    def check_arguments(self, row_rule, column_rule, row, column, x, y, setting_root):
        if column_rule > 45 or row_rule > 45:
            self.throw_exception('Argument error', 'The amount can not exceed 45', setting_root)
            return False
        if row_rule < 0 or column_rule < 0 or row < 0 or column < 0:
            self.throw_exception('Argument error', 'One or more argument less zero', setting_root)
            return False
        if x + column >= self.dimension:
            self.throw_exception('Argument error', 'Row length too large', setting_root)
            return False
        if y + row >= self.dimension:
            self.throw_exception('Argument error', 'Column length too large', setting_root)
            return False
        return True

    def redraw(self):
        for x in range(0, self.dimension):
            for y in range(0, self.dimension):
                if self.game_field.field[x][y].is_rules():
                    row = self.game_field.field[x][y].get_rules()[0]
                    column = self.game_field.field[x][y].get_rules()[1]
                    img = self.get_image_for_button(row, column)
                    self.list_button[x][y]['image'] = img
                if self.game_field.field[x][y].get_type() == CellType.PLAY:
                    value = self.game_field.field[x][y].get_value()
                    self.list_button[x][y]['image'] = self.get_image_value_cell(value)
        self.root.update()

    def get_image_for_button(self, row, column):
        img = Image.new('RGB', (self.size_button, self.size_button), 'white')
        drawer = ImageDraw.Draw(img)
        if row > 0:
            to_str = str(int(row))
            numbers = self.count_number(row)
            drawer.text([self.size_button // 2, 0], text=to_str[0:numbers], fill='black', align='center')
        if column > 0:
            to_str = str(int(column))[0:3]
            numbers = self.count_number(column)
            drawer.text([0, self.size_button // 2], text=to_str[0:numbers], fill='black')
        drawer.line([0, 0, self.size_button, self.size_button], 'black')
        img.save("res.bmp")
        p_img = ImageTk.PhotoImage(img)
        self.all_img.append(p_img)
        return p_img

    def count_number(self, n):
        i = 0
        while n > 0:
            n = n // 10
            i += 1
        return i

    def get_image_value_cell(self, value):
        img = Image.new('RGB', (self.size_button, self.size_button), 'white')
        drawer = ImageDraw.Draw(img)
        drawer.text([self.size_button // 2, self.size_button // 2],
                    text=str(value), fill='black', align='center')
        p_img = ImageTk.PhotoImage(img)
        self.all_img.append(p_img)
        return p_img

    def draw_menu(self):
        menu_bar = Menu(self.root)
        file_menu = Menu(menu_bar)
        file_menu.add_command(label='Create new kakuro', command=self.start_setting)
        menu_bar.add_cascade(label='File', menu=file_menu)
        solve_menu = Menu(menu_bar, tearoff=0)
        solve_menu.add_command(label='Solve', command=self.solve)
        menu_bar.add_cascade(label="Solution", menu=solve_menu)
        self.root.config(menu=menu_bar)

    def solve(self):
        solver = Solver(self.game_field)
        solution = solver.solve()
        if solution is None:
            return
        self.game_field.field = solution
        self.redraw()

    def start_setting(self):
        start_setting_root = Tk()
        start_setting_root.title('Create new kakuro')
        width = 15
        height = 2
        label_d = Label(start_setting_root, text='Select the dimension', width=width, height=height)
        entry_d = Entry(start_setting_root, width=width)
        create_button = Button(start_setting_root, width=width, height=height, text='Create')
        cancel = Button(start_setting_root, width=width, height=height, text='Cancel')
        cancel['command'] = partial(self.close_window, start_setting_root)
        create_button['command'] = partial(self.start_new_kakuro, entry_d, start_setting_root)
        label_d.grid(row=0, column=0, padx=10)
        entry_d.grid(row=0, column=2)
        create_button.grid(row=1, column=0)
        cancel.grid(row=1, column=2)
        start_setting_root.mainloop()

    def start_new_kakuro(self, entry_dimension, start_root):
        try:
            dimension = int(entry_dimension.get())
        except Exception as e:
            self.throw_exception('Incorrect dimension', 'Dimension is NaN', start_root)
            return
        if dimension < 1:
            self.throw_exception('Incorrect dimension', 'Dimension is less zero', start_root)
            return
        if dimension > 10:
            self.throw_exception('Incorrect dimension', 'Dimension too large', start_root)
            return
        self.game_field = GameField(dimension, dimension)
        self.dimension = dimension
        self.all_img.clear()
        self.list_button.clear()
        self.draw_field()
        self.root.geometry("{0}x{1}".format(dimension * 70, dimension * 70))
        self.root.update()
        self.close_window(start_root)

    def throw_exception(self, title, msg, start_root):
        messagebox.showerror(title, msg)
        self.close_window(start_root)


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    a = GUI(root, 4)

