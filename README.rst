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

Enable Debug Mode
#################

If enabled, the content of the diazo snippets will be visible to the user.
If disabled, the content is hidden with CSS.
There is also a debug option which will be available as content with the CSS id ``PLONE_THEMING_DEBUG`` if enabled.
The default is set to ``False``.

Diazo example::

  <!-- Show spirit.plone.theming debug output for logged in users, if enabled. -->
  <before css:theme-children=".wrapper" css:if-content=".userrole-authenticated #PLONE_THEMING_DEBUG">
    <div class="container">
      <div class="row">
        <div class="col-xs-12">
          <xsl:copy-of css:select="#spirit_plone_theming_diazo_snippets" />
        </div>
      </div>
    </div>
  </before>


Site Favicon
############

You can upload a custom favicon for your Plone site.
Any image format can be uploaded, but \*.ico and \*.png files work best.
If no custom icon is set, Plone's default favicon will be used.
The favicon link HTML markup will be available as content with the CSS id ``PLONE_THEMING_FAVICON``.

Diazo example::

    <replace
        css:theme="head link[rel='shortcut icon']"
        css:content="#PLONE_THEMING_FAVICON link"
        />


Header Option
#############

You can select one of the available header options which are provided by the theme, e.g. ``header-v1`` and ``header-v2``.
If no option is selected, the theme might render a default header.
The selected header option will be available as content with the CSS id ``PLONE_THEMING_HEADER_OPTION``.
The theme should set all available header options using the ``spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_header_options`` registry key.

Diazo example::

    <!-- Define this variable in your main rules.xml file. -->
    <xsl:variable name="header" css:select="#PLONE_THEMING_HEADER_OPTION"></xsl:variable>

    ...

    <!-- Add selected header CSS from spirit.plone.theming. -->
    <after css:theme-children="html head" css:if-content="#PLONE_THEMING_HEADER_OPTION">
      <!-- CSS Header -->
      <xsl:choose>
        <xsl:when test="starts-with($header, 'header-v1')">
          <link rel="stylesheet" href="/++theme++mytheme/assets/css/headers/header-v1.css" />
        </xsl:when>
        <xsl:when test="starts-with($header, 'header-v2')">
          <link rel="stylesheet" href="/++theme++mytheme/assets/css/headers/header-v2.css" />
        </xsl:when>
        <xsl:otherwise>
          <link rel="stylesheet" href="/++theme++mytheme/assets/css/headers/header-v1.css" />
        </xsl:otherwise>
      </xsl:choose>
    </after>

    <!-- Add default header CSS in case we have no option. -->
    <after css:theme-children="html head" css:if-not-content="#PLONE_THEMING_HEADER_OPTION">
      <!-- CSS Header -->
      <link rel="stylesheet" href="/++theme++mytheme/assets/css/headers/header-v1.css" />
    </after>


Footer Option
#############

You can select one of the available footer options which are provided by the theme, e.g. ``footer-v1`` and ``footer-v2``.
If no option is selected, the theme might render a default footer.
The selected footer option will be available as content with the CSS id ``PLONE_THEMING_FOOTER_OPTION``.
The theme should set all available footer options using the ``spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_footer_options`` registry key.

Diazo example::

    <!-- Define this variable in your main rules.xml file. -->
    <xsl:variable name="footer" css:select="#PLONE_THEMING_FOOTER_OPTION"></xsl:variable>

    ...

    <!-- Add selected footer CSS from spirit.plone.theming. -->
    <after css:theme-children="html head" css:if-content="#PLONE_THEMING_FOOTER_OPTION">
      <!-- CSS Footer -->
      <xsl:choose>
        <xsl:when test="starts-with($footer, 'footer-v1')">
          <link rel="stylesheet" href="/++theme++mytheme/assets/css/footers/footer-v1.css" />
        </xsl:when>
        <xsl:when test="starts-with($footer, 'footer-v2')">
          <link rel="stylesheet" href="/++theme++mytheme/assets/css/footers/footer-v2.css" />
        </xsl:when>
        <xsl:otherwise>
          <link rel="stylesheet" href="/++theme++mytheme/assets/css/footers/footer-v1.css" />
        </xsl:otherwise>
      </xsl:choose>
    </after>

    <!-- Add default footer CSS in case we have no option. -->
    <after css:theme-children="html head" css:if-not-content="#PLONE_THEMING_FOOTER_OPTION">
      <!-- CSS Footer -->
      <link rel="stylesheet" href="/++theme++mytheme/assets/css/footers/footer-v1.css" />
    </after>


Color Option
############

You can select one of the available color options which are provided by the theme, e.g. ``blue`` and ``red``.
If no option is selected, the theme might use a default color.
The selected color option will be available as content with the CSS id ``PLONE_THEMING_COLOR_OPTION``.
The theme should set all available color options using the ``spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_color_options`` registry key.

