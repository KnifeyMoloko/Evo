"""This is the app factory file. It should run the app proper and
return in to the orchestration file main.py"""

import logging
from .evo.evo import App


def create_app(cfg):
    """

    :param cfg: a config dict passed by main.py
    :return: application instance
    """

    logging.info("Creating App instance")

    # create app instance and return it
    app = App(cfg)
    return app
