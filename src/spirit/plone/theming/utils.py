"""Theming utils."""
# -*- coding: utf-8 -*-

from plone import api
from plone.registry.interfaces import IRegistry
from spirit.plone.theming import PLONE_4
from zope.component import getUtility


def get_site_favicon(site=None):
    """Return the custom favicon or Plone's default."""
    from spirit.plone.theming.interfaces import IPloneThemeSettings
    from plone.formwidget.namedfile.converter import b64decode_file

    if site is None:
        site = api.portal.get()

    registry = getUtility(IRegistry)
    settings = registry.forInterface(IPloneThemeSettings, check=False)  # noqa
    site_url = site.absolute_url()

    if getattr(settings, 'site_favicon', False):
        filename, data = b64decode_file(settings.site_favicon)
        return '{0}/@@site-favicon/{1}'.format(site_url, filename)
    else:
        return '{0}/favicon.ico'.format(site_url)


def get_site_logo(site=None):
    """Return the custom logo or Plone's default."""
    if not PLONE_4:
        try:
            from Products.CMFPlone.utils import getSiteLogo
        except ImportError:
            return None
        else:
            return getSiteLogo(site=site)

    from spirit.plone.theming.interfaces import IPloneThemeSettings
    from plone.formwidget.namedfile.converter import b64decode_file

    if site is None:
        site = api.portal.get()

    registry = getUtility(IRegistry)
    settings = registry.forInterface(IPloneThemeSettings, check=False)  # noqa
    site_url = site.absolute_url()

    if getattr(settings, 'site_logo', False):
        filename, data = b64decode_file(settings.site_logo)
        return '{0}/@@site-logo-plone4/{1}'.format(site_url, filename)
    else:
        return '{0}/logo.png'.format(site_url)
