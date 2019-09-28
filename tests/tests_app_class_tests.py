"""These are the test classes for the Evo app itself. Mostly
basic stuff: does it exit gracefully, does it configure and
init as expected etc.
"""

import unittest
import os
from app import create_app


class AppClass(unittest.TestCase):
    def setUp(self):
        from pathlib import Path
        from configparser import RawConfigParser
        os.environ['APP_ENV'] = 'test'
        root = Path('.') / os.getcwd()
        cfg_path = root / 'config' / '{}.ini'.format(os.environ.get('APP_ENV'))
        cfg_parser = RawConfigParser()
        cfg = cfg_parser.read(cfg_path)
        cfg_dict = {x: dict(cfg_parser.items(x)) for x in cfg_parser.sections()}
        self.cfg = cfg_dict

    def tearDown(self):
        os.environ.pop('APP_ENV')

    def test_app_is_not_none(self):
        self.assertTrue(create_app(
            {"app": {"name": "not_really_an_app"},
             "environment": {"duration": 5, "size": 4,
                             "tick": 10}}) is not None)

    def test_app_factory_returns_object(self):
        self.assertIsNotNone(create_app(self.cfg))

    def test_app_throws_error_on_no_config(self):
        with self.assertRaises(ValueError):
            create_app("")

    def test_app_has_name(self):
        app = create_app(self.cfg)
        self.assertTrue(app.name)

    def test_app_has_duration(self):
        app = create_app(self.cfg)
        self.assertTrue(app.duration)

    def test_app_has_size(self):
        app = create_app(self.cfg)
        self.assertTrue(app.size > 0)

    def test_app_has_tick(self):
        app = create_app(self.cfg)
        self.assertTrue(app.tick > 0)
