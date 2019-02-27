# -*- coding: utf-8 -*-
"""Test UI with robot framework."""

from plone.app.testing import ROBOT_TEST_LEVEL
from plone.testing import layered
from spirit.plone.theming import testing

import os
import robotsuite
import unittest


def test_suite():
    """Create a test suite for robot tests."""
    suite = unittest.TestSuite()
    current_dir = os.path.abspath(os.path.dirname(__file__))
    robot_dir = os.path.join(current_dir, 'robot')
    robot_tests = [
        os.path.join('robot', doc)
        for doc in os.listdir(robot_dir)
        if doc.startswith('test') and doc.endswith('.robot')
    ]
    for robot_test in robot_tests:
        robottestsuite = robotsuite.RobotTestSuite(robot_test)
        robottestsuite.level = ROBOT_TEST_LEVEL
        suite.addTests(
            [
                layered(
                    robottestsuite,
                    layer=testing.ACCEPTANCE_TESTING,
                ),
            ],
        )
    return suite
