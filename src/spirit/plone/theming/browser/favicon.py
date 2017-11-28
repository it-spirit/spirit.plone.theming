# -*- coding: utf-8 -*-
"""Browser view for getting the favicon."""

from plone.formwidget.namedfile.converter import b64decode_file
from plone.namedfile.browser import Download
from plone.namedfile.file import NamedImage
from plone.registry.interfaces import IRegistry
from spirit.plone.theming.interfaces import IPloneThemeSettings
from zope.component import getUtility


class Favicon(Download):
    """Browser view for getting the favicon."""

    def __init__(self, context, request):
        super(Favicon, self).__init__(context, request)
        self.filename = None
        self.data = None

        registry = getUtility(IRegistry)
        settings = registry.forInterface(IPloneThemeSettings)  # noqa
        if getattr(settings, 'site_favicon', False):
            filename, data = b64decode_file(settings.site_favicon)
            data = NamedImage(data=data, filename=filename)
            self.data = data
            self.filename = filename
            # self.width, self.height = self.data.getImageSize()

    def _getFile(self):
        return self.data
