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
        self.logger = logging.getLogger(config["app"]["name"] + " logger")
        self.logger.info("Starting app configuration")
        self.name = config["app"]["name"]
        self.duration = int(config["environment"]["duration"])
        self.size = int(config["environment"]["size"])
        self.tick = int(config["environment"]["tick"])
        self.logger.info("Ended app configuration")
