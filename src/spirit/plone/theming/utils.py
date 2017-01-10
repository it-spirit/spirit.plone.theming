# -*- coding: utf-8 -*-

# zope imports
from plone import api
from plone.registry.interfaces import IRegistry
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
