# -*- coding: utf-8 -*-
"""Test spirit.plone.theming viewlets."""

# zope imports
from plone import api as ploneapi
from plone.app.layout.viewlets.tests.base import ViewletsTestCase
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

# local imports
from spirit.plone.theming.browser.viewlets import DiazoSnippetViewlet
from spirit.plone.theming.interfaces import (
    IPloneThemeSettings,
    IPloneThemingVocabularies,
)


class TestDiazoSnippetsViewlet(ViewletsTestCase):
    """Validate the diazo snippets viewlet."""

    if ploneapi.env.plone_version()[:1] >= '5':
        from spirit.plone.theming.testing import INTEGRATION_TESTING
        layer = INTEGRATION_TESTING

    def afterSetUp(self):
        registry = getUtility(IRegistry)
        registry.registerInterface(IPloneThemeSettings)
        registry.registerInterface(IPloneThemingVocabularies)

    def test_diazo_snippets_viewlet_render(self):
        """Validate that the diazo snippet viewlet renders correctly."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        rendered = dsv.render()
        try:
            self.assertIn('spirit_plone_theming_diazo_snippets', rendered)
        except AttributeError:
            self.assertTrue('spirit_plone_theming_diazo_snippets' in rendered)

    def test_diazo_snippets_debug_style(self):
        """Validate that the diazo snippet viewlet applies correct CSS."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        rendered = dsv.render()
        self.assertEqual(dsv.debug_style, 'none')
        try:
            self.assertIn('style="display: none"', rendered)
        except AttributeError:
            self.assertTrue('style="display: none"' in rendered)

    def test_diazo_snippets_debug_style_set(self):
        """Validate that the diazo snippet viewlet applies correct CSS."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='debug',
            value=True,
            interface=IPloneThemeSettings,
        )
        rendered = dsv.render()
        self.assertEqual(dsv.debug_style, 'block')
        try:
            self.assertIn('style="display: block"', rendered)
        except AttributeError:
            self.assertTrue('style="display: block"' in rendered)

    def test_diazo_snippet_debug(self):
        """Validate the 'debug' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        rendered = dsv.render()
        self.assertFalse(dsv.debug)
        try:
            self.assertNotIn('PLONE_THEMING_DEBUG', rendered)
        except AttributeError:
            self.assertFalse('PLONE_THEMING_DEBUG' in rendered)

    def test_diazo_debug_set(self):
        """Validate the 'debug' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='debug',
            value=True,
            interface=IPloneThemeSettings,
        )
        rendered = dsv.render()
        self.assertTrue(dsv.debug)
        try:
            self.assertIn('PLONE_THEMING_DEBUG', rendered)
        except AttributeError:
            self.assertTrue('PLONE_THEMING_DEBUG' in rendered)

    def test_diazo_snippet_plone_version(self):
        """Validate the 'plone_version' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        rendered = dsv.render()
        version = ploneapi.env.plone_version()[:1]
        self.assertEqual(dsv.plone_version, version)
        snippet_id = '_'.join(['PLONE_THEMING_PLONE_VERSION', version])
        try:
            self.assertIn(snippet_id, rendered)
        except AttributeError:
            self.assertTrue(snippet_id in rendered)

    def test_diazo_snippet_header_option(self):
        """Validate the 'header_option' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        self.assertEqual(dsv.header_option, None)

    def test_diazo_snippet_header_option_set(self):
        """Validate the 'header_option' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='available_header_options',
            value=set(['header-default', ]),
            interface=IPloneThemingVocabularies,
        )
        ploneapi.portal.set_registry_record(
            name='header_option',
            value='header-default',
            interface=IPloneThemeSettings,
        )
        self.assertEqual(dsv.header_option, 'header-default')

    def test_diazo_snippet_footer_option(self):
        """Validate the 'footer_option' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        self.assertEqual(dsv.footer_option, None)

    def test_diazo_snippet_footer_option_set(self):
        """Validate the 'footer_option' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='available_footer_options',
            value=set(['footer-default', ]),
            interface=IPloneThemingVocabularies,
        )
        ploneapi.portal.set_registry_record(
            name='footer_option',
            value='footer-default',
            interface=IPloneThemeSettings,
        )
        self.assertEqual(dsv.footer_option, 'footer-default')

    def test_diazo_snippet_color_option(self):
        """Validate the 'color_option' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        self.assertEqual(dsv.color_option, None)

    def test_diazo_snippet_color_option_set(self):
        """Validate the 'color_option' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='available_color_options',
            value=set(['blue', 'green', ]),
            interface=IPloneThemingVocabularies,
        )
        ploneapi.portal.set_registry_record(
            name='color_option',
            value='green',
            interface=IPloneThemeSettings,
        )
        self.assertEqual(dsv.color_option, 'green')

    def test_diazo_snippet_pattern_option(self):
        """Validate the 'pattern_option' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        self.assertEqual(dsv.pattern_option, None)

    def test_diazo_snippet_pattern_option_set(self):
        """Validate the 'pattern_option' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='available_pattern_options',
            value=set(['pat1', 'pat2', 'pat3', ]),
            interface=IPloneThemingVocabularies,
        )
        ploneapi.portal.set_registry_record(
            name='pattern_option',
            value='pat2',
            interface=IPloneThemeSettings,
        )
        self.assertEqual(dsv.pattern_option, 'pat2')

    def test_diazo_snippet_layout_option(self):
        """Validate the 'layout_option' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        self.assertEqual(dsv.layout_option, None)

    def test_diazo_snippet_layout_option_set(self):
        """Validate the 'layout_option' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='available_layout_options',
            value=set(['boxed', 'wide', ]),
            interface=IPloneThemingVocabularies,
        )
        ploneapi.portal.set_registry_record(
            name='layout_option',
            value='boxed',
            interface=IPloneThemeSettings,
        )
        self.assertEqual(dsv.layout_option, 'boxed')

    def test_diazo_snippet_slogan(self):
        """Validate the 'slogan' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        self.assertEqual(dsv.slogan, None)

    def test_diazo_snippet_slogan_set(self):
        """Validate the 'slogan' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='slogan',
            value=u'This is my slogan.',
            interface=IPloneThemeSettings,
        )
        self.assertEqual(dsv.slogan, u'This is my slogan.')

    def test_diazo_snippet_phone_number(self):
        """Validate the 'phone_number' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        self.assertEqual(dsv.phone_number, None)
        self.assertEqual(dsv.phone_number_raw, None)

    def test_diazo_snippet_phone_number_set(self):
        """Validate the 'phone_number' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='phone_number',
            value=u'+1 (234) 567-890',
            interface=IPloneThemeSettings,
        )
        self.assertEqual(dsv.phone_number, u'+1 (234) 567-890')
        self.assertEqual(dsv.phone_number_raw, u'1234567890')

    def test_diazo_snippet_email(self):
        """Validate the 'email' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        self.assertEqual(dsv.email, None)

    def test_diazo_snippet_email_set(self):
        """Validate the 'email' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='email',
            value=u'info@example.com',
            interface=IPloneThemeSettings,
        )
        self.assertEqual(dsv.email, u'info@example.com')

    def test_diazo_snippet_hide_searchbox(self):
        """Validate the 'hide_searchbox' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        rendered = dsv.render()
        self.assertFalse(dsv.hide_searchbox)
        try:
            self.assertNotIn('PLONE_THEMING_HIDE_SEARCHBOX', rendered)
        except AttributeError:
            self.assertFalse('PLONE_THEMING_HIDE_SEARCHBOX' in rendered)

    def test_diazo_snippet_hide_searchbox_set(self):
        """Validate the 'hide_searchbox' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='hide_searchbox',
            value=True,
            interface=IPloneThemeSettings,
        )
        rendered = dsv.render()
        self.assertTrue(dsv.hide_searchbox)
        try:
            self.assertIn('PLONE_THEMING_HIDE_SEARCHBOX', rendered)
        except AttributeError:
            self.assertTrue('PLONE_THEMING_HIDE_SEARCHBOX' in rendered)

    def test_diazo_snippet_slideshow_fullscreen(self):
        """Validate the 'slideshow_fullscreen' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        rendered = dsv.render()
        self.assertFalse(dsv.slideshow_fullscreen)
        try:
            self.assertNotIn('PLONE_THEMING_SLIDESHOW_FULLSCREEN', rendered)
        except AttributeError:
            self.assertFalse('PLONE_THEMING_SLIDESHOW_FULLSCREEN' in rendered)

    def test_diazo_snippet_slideshow_fullscreen_set(self):
        """Validate the 'slideshow_fullscreen' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='slideshow_fullscreen',
            value=True,
            interface=IPloneThemeSettings,
        )
        rendered = dsv.render()
        self.assertTrue(dsv.slideshow_fullscreen)
        try:
            self.assertIn('PLONE_THEMING_SLIDESHOW_FULLSCREEN', rendered)
        except AttributeError:
            self.assertTrue('PLONE_THEMING_SLIDESHOW_FULLSCREEN' in rendered)

    def test_diazo_snippet_footer_text(self):
        """Validate the 'footer_text' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        self.assertEqual(dsv.footer_text, None)

    def test_diazo_snippet_footer_text_set(self):
        """Validate the 'footer_text' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='footer_text',
            value=u'<p>&copy; Copyright 2009-{year} Your Company Name</p>',
            interface=IPloneThemeSettings,
        )
        output = dsv.footer_text
        import datetime
        year = datetime.datetime.now().strftime('%Y')
        try:
            self.assertIn('Copyright 2009-', output)
            self.assertIn(year, output)
        except AttributeError:
            self.assertTrue('Copyright 2009-' in output)
            self.assertTrue(year in output)

    def test_diazo_snippet_colophon_text(self):
        """Validate the 'colophon_text' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        self.assertEqual(dsv.colophon_text, None)

    def test_diazo_snippet_colophon_text_set(self):
        """Validate the 'colophon_text' attribute."""
        dsv = DiazoSnippetViewlet(self.portal, self.app.REQUEST, None)
        dsv.update()
        ploneapi.portal.set_registry_record(
            name='colophon_text',
            value=u''.join([
                u'<p>Powered by Plone, Python & <a href="{portal_url}">'
                u'Your Company Name</a></p>',
            ]),
            interface=IPloneThemeSettings,
        )
        output = dsv.colophon_text
        url = u'http://nohost/plone'
        try:
            self.assertIn('Powered by Plone, Python', output)
            self.assertIn(url, output)
        except AttributeError:
            self.assertTrue('Powered by Plone, Python' in output)
            self.assertTrue(url in output)
