from .base import Environment


class RegularClearEnvironment(Environment):
    def __init__(self, name, duration, size):
        super().__init__(name, duration, size)
