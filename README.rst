spirit.plone.theming
====================

This Plone Add-On provides some theming extensions for `Plone`_ Websites.
In order to use it, you would need a diazo theme which supports the provided options.


Mostly Harmless
---------------

.. image:: https://travis-ci.org/it-spirit/spirit.plone.theming.png?branch=master
    :target: http://travis-ci.org/it-spirit/spirit.plone.theming
    :alt: Travis CI status


Available Options
-----------------

Below is a list of currently supported options.
Note that not every theme by default supports all of those options.
The default value is in [square brackets].

debug [``False``]
#################

If enabled, the content of the diazo snippets will be visible to the user.
If disabled, the content is hidden with CSS.
There is also a debug option which will be available as content with the CSS id ``PLONE_THEMING_DEBUG`` if enabled.

header_option [``None``]
########################

Select the header variant which should be used for the current theme.

footer_option [``None``]
########################

Select the footer variant which should be used for the current theme.

color_option [``None``]
#######################

Select the color variant which should be used for the current theme.

pattern_option [``None``]
#########################

Select the background pattern which should be used for the current theme.

layout_option [``None``]
########################

Select the layout variant which should be used for the current theme.

slogan [``None``]
#################

Add a slogan for your website (HTML is supported).
The slogan will be available as content with the CSS id ``PLONE_THEMING_SLOGAN``.

Diazo example::

    <replace css:content="#PLONE_THEMING_SLOGAN" css:theme="#header-headline" />
    <drop css:if-not-content="#PLONE_THEMING_SLOGAN" css:theme="#header-headline" />

phone_number [``None``]
#######################

Add a phone number for your primary website contact.
The phone number will be available as content with the CSS id ``PLONE_THEMING_PHONE_NUMBER`` and ``PLONE_THEMING_PHONE_NUMBER_RAW`` (all non-number characters removed).

Diazo example::

    <replace css:content="#PLONE_THEMING_PHONE_NUMBER" css:theme=".site-social-links .phone" />
    <drop css:if-not-content="#PLONE_THEMING_PHONE_NUMBER" css:theme=".site-social-links .phone" />

email [``None``]
################

Add a valid email address.
The email address will be available as content with the CSS id ``PLONE_THEMING_EMAIL``.

hide_searchbox [``False``]
##########################

If enabled, the search box (available in the header part) will be removed in the theme.
The searchbox option will be available as content with the CSS id ``PLONE_THEMING_HIDE_SEARCHBOX`` if enabled.

slideshow_fullscreen [``False``]
################################

If enabled, a slideshow (if available) will be rendered in fullscreen mode.
Depending on the theme, this might be above the main menu or as header background.
If disabled, the slideshow is visible within the content area.
The slideshow fullscreen mode will be available as content with the CSS id ``PLONE_THEMING_SLIDESHOW_FULLSCREEN`` if enabled.

footer_text [``None``]
######################

Add your custom footer text (HTML is supported).
The footer text will be available as content with the CSS id ``PLONE_THEMING_FOOTER_TEXT``.
You can also add the following variables:

- ``{portal_url}``
- ``{year}``

Example::

     <p>&copy; Copyright 2009-{year} Your Company Name.</p>

colophon_text [``None``]
########################

Add your custom colophon text (HTML is supported).
The colophon text will be available as content with the CSS id ``PLONE_THEMING_COLOPHON_TEXT``.
You can also add the following variables:

- ``{portal_url}``
- ``{year}``

Example::

     <p>Powered by Plone, Python & <a href="{portal_url}">Your Company Name</a></p>


Additional available snippets
-----------------------------

The following snippets are always available, as soon as the add-on is activated.

plone_version
#############

It will show the currently used Plone major version number.
It will be available as content with the CSS id ``PLONE_THEMING_PLONE_VERSION_${plone_version}``, e.g. ``PLONE_THEMING_PLONE_VERSION_4`` for Plone 4.

Diazo example::

    <rules css:if-content="#PLONE_THEMING_PLONE_VERSION_4">
      <!-- Do some Plone 4 specific stuff -->
    </rules>

    <rules css:if-content="#PLONE_THEMING_PLONE_VERSION_5">
      <!-- Do some Plone 5 specific stuff -->
    </rules>


Adding available options from within a Diazo Theme
--------------------------------------------------

By default, the available options for header, footer, color and layout are empty.
But a theme can add it's options to the list of available items by adding elements to the ``plone.registry`` based record values.
The values are then provided as a vocabulary to the theming settings.
The records are defined in ``spirit.plone.theming.interfaces.IPloneThemingVocabularies``.
Currently the following records are available:

- ``available_header_options``
- ``available_footer_options``
- ``available_color_options``
- ``available_layout_options``

A theme could add the records on installation time using the ``registry.xml`` GenersicSetup import step::

    <registry>
      <record field="available_color_options"
          name="spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_color_options"
          interface="spirit.plone.theming.interfaces.IPloneThemingVocabularies">
        <value>
          <element>color-1</element>
          <element>color-2</element>
        </value>
      </record>
      <record field="available_footer_options"
          name="spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_footer_options"
          interface="spirit.plone.theming.interfaces.IPloneThemingVocabularies">
        <value>
          <element>footer-default</element>
          <element>footer-v1</element>
          <element>footer-v2</element>
        </value>
      </record>
      <record field="available_header_options"
          name="spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_header_options"
          interface="spirit.plone.theming.interfaces.IPloneThemingVocabularies">
        <value>
          <element>header-default</element>
          <element>header-v1</element>
          <element>header-v2</element>
        </value>
      </record>
      <record field="available_layout_options"
          name="spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_layout_options"
          interface="spirit.plone.theming.interfaces.IPloneThemingVocabularies">
        <value>
          <element>boxed</element>
          <element>wide</element>
        </value>
      </record>
    </registry>

When the theme gets uninstalled, the entries should be removed.
To do this, add a ``registry.xml`` file to your uninstall profile with the following content::

    <registry>
      <record field="available_color_options"
          name="spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_color_options"
          interface="spirit.plone.theming.interfaces.IPloneThemingVocabularies">
        <value />
      </record>
      <record field="available_footer_options"
          name="spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_footer_options"
          interface="spirit.plone.theming.interfaces.IPloneThemingVocabularies">
        <value />
      </record>
      <record field="available_header_options"
          name="spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_header_options"
          interface="spirit.plone.theming.interfaces.IPloneThemingVocabularies">
        <value />
      </record>
      <record field="available_layout_options"
          name="spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_layout_options"
          interface="spirit.plone.theming.interfaces.IPloneThemingVocabularies">
        <value />
      </record>
    </registry>

``spirit.plone.theming`` has a dependency to `collective.themesitesetup`_, which allows the embedding of GenericSetup import and export steps into zipped theme packages.
To enable this, add the following lines to your theme's manifest.cfg::

  [theme:genericsetup]
  install = install
  uninstall = uninstall

Add the two folders ``install`` and ``uninstall`` next to your manifest.cfg and copy over the ``registry.xml`` files from above.


.. note::

    Themes created with `spirit.bob`_'s ``diazo_theme`` template already include the dependency to ``spirit.plone.theming`` and the required ``registry.xml`` files.

.. _`Plone`: https://plone.org
.. _`collective.themesitesetup`: https://github.com/collective/collective.themesitesetup
.. _`spirit.bob`: https://github.com/it-spirit/spirit.bob
