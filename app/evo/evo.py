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
        self.default_environment_config = config["environment"]
        self.name = config["app"]["name"]
        self.tick = config["app"]["name"]
        self.logger.info("Ended app configuration")

    def spawn_environment(self, environment, duration, size):
        self.__setattr__("environment", {"size": size})
