import os
import sys
import unittest

from test_svc.scripts.run import run


CONFIG_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
    'user_settings.py')


class TestTestCase(unittest.TestCase):
    def test_1(self):
        run(CONFIG_FILE)
