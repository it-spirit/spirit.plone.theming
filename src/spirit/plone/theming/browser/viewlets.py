# -*- coding: utf-8 -*-
"""Viewlets for spirit.plone.theming."""

from plone import api as ploneapi
from plone.api.exc import InvalidParameterError
from plone.app.layout.viewlets.common import LogoViewlet as LogoViewletPlone
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize import view
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from spirit.plone.theming import utils
from spirit.plone.theming.interfaces import IPloneThemeSettings

import datetime
import pkg_resources


class DiazoSnippetViewlet(ViewletBase):
    """Rendered diazo snippets."""

    index = ViewPageTemplateFile('templates/diazo_snippets.pt')

    def _get_registry_record(self, name=None):
        try:
            return ploneapi.portal.get_registry_record(
                name=name,
                interface=IPloneThemeSettings,
            )
        except (KeyError, InvalidParameterError):
            return None

    @property
    @view.memoize_contextless
    def debug_style(self):
        raw = self._get_registry_record(name='debug')
        return raw and 'block' or 'none'

    @property
    @view.memoize_contextless
    def debug(self):
        return self._get_registry_record(name='debug')

    @property
    @view.memoize_contextless
    def plone_version(self):
        return ploneapi.env.plone_version()[:1]

    @property
    @view.memoize_contextless
    def colophon_text(self):
        raw = self._get_registry_record(name='colophon_text')
        if not raw:
            return
        return raw.format(
            portal_url=ploneapi.portal.get().absolute_url(),
            year=datetime.datetime.now().year,
        )

    @property
    @view.memoize_contextless
    def color_option(self):
        return self._get_registry_record(name='color_option')

    @property
    @view.memoize_contextless
    def email(self):
        return self._get_registry_record(name='email')

    @property
    @view.memoize_contextless
    def footer_option(self):
        return self._get_registry_record(name='footer_option')

    @property
    @view.memoize_contextless
    def footer_text(self):
        raw = self._get_registry_record(name='footer_text')
        if not raw:
            return
        return raw.format(
            portal_url=ploneapi.portal.get().absolute_url(),
            year=datetime.datetime.now().year,
        )

    @property
    @view.memoize_contextless
    def header_option(self):
        return self._get_registry_record(name='header_option')

    @property
    @view.memoize_contextless
    def layout_option(self):
        return self._get_registry_record(name='layout_option')

    @property
    @view.memoize_contextless
    def pattern_option(self):
        return self._get_registry_record(name='pattern_option')

    @property
    @view.memoize_contextless
    def phone_number(self):
        return self._get_registry_record(name='phone_number')

    @property
    @view.memoize_contextless
    def phone_number_raw(self):
        raw = self._get_registry_record(name='phone_number')
        return utils.get_raw_phone_number(raw)

    @property
    @view.memoize_contextless
    def hide_searchbox(self):
        return self._get_registry_record(name='hide_searchbox')

    @property
    @view.memoize_contextless
    def slogan(self):
        return self._get_registry_record(name='slogan')

    @property
    @view.memoize_contextless
    def favicon(self):
        return utils.get_site_favicon()

    @property
    @view.memoize_contextless
    def hide_footer(self):
        return self._get_registry_record(name='hide_footer')

    @property
    @view.memoize_contextless
    def hide_colophon(self):
        return self._get_registry_record(name='hide_colophon')

    @property
    @view.memoize_contextless
    def themingplugins_available(self):
        try:
            pkg_resources.get_distribution('plone.app.themingplugins')
            return True
        except pkg_resources.DistributionNotFound:
            return False

    @property
    @view.memoize_contextless
    def themefragments_available(self):
        try:
            pkg_resources.get_distribution('collective.themefragments')
            return True
        except pkg_resources.DistributionNotFound:
            return False

    @property
    @view.memoize_contextless
    def rapido_available(self):
        try:
            pkg_resources.get_distribution('rapido.plone')
            return True
        except pkg_resources.DistributionNotFound:
            return False


class LogoViewlet(LogoViewletPlone):
    """Show the site logo."""

    index = ViewPageTemplateFile('templates/logo.pt')

    def update(self):
        super(LogoViewlet, self).update()

        self.navigation_root_title = self.portal_state.navigation_root_title()
        self.img_src = utils.get_site_logo()