Diazo example::

    <!-- Add selected theme color option from spirit.plone.theming. -->
    <after css:theme-children="html head" css:if-content="#PLONE_THEMING_COLOR_OPTION">
      <xsl:variable name="color" css:select="#PLONE_THEMING_COLOR_OPTION"></xsl:variable>
      <link rel="stylesheet" href="{$portal_url}/++theme++mytheme/assets/css/{$color}.css" type="text/css" />
    </after>

    <!-- Add default theme color in case we have no option. -->
    <after css:theme-children="html head" css:if-not-content="#PLONE_THEMING_COLOR_OPTION">
      <link rel="stylesheet" href="{$portal_url}/++theme++mytheme/assets/css/blue.css" type="text/css" />
    </after>


Pattern Option
##############

You can select one of the available background pattern options which are provided by the theme, e.g. ``diagonal-noise`` and ``fabric-plaid``.
If no option is selected, the theme might use a default pattern.
The selected pattern option will be available as content with the CSS id ``PLONE_THEMING_PATTERN_OPTION``.
The theme should set all available pattern options using the ``spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_pattern_options`` registry key.

This option could also be used to switch between color modes, e.g. ``light`` and ``dark``, if no patterns are available in the theme.

Diazo example::

    <!-- Define this variable in your main rules.xml file. -->
    <xsl:variable name="pattern" css:select="#PLONE_THEMING_PATTERN_OPTION"></xsl:variable>

    ...

    <!-- Add selected pattern option from spirit.plone.theming. -->
    <after css:theme-children="head" css:if-content="#PLONE_THEMING_PATTERN_OPTION">
      <!-- CSS Theme -->
      <xsl:choose>
        <xsl:when test="$pattern='dark'">
          <link rel="stylesheet" href="/++theme++mytheme/assets/css/theme-skins/dark.css" type="text/css" />
        </xsl:when>
      </xsl:choose>
    </after>


Layout Option
#############

You can select one of the available layout options which are provided by the theme, e.g. ``wide`` and ``boxed``.
If no option is selected, the theme might use a default layout.
The selected layout option will be available as content with the CSS id ``PLONE_THEMING_LAYOUT_OPTION``.
The theme should set all available layout options using the ``spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_layout_options`` registry key.

Diazo example::

    <!-- Define this variable in your main rules.xml file. -->
    <xsl:variable name="layout" css:select="#PLONE_THEMING_LAYOUT_OPTION"></xsl:variable>

    ...

    <!-- Add required CSS classes to body tag based on spirit.plone.theming settings. -->
    <before theme-children="html/body">
      <xsl:attribute name="class"><xsl:value-of select="/html/body/@class" />

        <!-- Add selected layout classes from spirit.plone.theming to body tag. -->
        <xsl:choose>
          <xsl:when test="$layout='boxed'">
            <xsl:value-of select="' boxed-layout container'" />
          </xsl:when>
        </xsl:choose>

        ...

      </xsl:attribute>
    </before>


Slogan
######

Add a slogan for your website (HTML is supported).
The slogan will be available as content with the CSS id ``PLONE_THEMING_SLOGAN``.

Diazo example::

    <replace css:content="#PLONE_THEMING_SLOGAN" css:theme="#header-headline" />
    <drop css:if-not-content="#PLONE_THEMING_SLOGAN" css:theme="#header-headline" />


Phone number
############

Add a phone number for your primary website contact.
The phone number will be available as content with the CSS id ``PLONE_THEMING_PHONE_NUMBER`` and ``PLONE_THEMING_PHONE_NUMBER_RAW`` (all non-number characters removed).

Diazo example::

    <replace css:content="#PLONE_THEMING_PHONE_NUMBER" css:theme=".site-social-links .phone" />
    <drop css:if-not-content="#PLONE_THEMING_PHONE_NUMBER" css:theme=".site-social-links .phone" />


E-Mail Address
##############

Add a valid email address.
The email address will be available as content with the CSS id ``PLONE_THEMING_EMAIL``.

Diazo example::

    <replace css:content="#PLONE_THEMING_EMAIL" css:theme=".site-social-links .email" />
    <drop css:if-not-content="#PLONE_THEMING_EMAIL" css:theme=".site-social-links .email" />


Hide Search Box
###############

If enabled, the search box (available in the header part) will be removed in the theme.
The searchbox option will be available as content with the CSS id ``PLONE_THEMING_HIDE_SEARCHBOX`` if enabled.

