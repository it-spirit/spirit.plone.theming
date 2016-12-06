# -*- coding: utf-8 -*-
"""Test spirit.plone.theming vocabularies."""

# python imports
try:
    import unittest2 as unittest
except ImportError:
    import unittest

# zope imports
from plone import api as ploneapi
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory

# local imports
from spirit.plone.theming.interfaces import IPloneThemingVocabularies
from spirit.plone.theming.testing import INTEGRATION_TESTING


class VocabulariesTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_available_header_options_vocabulary(self):
        """Validate the 'AvailableHeaderOptions' vocabulary."""
        name = 'spirit.plone.theming.AvailableHeaderOptions'
        vocabulary = queryUtility(IVocabularyFactory, name)
        self.assertIsNotNone(vocabulary)
        items = vocabulary(self.portal)
        self.assertEqual(len(items), 0)

        ploneapi.portal.set_registry_record(
            name='available_header_options',
            value=set(['header-default', 'header-v1']),
            interface=IPloneThemingVocabularies,
        )
        items = vocabulary(self.portal)
        self.assertEqual(len(items), 2)
        self.assertIn(u'header-default', items)
        self.assertIn(u'header-v1', items)

    def test_available_footer_options_vocabulary(self):
        """Validate the 'AvailableFooterOptions' vocabulary."""
        name = 'spirit.plone.theming.AvailableFooterOptions'
        vocabulary = queryUtility(IVocabularyFactory, name)
        self.assertIsNotNone(vocabulary)
        items = vocabulary(self.portal)
        self.assertEqual(len(items), 0)

        ploneapi.portal.set_registry_record(
            name='available_footer_options',
            value=set(['footer-default', 'footer-v1']),
            interface=IPloneThemingVocabularies,
        )
        items = vocabulary(self.portal)
        self.assertEqual(len(items), 2)
        self.assertIn(u'footer-default', items)
        self.assertIn(u'footer-v1', items)

    def test_available_color_options_vocabulary(self):
        """Validate the 'AvailableColorOptions' vocabulary."""
        name = 'spirit.plone.theming.AvailableColorOptions'
        vocabulary = queryUtility(IVocabularyFactory, name)
        self.assertIsNotNone(vocabulary)
        items = vocabulary(self.portal)
        self.assertEqual(len(items), 0)

        ploneapi.portal.set_registry_record(
            name='available_color_options',
            value=set(['blue', 'green', 'red']),
            interface=IPloneThemingVocabularies,
        )
        items = vocabulary(self.portal)
        self.assertEqual(len(items), 3)
        self.assertIn(u'blue', items)
        self.assertIn(u'green', items)
        self.assertIn(u'red', items)

    def test_available_pattern_options_vocabulary(self):
        """Validate the 'AvailablePatternOptions' vocabulary."""
        name = 'spirit.plone.theming.AvailablePatternOptions'
        vocabulary = queryUtility(IVocabularyFactory, name)
        self.assertIsNotNone(vocabulary)
        items = vocabulary(self.portal)
        self.assertEqual(len(items), 0)

        ploneapi.portal.set_registry_record(
            name='available_pattern_options',
            value=set(['pat1', 'pat2', 'pat3']),
            interface=IPloneThemingVocabularies,
        )
        items = vocabulary(self.portal)
        self.assertEqual(len(items), 3)
        self.assertIn(u'pat1', items)
        self.assertIn(u'pat2', items)
        self.assertIn(u'pat3', items)

    def test_available_layout_options_vocabulary(self):
        """Validate the 'AvailableLayoutOptions' vocabulary."""
        name = 'spirit.plone.theming.AvailableLayoutOptions'
        vocabulary = queryUtility(IVocabularyFactory, name)
        self.assertIsNotNone(vocabulary)
        items = vocabulary(self.portal)
        self.assertEqual(len(items), 0)

        ploneapi.portal.set_registry_record(
            name='available_layout_options',
            value=set(['boxed', 'wide']),
            interface=IPloneThemingVocabularies,
        )
        items = vocabulary(self.portal)
        self.assertEqual(len(items), 2)
        self.assertIn(u'boxed', items)
        self.assertIn(u'wide', items)
