"""
Main application class definition for the Evo app.
Manages starting and shutdown as well as putting
the environment in place, spawns and main evo
logic.
"""
import logging
from threading import Timer


class App(Timer):
    def __init__(self, config, environment_dict):
        if not config:
            raise ValueError
        self._timer = None
        self.logger = logging.getLogger(config["app"]["name"] + " logger")
        self.logger.info("Starting app configuration")
        self.default_environment_config = config["environment"]
        self.env_dict = environment_dict
        self.name = config["app"]["name"]
        self.runtime = 0.0
        self.tick_interval = config["app"]["tick_interval"]
        self.logger.info("Ended app configuration")

    def spawn_environment(self, environment, duration, size):
        env = self.env_dict.get(environment)
        new_env = env(self.name, duration, size)
        self.__setattr__("environment", new_env)

    def run(self):
        if self.denvironment:
            while self.runtime <= float(self.environment.duration):
                self.runtime += 1
        else:
            self.logger.exception(msg="No environment to run. Spawn environment first.")
            raise AttributeError

    def tick(self):
        pass
