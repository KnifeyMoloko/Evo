"""These are the test classes for the Evo app itself. Mostly
basic stuff: does it exit gracefully, does it configure and
init as expected etc.
"""
import unittest
import os
from app import create_app
from helpers.general import get_config, time_func_perf


class AppClass(unittest.TestCase):
    def setUp(self):
        os.environ['APP_ENV'] = 'test'
        self.cfg = get_config().get("cfg")

    def tearDown(self):
        os.environ.pop('APP_ENV')

    def test_app_is_not_none(self):
        self.assertIsNotNone(create_app(
            {"app": {"name": "not_really_an_app"},
             "environment": {"duration": 5, "size": 4,
                             "tick": 10}}))

    def test_app_factory_returns_object(self):
        self.assertIsNotNone(create_app(self.cfg))

    def test_app_throws_error_on_no_config(self):
        with self.assertRaises(ValueError):
            create_app("")

    def test_app_has_name(self):
        app = create_app(self.cfg)
        self.assertTrue(app.name)

    def test_app_has_tick(self):
        self.assertTrue(create_app(self.cfg).tick)

    def test_app_has_environment_config(self):
        self.assertTrue(create_app(self.cfg).default_environment_config)

    def test_app_is_running_until_duration_condition_is_met(self):
        app = create_app(self.cfg)
        duration = float(app.default_environment_config["duration"])
        app.spawn_environment(environment="regular_clear",
                              duration=app.default_environment_config["duration"],
                              size=app.default_environment_config["size"])
        runtime = time_func_perf(func=app.run)
        self.assertGreaterEqual(duration, runtime, msg="Runtime exceeded duration attribute value")

    #TODO delegate run method to a thread to allow for stop signal listening
