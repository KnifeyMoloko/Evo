"""
This is the app factory file. It should run the app proper and
return in to the orchestration file main.py
"""
import logging
from .evo.evo import App
from .environment import environments


def create_app(cfg):
    """
    Instantiate an app with the given configuration.
    :param cfg: a config dict passed by main.py
    :return: application instance
    """

    logging.info("Creating App instance")

    # create app instance and return it
    app = App(cfg, environments)
    return app
