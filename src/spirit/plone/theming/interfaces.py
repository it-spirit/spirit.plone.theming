# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

# zope imports
from plone.directives import form
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

# local imports
from spirit.plone.theming import _


class ISpiritPloneThemingLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPloneThemeSettingsEditForm(Interface):
    """Marker interface for the Theme Settings Form."""


class IPloneThemeSettings(form.Schema):
    """Plone Theming Settings.

    This describes records stored in the configuration registry and obtainable
    via plone.registry.
    """
    debug = schema.Bool(
        description=_(
            u'If enabled, the content of the diazo snippets will be '
            u'visible to the user. If disabled, the content is hidden '
            u'with CSS.'
        ),
        required=False,
        title=_(u'Enable Debug Mode'),
    )

    header_option = schema.Choice(
        description=_(
            u'Select the header variant which should be used for the current '
            u'theme.'
        ),
        required=False,
        title=_(u'Header Option'),
        vocabulary='spirit.plone.theming.AvailableHeaderOptions',
    )

    footer_option = schema.Choice(
        description=_(
            u'Select the footer variant which should be used for the current '
            u'theme.'
        ),
        required=False,
        title=_(u'Footer Option'),
        vocabulary='spirit.plone.theming.AvailableFooterOptions',
    )

    color_option = schema.Choice(
        description=_(
            u'Select the color variant which should be used for the current '
            u'theme.'
        ),
        required=False,
        title=_(u'Color Option'),
        vocabulary='spirit.plone.theming.AvailableColorOptions',
    )

    pattern_option = schema.Choice(
        description=_(
            u'Select the background pattern which should be used for the '
            u'current theme.'
        ),
        required=False,
        title=_(u'Pattern Option'),
        vocabulary='spirit.plone.theming.AvailablePatternOptions',
    )

    layout_option = schema.Choice(
        description=_(
            u'Select the layout variant which should be used for the current '
            u'theme.'
        ),
        required=False,
        title=_(u'Layout Option'),
        vocabulary='spirit.plone.theming.AvailableLayoutOptions',
    )

    slogan = schema.Text(
        description=_(
            u'Add a slogan for your website (HTML is supported). '
            u'The slogan will be available as content with the CSS id '
            u'<em>PLONE_THEMING_SLOGAN</em>.'
        ),
        required=False,
        title=_(u'Slogan')
    )

    phone_number = schema.TextLine(
        description=_(
            u'Add a phone number for your primary website contact. '
            u'The phone number will be available as content with the CSS id '
            u'<em>PLONE_THEMING_PHONE_NUMBER</em> and '
            u'<em>PLONE_THEMING_PHONE_NUMBER_RAW</em> (all non-number '
            u'characters removed).'
        ),
        required=False,
        title=_(u'Phone number'),
    )

    email = schema.TextLine(
        description=_(
            u'Add a valid email address. '
            u'The email address will be available as content with the CSS id '
            u'<em>PLONE_THEMING_EMAIL</em>.'
        ),
        required=False,
        title=_(u'E-Mail Address'),
    )

    hide_searchbox = schema.Bool(
        description=_(
            u'If enabled, the search box (available in the header part) '
            u'will be removed in the theme.'
            u'The searchbox option will be available as content '
            u'with the CSS id <em>PLONE_THEMING_HIDE_SEARCHBOX</em> '
            u'if enabled.'
        ),
        required=False,
        title=_(u'Hide Search Box'),
    )

    slideshow_fullscreen = schema.Bool(
        description=_(
            u'If enabled, a slideshow (if available) will be rendered in '
            u'fullscreen mode. Depending on the theme, this might be above '
            u'the main menu or as header background. If disabled, the '
            u'slideshow is visible within the content area.'
            u'The slideshow fullscreen mode will be available as content '
            u'with the CSS id <em>PLONE_THEMING_SLIDESHOW_FULLSCREEN</em> '
            u'if enabled.'
        ),
        required=False,
        title=_(u'Slideshow Fullscreen Mode'),
    )

    footer_text = schema.Text(
        description=_(
            u'Add your custom footer text (HTML is supported). '
            u'The footer text will be available as content with the CSS id '
            u'<em>PLONE_THEMING_FOOTER_TEXT</em>. '
            u'You can also add the following variables: '
            u'<em>{portal_url}</em>, '
            u'<em>{year}</em>. '
            u'Example: <code>&lt;p&gt;&amp;copy; Copyright 2009-{year} '
            u'Your Company Name&lt;/p&gt;</code>.'
        ),
        required=False,
        title=_(u'Custom Footer Text'),
    )

    colophon_text = schema.Text(
        description=_(
            u'Add your custom colophon text (HTML is supported). '
            u'The colophon text will be available as content with the CSS id '
            u'<em>PLONE_THEMING_COLOPHON_TEXT</em>. '
            u'You can also add the following variables: '
            u'<em>{portal_url}</em>, '
            u'<em>{year}</em>. '
            u'Example: <code>&lt;p&gt;Powered by Plone, Python &amp; &lt;a '
            u'href="{portal_url}"&gt;Your Company Name&lt;/a&gt;&lt;/p&gt;'
            u'</code>.'
        ),
        required=False,
        title=_(u'Custom Colophon Text'),
    )


class IPloneThemingVocabularies(form.Schema):

    available_header_options = schema.Set(
        title=_(u'Available Header Options'),
        required=False,
        default=set(),
        value_type=schema.ASCIILine(title=_(u'Option')),
    )

    available_footer_options = schema.Set(
        title=_(u'Available Footer Options'),
        required=False,
        default=set(),
        value_type=schema.ASCIILine(title=_(u'Option')),
    )

    available_color_options = schema.Set(
        title=_(u'Available Color Options'),
        required=False,
        default=set(),
        value_type=schema.ASCIILine(title=_(u'Option')),
    )

    available_pattern_options = schema.Set(
        title=_(u'Available Pattern Options'),
        required=False,
        default=set(),
        value_type=schema.ASCIILine(title=_(u'Option')),
    )

    available_layout_options = schema.Set(
        title=_(u'Available Layout Options'),
        required=False,
        default=set(),
        value_type=schema.ASCIILine(title=_(u'Option')),
    )
