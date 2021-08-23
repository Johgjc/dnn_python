import random
import os


class Vector:
    def __init__(self):
        self.size = 0
        self.value = []

    def __mul__(self, _other):
        assert isinstance(_other, Vector), "Wrong param type, a vector param is needed."
        assert _other.size == self.size, ("Different size between two vectors with size {} and {}"
                                          .format(_other.size, self.size))
        result = 0.0
        for index in range(0, self.size):
            result += self.value[index] * _other.value[index]
        return result

    def __add__(self, _other):
        assert isinstance(_other, Vector), "Wrong param type, a vector param is needed."
        assert _other.size == self.size, ("Different size between two vectors with size {} and {}"
                                          .format(_other.size, self.size))
        for index in range(0, self.size):
            self.value[index] += _other.value[index]
        return self

    def get(self, _index):
        assert _index >= self.size, "Max index is {}, param is {}".format(self.size, _index)
        return self.value[_index]

    def generate(self, _length, _random_init=False, _default_value=0.0):
        self.value = []
        self.size = 0
        assert _length > 0, "Vector length must bigger than 0!"
        if _random_init:
            for index in range(0, _length):
                self.value.append(random.random())
        else:
            for index in range(0, _length):
                self.value.append(_default_value)
        self.size = _length
        return self

    def load(self, _filename):
        assert os.path.isfile(_filename), "No such file or directory {}".format(_filename)
        self.value = []
        self.size = 0
        tmp_values = []
        with open(_filename, 'r') as f:
            for line in f:
                tmp_values = line.split(' ')
        for value in tmp_values:
            self.value.append(float(value))
        self.size = len(self.value)

    def dump(self, _filename):
        assert os.path.isfile(os.path.abspath(_filename)), ("No such file or directory {}"
                                                            .format(os.path.abspath(_filename)))
        dump_file = open(_filename, 'w')
        tmp_values = []
        for value in self.value:
            tmp_values.append(str(value))
        dump_file.write(" ".join(tmp_values))
        dump_file.close()
