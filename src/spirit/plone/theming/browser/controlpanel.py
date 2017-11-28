# -*- coding: utf-8 -*-
"""Plone Theming Settings Control Panel."""

from plone.app.registry.browser import controlpanel
from plone.formwidget.namedfile.widget import NamedImageFieldWidget
from plone.registry.interfaces import IRegistry
from spirit.plone.theming import _
from spirit.plone.theming import PLONE_4
from spirit.plone.theming.interfaces import IPloneThemeSettings
from spirit.plone.theming.interfaces import IPloneThemeSettingsEditForm
from z3c.form import field
from zope.component import getUtility
from zope.interface import implementer


class SelfHealingRegistryEditForm(controlpanel.RegistryEditForm):
    """Registers the schema if an error occured."""

    def getContent(self):
        registry = getUtility(IRegistry)
        try:
            return registry.forInterface(  # noqa
                self.schema,
                prefix=self.schema_prefix,
            )
        except KeyError:
            self.ignoreContext = True
            self.fields = field.Fields()
            registry.registerInterface(self.schema)
            self.status = _(
                u'Registry has been updated. Please reload this page.'
            )
            return None


@implementer(IPloneThemeSettingsEditForm)
class PloneThemeSettingsEditForm(SelfHealingRegistryEditForm):
    """Plone Theming Settings Form."""

    schema = IPloneThemeSettings
    label = _(u'Plone Theming Settings')
    description = _(
        u'Settings that can be used by Diazo themes. Please note that not '
        u'every theme supports all possible options.'
    )

    def updateFields(self):
        super(PloneThemeSettingsEditForm, self).updateFields()
        if PLONE_4:
            self.fields['site_logo'].widgetFactory = NamedImageFieldWidget
        self.fields['site_favicon'].widgetFactory = NamedImageFieldWidget

    def updateWidgets(self):
        super(PloneThemeSettingsEditForm, self).updateWidgets()


class PloneThemeSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Plone Theming Settings Control Panel."""

    form = PloneThemeSettingsEditForm
