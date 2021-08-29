import math
from vector import Vector


def exp(x):
    return math.exp(x)


def linear(x):
    return x


def sigmoid(x):
    if str(x).isdigit():
        return 1.0 / (1 + exp(-x))
    elif isinstance(x, Vector):
        for index in range(0, x.size):
            x[index] = sigmoid(x[index])
    else:
        ValueError("Unsupported value type {}".format(type(x)))


def tanh(x):
    if str(x).isdigit():
        return 1.0 - 2 * exp(-x) / (1 + exp(x))
    elif isinstance(x, Vector):
        for index in range(0, x.size):
            x[index] = tanh(x[index])
    else:
        ValueError("Unsupported value type {}".format(type(x)))


def relu(x):
    if str(x).isdigit():
        return x if x > 0.0 else 0.0
    elif isinstance(x, Vector):
        for index in range(0, x.size):
            x[index] = relu(x[index])
    else:
        ValueError("Unsupported value type {}".format(type(x)))


def leak_relu(x, _alpha):
    if str(x).isdigit():
        return x if x > 0.0 else _alpha * x
    elif isinstance(x, Vector):
        for index in range(0, x.size):
            x[index] = leak_relu(x[index], _alpha)
    else:
        ValueError("Unsupported value type {}".format(type(x)))


def elu(x, _alpha):
    if str(x).isdigit():
        return x if x > 0.0 else _alpha * (exp(x) - 1)
    elif isinstance(x, Vector):
        for index in range(0, x.size):
            x[index] = elu(x[index], _alpha)
    else:
        ValueError("Unsupported value type {}".format(type(x)))


def softmax(x):
    if not isinstance(x, Vector):
        return [0.0]
    else:
        value_sum = 0.0
        for index in range(0, x.size):
            value_sum += exp(x[index])
        values = []
        for index in range(0, x.size):
            values.append(exp(x[index]) / value_sum)
        return values


def activate_map(_activate):
    activates = set()
    activates.add("sigmoid")
    activates.add("tanh")
    activates.add("relu")
    activates.add("leak_relu")
    activates.add("elu")
    activates.add("softmax")
    activates.add("linear")
    if _activate in activates:
        return eval(_activate)
    else:
        return None
