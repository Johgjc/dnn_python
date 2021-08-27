import random
import os
from vector import Vector


class Matrix:
    def __init__(self):
        self.__row = 0
        self.__col = 0
        self.__value = []

    def __str__(self):
        if self.__row == 0:
            return ""
        result = ""
        for row in self.__value:
            result += str(row)
            result += "\n"
        result = result[:-1]
        return result

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, _item):
        if _item == "row":
            return self.__row
        elif _item == "col":
            return self.__col

    def __getitem__(self, _position):
        row, col = _position
        if row >= self.__row or row < 0:
            raise ValueError("Max row index is {}, param is {}".format(self.__row, row))
        if col >= self.__col or col < 0:
            raise ValueError("Max col index is {}, param is {}".format(self.__col, col))
        return self.__value[row][col]

    def __setitem__(self, _position, _value):
        row, col = _position
        if row >= self.__row or row < 0:
            raise ValueError("Max row index is {}, param is {}".format(self.__row, row))
        if col >= self.__col or col < 0:
            raise ValueError("Max col index is {}, param is {}".format(self.__col, col))
        self.__value[row][col] = _value

    def __mul__(self, _other):
        if isinstance(_other, Matrix):
            if not _other.row == self.__col:
                raise ValueError("Size of two matrices not match : {} and {}".format(_other.row, self.__col))
            else:
                matrix = Matrix.generate(self.__row, _other.col, False, 0.0)
                for row in range(0, self.__row):
                    for col in range(0, _other.col):
                        for index in range(0, self.__col):
                            matrix[row, col] += self.get(row, index) * _other.get(index, col)

                return matrix

        elif isinstance(_other, Vector):
            if not _other.size == self.__col:
                raise ValueError("Size of vector and matrix not match: {} and {}".format(_other.size, self.__col))
            else:
                vector = Vector.generate(self.__row, False, 0.0)
                for row in range(0, self.__row):
                    for col in range(0, self.__col):
                        vector[row] += self.get(row, col) * _other.get(col)
                return vector
        elif str(_other).isdigit():
            matrix = Matrix.generate(self.__row, self.__col, False, 0.0)
            for row in range(0, self.__row):
                for col in range(0, self.__col):
                    matrix = self.get(row, col) * _other

            return matrix
        else:
            raise ValueError("Wrong param type, a matrix, vector or digit type param is needed")

    def __add__(self, _other):
        if not isinstance(_other, Matrix):
            raise ValueError("Wrong param type, a matrix type param is needed")
        if not _other.row == self.__row:
            raise ValueError("Different rwo size between two matrices {} and {}".format(_other.row, self.__row))
        if not _other.__col == self.__col:
            raise ValueError("Different col size between two matrices {} and {}".format(_other.col, self.__col))
        matrix = Matrix.generate(self.__row, self.__col, False, 0.0)
        for row in range(0, self.__row):
            for col in range(0, self.__col):
                matrix[row, col] = self.__value[row][col] - _other[row, col]
        return matrix

    def resize(self, _row, _col):
        if _row <= 0 or _col <= 0:
            raise ValueError("Row and col must bigger than 0 which inputs are row: {} and col: {}"
                             .format(self.__row, self.__col))
        if _row < self.__row:
            self.__value = self.__value[:_row - self.__row]
        elif _row > self.__row:
            for row in range(self.__row, _row):
                tmp_col = []
                for col in range(0, self.__col):
                    tmp_col.append(0.0)
                self.__value.append(tmp_col)
        self.__row = _row
        if _col < self.__col:
            for row in range(0, self.__row):
                for col in range(self.__col, _col):
                    self.__value[row].append(0.0)
        elif _col > self.__col:
            for row in range(0, self.__row):
                for col in range(self.__col, _col):
                    self.__value[row].append(0.0)
        self.__col = _col

    def set(self, _row, _col, _value):
        return self.__setitem__((_row, _col), _value)

    def get(self, _row, _col):
        return self.__getitem__((_row, _col))

    def transform(self):
        if self.__row == 0:
            return Matrix()
        matrix = Matrix.generate(self.__col, self.__row, False, 0.0)
        for row in range(0, self.__row):
            for col in range(0, self.__col):
                matrix[col, row] = self.get(row, col)
        return matrix

    def load(self, _filename):
        if not os.path.isfile(_filename):
            raise ValueError("No such file or directory {}".format(_filename))
        with open(_filename, 'r') as f:
            for line in f:
                tmp_values = []
                tmp_line = line.split(' ')
                for value in tmp_line:
                    tmp_values.append(float(value))
                self.__value.append(tmp_values)
        self.__row = len(self.__value)
        self.__col = len(self.__value[0])
        return True, _filename

    def dump(self, _filename):
        filename = os.path.abspath(_filename)
        file_dir = os.path.dirname(filename)

        if not os.path.isdir(file_dir):
            raise ValueError("No such file or directory {}".format(_filename))
        dump_file = open(filename, 'w')
        for row in self.__value:
            tmp_values = []
            for value in row:
                tmp_values.append(str(value))
            dump_file.write(" ".join(tmp_values))
            dump_file.write("\n")
        dump_file.close()
        return True, filename

    @staticmethod
    def clone(_other):
        if not isinstance(_other, Matrix):
            raise ValueError("Wrong value type {}, a matrix is needed".format(type(_other)))
        matrix = Matrix()
        matrix.resize(_other.row, _other.col)
        for row in range(0, _other.row):
            for col in range(0, _other.col):
                matrix[row, col] = _other[row, col]
        return matrix

    @staticmethod
    def generate(_row, _col, _random_init=False, _default_value=0.0):
        if not _row > 0:
            raise ValueError("Matrix row count must bigger than 0")
        if not _col > 0:
            raise ValueError("Matrix col count must bigger than 0")
        matrix = Matrix()
        matrix.resize(_row, _col)
        if _random_init:
            for row in range(0, _row):
                for col in range(0, _col):
                    matrix.set(row, col, random.random())
        else:
            for row in range(0, _row):
                for col in range(0, _col):
                    matrix.set(row, col, _default_value)
        return matrix


