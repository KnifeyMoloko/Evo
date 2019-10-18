import os
import unittest
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
        duration = int(app.default_environment_config.get("duration"))
        self.assertTrue(duration)

    def test_env_cfg_has_has_size(self):
        app = create_app(self.cfg)
        size = int(app.default_environment_config.get("size"))
        self.assertTrue(size)


class EnvironmentClassTests(unittest.TestCase):
    def setUp(self):
        os.environ['APP_ENV'] = 'test'
        self.cfg = get_config().get("cfg")

    def tearDown(self):
        os.environ.pop('APP_ENV')

    def test_app_spawns_environment(self):
        app = create_app(self.cfg)
        app.spawn_environment("base", duration=10, size=64)
        self.assertIsNotNone(app.environment)

    def test_environment_is_instance_of_class_Environment(self):
        app = create_app(self.cfg)
        env_class = app.env_dict.get("base")
        app.spawn_environment(environment="base", duration=10, size=16)
        self.assertIsInstance(obj=app.environment, cls=env_class)

    def test_env_has_non_zero_size(self):
        app = create_app(self.cfg)
        expected_size = 8
        app.spawn_environment("base", duration=10, size=expected_size)
        self.assertEqual(app.environment.size, expected_size)

    # TODO: redo the class instance test to check for sublcassing
    # TODO: environment instance has the correct attributes: size, duration, name
    # TODO: app loads the correct environment based on name
    # TODO: add a tick() method to the app
    # TODO: add a stop() method to the the app? or environ? = duration
