import random
import os
from vector import Vector


class Matrix:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.value = []

    def __mul__(self, _other):
        if isinstance(_other, Matrix):
            assert _other.row == self.col, "Size of two matrices not match: {} and {}".format(_other.row, self.col)
        elif isinstance(_other, Vector):
            assert _other.size == self.col, "Size of vector and matrix not match: {} and {}".format(_other.size,
                                                                                                    self.row)
        else:
            assert False, "Wrong param type, a matrix or vector is needed."

    def __add__(self, _other):
        assert isinstance(_other, Matrix), "Wrong param type, a matrix type param is needed."
        assert _other.row == self.row, "Different row size between two matrices {} and {}".format(_other.row, self.row)
        assert _other.col == self.col, "Different col size between two matrices {} and {}".format(_other.col, self.col)

    def rows(self):
        return self.row

    def cols(self):
        return self.col

    def get(self, _row, _col):
        assert _row >= self.row, "Max row index is {}, param is {}.".format(self.row - 1, _row)
        assert _col >= self.col, "Max col index is {}, param is {}.".format(self.col - 1, _col)
        return self.value[_row][_col]

    def transform(self):
        if self.row == 0:
            return self
        tmp_value = []
        for index in range(0, self.col):
            tmp_value.append([])
        for row in range(0, self.row):
            for col in range(0, self.col):
                tmp_value[col].append(self.value[row][col])
        self.value = tmp_value
        return self

    def generate(self, _row, _col, _random_init=False, _default_value=0.0):
        assert _row > 0, "Matrix row count must bigger than 0!"
        assert _col > 0, "Matrix col count must bigger than 0!"
        if _random_init:
            for row in range(0, _row):
                tmp_row = []
                for col in range(0, _col):
                    tmp_row.append(random.random())
                self.value.append(tmp_row)
        else:
            for row in range(0, _row):
                tmp_row = []
                for col in range(0, _col):
                    tmp_row.append(_default_value)
                self.value.append(tmp_row)
        self.row = _row
        self.col = _col
        return self

    def load(self, _filename):
        assert os.path.isfile(_filename), "No such file or directory {}".format(_filename)
        with open(_filename, 'r')as f:
            tmp_value = []
            for line in f:
                tmp_line = line.split(' ')
                for value in tmp_line:
                    tmp_value.append(float(value))
            for value in tmp_value:
                self.value.append(value)
        self.row = len(self.value)
        self.col = len(self.value[0])

    def dump(self, _filename):
        assert os.path.isfile(os.path.abspath(_filename)), ("No such file or directory {}"
                                                            .format(os.path.abspath(_filename)))
        dump_file = open(_filename, 'w')
        for row in self.value:
            tmp_values = []
            for value in row:
                tmp_values.append(str(value))
            dump_file.write(" ".join(tmp_values))
        dump_file.close()
