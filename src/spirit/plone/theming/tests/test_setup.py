# -*- coding: utf-8 -*-
"""Test Setup of spirit.plone.theming."""

from plone import api
from plone.browserlayer.utils import registered_layers
from spirit.plone.theming.config import PROJECT_NAME
from spirit.plone.theming.testing import INTEGRATION_TESTING

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Validate setup process for spirit.plone.theming."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']
        if get_installer is not None:
            self.installer = get_installer(self.portal)
        else:
            self.installer = self.portal.portal_quickinstaller

    def test_product_is_installed(self):
        """Validate that our product is installed."""
        try:
            result = self.installer.is_product_installed(PROJECT_NAME)
        except AttributeError:
            result = self.installer.isProductInstalled(PROJECT_NAME)
        self.assertTrue(result)

    def test_addon_layer(self):
        """Validate that the browserlayer for our product is installed."""
        from spirit.plone.theming.interfaces import ISpiritPloneThemingLayer
        self.assertIn(ISpiritPloneThemingLayer, registered_layers())


class UninstallTestCase(unittest.TestCase):
    """Validate uninstall process for spirit.plone.theming."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']

        if get_installer is not None:
            self.installer = get_installer(self.portal)
        else:
            self.installer = self.portal.portal_quickinstaller

        with api.env.adopt_roles(['Manager']):
            try:
                self.installer.uninstall_product(PROJECT_NAME)
            except AttributeError:
                self.installer.uninstallProducts(products=[PROJECT_NAME])

    def test_product_is_uninstalled(self):
        """Validate that our product is uninstalled."""
        try:
            result = self.installer.is_product_installed(PROJECT_NAME)
        except AttributeError:
            result = self.installer.isProductInstalled(PROJECT_NAME)
        self.assertFalse(result)

    def test_addon_layer_removed(self):
        """Validate that the browserlayer is removed."""
        from spirit.plone.theming.interfaces import ISpiritPloneThemingLayer
        self.assertNotIn(ISpiritPloneThemingLayer, registered_layers())
