import math


def exp(x):
    return math.exp(x)


def sigmoid(x):
    return 1.0 / (1 + exp(-x))


def tanh(x):
    return 1.0 - 2 * exp(-x) / (1 + exp(x))


def relu(x):
    return x if x > 0.0 else 0.0


def leak_relu(x, _alpha):
    return x if x > 0.0 else _alpha * x


def elu(x, _alpha):
    return x if x > 0.0 else _alpha * (exp(x) - 1)


def softmax(x):
    if not isinstance(x, list):
        return [0.0]
    else:
        value_sum = 0.0
        for value in x:
            value_sum += exp(value)
        values = []
        for value in x:
            values.append(exp(value) / value_sum)
        return values


def activate_map(_activate):
    activates = set()
    activates.add("sigmoid")
    activates.add("tanh")
    activates.add("relu")
    activates.add("leak_relu")
    activates.add("elu")
    activates.add("softmax")
    if _activate in activates:
        return eval(_activate)
    else:
        return None
