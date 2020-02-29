"""
These are the class definitions for basic test cases, used by unittest.
Add to them as you see fit.
"""
import unittest
import os
import main
from helpers.general import get_config


class AppBasics(unittest.TestCase):
    def setUp(self):
        os.environ['APP_ENV'] = 'test'

    def tearDown(self):
        os.environ.pop('APP_ENV')

    def test_main_is_running(self):
        self.assertTrue(main.main())

    def test_logger_is_present(self):
        self.assertLogs()

    def test_config_is_not_empty(self):
        cfg = get_config()
        self.assertTrue(len(cfg) > 0)
