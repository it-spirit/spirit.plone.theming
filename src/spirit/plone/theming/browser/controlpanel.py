# -*- coding: utf-8 -*-
"""Plone Theming Settings Control Panel."""

# zope imports
from plone.app.registry.browser import controlpanel
from plone.registry.interfaces import IRegistry
from z3c.form import field
from zope.component import getUtility
from zope.interface import implementer

# local imports
from spirit.plone.theming import _
from spirit.plone.theming.interfaces import (
    IPloneThemeSettings,
    IPloneThemeSettingsEditForm,
)


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

    def updateWidgets(self):
        super(PloneThemeSettingsEditForm, self).updateWidgets()


class PloneThemeSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Plone Theming Settings Control Panel."""

    form = PloneThemeSettingsEditForm
