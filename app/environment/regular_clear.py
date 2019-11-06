from .base import Environment


class RegularClearEnvironment(Environment):
    def __init__(self, name, duration, size):
        super(RegularClearEnvironment, self).__init__(name, duration, size)
