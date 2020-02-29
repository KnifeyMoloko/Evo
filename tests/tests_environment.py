import os
import unittest
from random import randint
from random import random
from helpers.general import get_config
from app import create_app


class EnvironmentConfigTests(unittest.TestCase):
    def setUp(self):
        os.environ['APP_ENV'] = 'test'
        self.cfg = get_config().get("cfg")

    def tearDown(self):
        os.environ.pop('APP_ENV')

    def test_env_cfg_has_duration(self):
        app = create_app(self.cfg)
        duration = app.default_environment_config.get("duration")
        self.assertTrue(duration)

    def test_env_cfg_has_has_size(self):
        app = create_app(self.cfg)
        size = int(app.default_environment_config.get("size"))
        self.assertTrue(size)


class EnvironmentClassSetupTests(unittest.TestCase):
    def setUp(self):
        os.environ['APP_ENV'] = 'test'
        self.cfg = get_config().get("cfg")

    def tearDown(self):
        os.environ.pop('APP_ENV')

    def test_app_spawns_environment(self):
        app = create_app(self.cfg)
        app.spawn_environment("base", duration=10.0, size=64)
        self.assertIsNotNone(app.environment)

    def test_environment_is_instance_of_class_Environment(self):
        app = create_app(self.cfg)
        env_base_class = app.env_dict.get("base")
        app.spawn_environment(environment="regular_clear", duration=10.0, size=16)
        app_env = app.environment
        self.assertTrue(issubclass(app_env.__class__, env_base_class))


class TestEnvOwnAttributes(unittest.TestCase):
    def setUp(self):
        os.environ['APP_ENV'] = 'test'
        self.cfg = get_config().get("cfg")
        self.app = create_app(self.cfg)
        self.rng_size = randint(0, 1000000)
        self.rng_duration = random() * 10e2
        self.app.spawn_environment(environment="regular_clear",
                                   size=self.rng_size,
                                   duration=self.rng_duration)

    def tearDown(self):
        os.environ.pop('APP_ENV')

    def test_env_has_non_zero_size(self):
        self.assertGreater(self.app.environment.size, 0)

    def test_env_has_non_zero_duration(self):
        self.assertGreater(self.app.environment.duration, 0.0)

    def test_env_expected_size(self):
        expected_size = self.rng_size
        self.assertEqual(self.app.environment.size, expected_size)

    def test_env_expected_duration(self):
        expected_duration = self.rng_duration
        self.assertEqual(self.app.environment.duration, expected_duration)

    def test_env_has_expected_name(self):
        self.assertEqual(self.app.environment.name, self.cfg["app"]["name"])

    # TODO: add a tick() method to the app
    # TODO: add a stop() method to the the app? or environ? = duration
