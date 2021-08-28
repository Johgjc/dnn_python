import random
import os
from matrix import Matrix


class Vector:
    def __init__(self):
        self.__size = 0
        self.__value = []

    def __len__(self):
        return self.__size

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(self.__value)

    def __getattr__(self, _item):
        if _item == "size":
            return self.__size

    def __getitem__(self, _index: int):
        if _index >= self.__size or _index < 0:
            raise ValueError("Max Index is {}, param is {}".format(self.__size, _index))
        return self.__value[_index]

    def __setitem__(self, _index: int, _value: float):
        if _index >= self.__size or _index < 0:
            raise ValueError("Max index is {}, param is {}".format(self.__size, _index))
        self.__value[_index] = _value

    def __mul__(self, _other):
        if not isinstance(_other, Vector):
            raise ValueError("Wrong param type, a vector or matrix param is needed")
        if not _other.size == self.__size:
            raise ValueError("Different size between two vectors with {} and {}".format(_other.size, self.__size))
        result = 0.0
        for index in range(0, self.__size):
            result += self.__value[index] * _other[index]
        return result

    def __add__(self, _other):
        if not isinstance(_other, Vector):
            raise ValueError("Wrong param type, a vector param is needed")
        if not _other.size == self.__size:
            raise ValueError("Different size between two vector with {} and {}".format(_other.size, self.__size))
        result = Vector.generate(self.__size, False, 0)
        for index in range(0, self.__size):
            result[index] = _other[index] + self.__value[index]
        return result

    def __sub__(self, _other):
        if not isinstance(_other, Vector):
            raise ValueError("Wrong param type, a vector param is needed")
        if not _other.size == self.__size:
            raise ValueError("Different size between two vectors with {} and {}".format(_other.size, self.__size))
        result = Vector.generate(self.__size, False, 0)
        for index in range(0, self.__size):
            result[index] = self.__value[index] - _other[index]
        return result

    def resize(self, _length: int):
        if _length < 0:
            raise ValueError("Vector size should bigger than 0")
        elif _length < self.__size:
            self.__value = self.__value[:_length - self.__size]
        elif _length == self.__size:
            return
        else:
            for index in range(self.__size, _length):
                self.__value.append(0)
        self.__size = _length

    def get(self, _index: int):
        return self.__getitem__(_index)

    def set(self, _index: int, _value: float):
        return self.__setitem__(_index, _value)

    def append(self, _value: float):
        self.__value.append(_value)
        self.__size += 1

    def load(self, _filename):
        if not os.path.isfile(_filename):
            raise ValueError("No such file or directory {}".format(_filename))
        tmp_values = []
        with open(_filename, 'r') as f:
            for line in f:
                tmp_values = line.split(' ')
        for value in tmp_values:
            self.__value.append(float(value))
        self.__size = len(self.__value)
        return True, _filename

    def dump(self, _filename):
        filename = os.path.abspath(_filename)
        file_dir = os.path.dirname(filename)
        if not os.path.isdir(file_dir):
            raise ValueError("No such file or directory {}".format(file_dir))
        dump_file = open(filename, 'w')
        tmp_values = []
        for value in self.__value:
            tmp_values.append(str(value))
        dump_file.write(" ".join(tmp_values))
        dump_file.close()
        return True, filename

    @staticmethod
    def clone(_other):
        if not isinstance(_other, Vector):
            raise ValueError("Wrong value type {}, a vector is needed".format(type(_other)))
        vector = Vector()
        vector.resize(_other.size)
        for index in range(0, vector.size):
            vector[index] = _other.index
        return vector

    @staticmethod
    def generate(_length, _random_init=False, _default_value=0.0):
        if not _length > 0:
            raise ValueError("Vector length must bigger than 0")
        vector = Vector()
        if _random_init:
            for index in range(0, _length):
                vector.__value.append(random.random())
        else:
            for index in range(0, _length):
                vector.__value.append(_default_value)
        vector.__size = _length
        return vector


def clone(_other):
    return Vector.clone(_other)


def load(_filename):
    return Vector().load(_filename)


def generate(_length, _random_init=False, _default_value=0.0):
    return Vector.generate(_length, _random_init, _default_value)


def test_vector():
    v1 = Vector()
    v1.append(1.0)
    v1.append(2.0)
    print("test_v1: {}".format(v1))
    print("test_v1[0]: {}".format(v1[0]))
    print("test_v1_len: {}".format(len(v1)))
    print("test_v1_size_attr: {}".format(v1.size))

    v2 = Vector()
    v2.append(3.0)
    v2.append(4.0)
    print("test_v2: {}".format(v2))
    print("test_v1*v2: {}".format(v1 * v2))
    print("test_v1+v2: {}".format(v1 + v2))
    v2[1] = 2.0
    print("test_v2_setitem: {}".format(v2))

    v3 = Vector.generate(3, True)
    print("test_generate_v3: {}".format(v3))
    print("test_dump_v3: {}", v3.dump("./input_vector.text"))

    v4 = Vector()
    print("test_load_v4: {}".format(v4.load("./input_vector.text")))
    print("test_v4: {}".format(v4))


if __name__ == '__main__':
    test_vector()
