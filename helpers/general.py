"""
General purpose helper functions.
"""
import os
from configparser import RawConfigParser
from pathlib import Path
from timeit import default_timer as timer


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


def time_func_perf(func, func_args=None, func_kwargs=None) -> float:
    """
    Return the time elapsed between start and end, calling a func in
    between them.
    :param func: function to be called
    :param func_args: arguments to be passed to the function
    :param func_kwargs: keyword arguments to passed to the function
    :return: time in fractional seconds
    """
    if func_args and func_kwargs:
        start = timer()
        func(*func_args, **func_kwargs)
        stop = timer()
        return stop - start

    if func_args and not func_kwargs:
        start = timer()
        func(*func_args)
        stop = timer()
        return stop - start

    if func_kwargs and not func_args:
        start = timer()
        func(**func_kwargs)
        stop = timer()
        return stop - start

    if not func_args and not func_kwargs:
        start = timer()
        func()
        stop = timer()
        return stop - start