def clone(_other):
    return Matrix.clone(_other)


def load(_filename):
    return Matrix().load(_filename)


def generate(_row, _col, _random_init=False, _default_value=0.0):
    return Matrix.generate(_row, _col, _random_init, _default_value)


def test_matrix():
    matrix1 = Matrix()
    matrix1.resize(2, 2)
    matrix1.set(0, 0, 0)
    matrix1.set(0, 1, 1)
    matrix1.set(1, 0, 2)
    matrix1.set(1, 1, 3)
    print("test_matrix_set")
    print(matrix1)
    print("test_matrix_get")
    print(matrix1[1, 1])
    print("test_matrix_row")
    print(matrix1.row)
    print("test_matrix_col")
    print(matrix1.col)
    print("test_matrix_transform")
    print(matrix1.transform())
    matrix1.transform()

    matrix2 = Matrix.generate(2, 2, False, 0.0)
    matrix2[0, 0] = 1
    matrix2[0, 1] = 2
    matrix2[1, 0] = 3
    matrix2[1, 1] = 4
    print("test_matrix_gen")
    print(matrix2)
    print("test_matrix_add")
    print(matrix1 + matrix2)
    print("test_matrix_mul")
    print(matrix1 * matrix2)

    matrix3 = Matrix.generate(4, 4, True)
    print("test_matrix_dump: {}".format(matrix3.dump("./input_matrix.text")))
    print(matrix3)
    matrix4 = Matrix()
    print("test_matrix_load: {}".format(matrix4.load("./input_matrix.text")))
    print(matrix4)


if __name__ == '__main__':
    test_matrix()
