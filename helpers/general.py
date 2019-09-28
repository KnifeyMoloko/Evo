"""
General purpose helper functions.
"""
import os
from configparser import RawConfigParser
from pathlib import Path


def get_config():
    """
    Looks for a config file using the APP_ENV environment
    variable and reads in the configuration as a dict.
    :return: dict(cfg dict, root, cfg_path)
    """
    # set root directory for the app (this directory, that is)
    root = Path.cwd()

    # setup configuration file path using the APP_ENV environment variable
    cfg_path = root / 'config' / '{}.ini'.format(os.environ.get('APP_ENV'))
    cfg_parser = RawConfigParser()

    # read .ini file for the appropriate app setup (dev, prod or test)
    cfg_parser.read(cfg_path)

    # create a dict with the config
    cfg_dict = {x: dict(cfg_parser.items(x)) for x in cfg_parser.sections()}
    return {"cfg": cfg_dict, "root": root, "cfg_path": cfg_path}
