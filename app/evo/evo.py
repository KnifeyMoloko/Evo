"""
Main application class definition for the Evo app.
Manages starting and shutdown as well as putting
the environment in place, spawns and main evo
logic.
"""

import logging


class App:
    def __init__(self, config):
        if not config:
            raise ValueError
        #TODO: set up logger, name, tick value, duration, size
