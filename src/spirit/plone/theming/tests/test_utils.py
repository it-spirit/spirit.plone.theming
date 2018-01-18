# -*- coding: utf-8 -*-
"""Test spirit.plone.theming utilities."""

from spirit.plone.theming import utils
from spirit.plone.theming.testing import INTEGRATION_TESTING


try:
    import unittest2 as unittest
except ImportError:
    import unittest


class UtilitiesTestCase(unittest.TestCase):
    """Validate the vocabularies."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_get_raw_phone_number(self):
        """Validate the 'get_raw_phone_number' function."""
        self.assertEqual(
            utils.get_raw_phone_number(u'1234567890'),
            u'1234567890',
        )
        self.assertEqual(
            utils.get_raw_phone_number(u'1-234-567-890'),
            u'1234567890',
        )
        self.assertEqual(
            utils.get_raw_phone_number(u'+1-234-567-890'),
            u'001234567890',
        )
        self.assertEqual(
            utils.get_raw_phone_number(u'+1-(234)-567-890'),
            u'001234567890',
        )