Diazo example::

    <replace css:if-not-content="#PLONE_THEMING_HIDE_SEARCHBOX" css:theme=".site-search">
      <xsl:for-each css:select="#portal-searchbox form">
        <form><xsl:copy-of select="attribute::*[not(name()='class')]" /><xsl:attribute name="class">site-search <xsl:value-of select="@class" /></xsl:attribute>
          <div class="input-append">
            <xsl:copy-of css:select="#searchGadget" />
            <xsl:for-each select="//input[@class='searchButton']">
              <button><xsl:copy-of select="attribute::*[not(name()='class')]" /><xsl:attribute name="class">btn <xsl:value-of select="@class" /></xsl:attribute>
                <i class="icon-search"></i>
              </button>
            </xsl:for-each>
          </div>
        </form>
      </xsl:for-each>
    </replace>
    <drop css:theme=".site-search" css:if-content="#PLONE_THEMING_HIDE_SEARCHBOX" />


Slideshow Fullscreen Mode
#########################

If enabled, a slideshow (if available) will be rendered in fullscreen mode.
Depending on the theme, this might be above the main menu or as header background.
If disabled, the slideshow is visible within the content area.
The slideshow fullscreen mode will be available as content with the CSS id ``PLONE_THEMING_SLIDESHOW_FULLSCREEN`` if enabled.

Diazo example::

    <rules css:if-content="#PLONE_THEMING_SLIDESHOW_FULLSCREEN">
      <replace css:theme-children="#slideshow_fs">
        <xsl:for-each css:select=".carousel">
          <div class="row">
            <div><xsl:copy-of select="attribute::*" />
              <xsl:apply-templates />
            </div>
          </div>
        </xsl:for-each>
      </replace>
      <drop css:content=".carousel" />
    </rules>
    <drop css:theme="#slideshow_fs" css:if-not-content="#PLONE_THEMING_SLIDESHOW_FULLSCREEN" />


Custom Footer Text
##################

Add your custom footer text (HTML is supported).
The footer text will be available as content with the CSS id ``PLONE_THEMING_FOOTER_TEXT``.
You can also add the following variables:

- ``{portal_url}``
- ``{year}``

Example::

     <p>&copy; Copyright 2009-{year} Your Company Name.</p>

Diazo example (Plone 5)::

    <!-- Replace footer information with Plone version. -->
    <replace
        css:if-not-content="#PLONE_THEMING_FOOTER_TEXT"
        css:theme-children=".footer-copyright p"
        css:content-children="#portal-footer-wrapper #portal-footer-signature .portletContent"
        />

    <replace
        css:if-content="#PLONE_THEMING_FOOTER_TEXT"
        css:theme-children=".footer-copyright"
        css:content-children="#PLONE_THEMING_FOOTER_TEXT"
        />


Hide Footer Text
################

If enabled, the footer text (available in the footer part) will be removed in the theme.
The footer option will be available as content with the CSS id ``PLONE_THEMING_HIDE_FOOTER`` if enabled.

Diazo example::

    <rules css:if-not-content="#PLONE_THEMING_HIDE_FOOTER">
      ...
    </rules>
    <drop css:theme-children=".footer-copyright" css:if-content="#PLONE_THEMING_HIDE_FOOTER" />


Custom Colophon Text
####################

Add your custom colophon text (HTML is supported).
The colophon text will be available as content with the CSS id ``PLONE_THEMING_COLOPHON_TEXT``.
You can also add the following variables:

- ``{portal_url}``
- ``{year}``

Example::

     <p>Powered by Plone, Python & <a href="{portal_url}">Your Company Name</a></p>


Diazo example (Plone 5)::

    <!-- Replace colophon information with Plone version. -->
    <replace
        css:if-not-content="#PLONE_THEMING_COLOPHON_TEXT"
        css:theme-children=".footer-colophon p"
        css:content-children="#portal-footer-wrapper #portal-colophon .portletContent"
        />

    <replace
        css:if-content="#PLONE_THEMING_COLOPHON_TEXT"
        css:theme-children=".footer-colophon"
        css:content-children="#PLONE_THEMING_COLOPHON_TEXT"
        />


Hide Colophon Text
##################

If enabled, the colophon text (available in the footer part) will be removed in the theme.
The colophon option will be available as content with the CSS id ``PLONE_THEMING_HIDE_COLOPHON`` if enabled.

Diazo example::

    <rules css:if-not-content="#PLONE_THEMING_HIDE_COLOPHON">
      ...
    </rules>
    <drop css:theme-children=".footer-colophon" css:if-content="#PLONE_THEMING_HIDE_COLOPHON" />


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
      <record field="available_pattern_options"
          name="spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_pattern_options"
          interface="spirit.plone.theming.interfaces.IPloneThemingVocabularies">
        <value>
          <element>diagonal-noise</element>
          <element>fabric-plaid</element>
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
      <record field="available_pattern_options"
          name="spirit.plone.theming.interfaces.IPloneThemingVocabularies.available_pattern_options"
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
