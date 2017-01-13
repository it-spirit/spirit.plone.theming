Diazo Snippets
==============

Base snippets
-------------

Enable Debug Mode
"""""""""""""""""

.. code-block:: xml

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
""""""""""""

.. code-block:: xml

    <replace
        css:theme="head link[rel='shortcut icon']"
        css:content="#PLONE_THEMING_FAVICON link"
        />


Header Option
"""""""""""""

Define this variable in your main rules.xml file:

.. code-block:: xml

    <xsl:variable name="header" css:select="#PLONE_THEMING_HEADER_OPTION"></xsl:variable>

Use the defined variable to load the CSS for the header option:

.. code-block:: xml

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
"""""""""""""

Define this variable in your main rules.xml file:

.. code-block:: xml

    <xsl:variable name="footer" css:select="#PLONE_THEMING_FOOTER_OPTION"></xsl:variable>

Use the defined variable to load the CSS for the footer option:

.. code-block:: xml

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
""""""""""""

Use the defined variable to load the CSS for the color option:

.. code-block:: xml

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
""""""""""""""

Define this variable in your main rules.xml file:

.. code-block:: xml

    <xsl:variable name="pattern" css:select="#PLONE_THEMING_PATTERN_OPTION"></xsl:variable>

Use the defined variable to load a pattern specific CSS:

.. code-block:: xml

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
"""""""""""""

Define this variable in your main rules.xml file:

.. code-block:: xml

    <xsl:variable name="layout" css:select="#PLONE_THEMING_LAYOUT_OPTION"></xsl:variable>

Use the defined variable to set a CSS class on the body tag for a specific layout option:

.. code-block:: xml

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
""""""

.. code-block:: xml

    <replace css:content="#PLONE_THEMING_SLOGAN" css:theme="#header-headline" />
    <drop css:if-not-content="#PLONE_THEMING_SLOGAN" css:theme="#header-headline" />


Phone number
""""""""""""

.. code-block:: xml

    <replace css:content="#PLONE_THEMING_PHONE_NUMBER" css:theme=".site-social-links .phone" />
    <drop css:if-not-content="#PLONE_THEMING_PHONE_NUMBER" css:theme=".site-social-links .phone" />


E-Mail Address
""""""""""""""

.. code-block:: xml

    <replace css:content="#PLONE_THEMING_EMAIL" css:theme=".site-social-links .email" />
    <drop css:if-not-content="#PLONE_THEMING_EMAIL" css:theme=".site-social-links .email" />


Hide Search Box
"""""""""""""""

.. code-block:: xml

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
"""""""""""""""""""""""""

.. code-block:: xml

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
""""""""""""""""""

.. code-block:: xml

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
""""""""""""""""

.. code-block:: xml

    <rules css:if-not-content="#PLONE_THEMING_HIDE_FOOTER">
      ...
    </rules>
    <drop css:theme-children=".footer-copyright" css:if-content="#PLONE_THEMING_HIDE_FOOTER" />


Custom Colophon Text
""""""""""""""""""""

.. code-block:: xml

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
""""""""""""""""""

.. code-block:: xml

    <rules css:if-not-content="#PLONE_THEMING_HIDE_COLOPHON">
      ...
    </rules>
    <drop css:theme-children=".footer-colophon" css:if-content="#PLONE_THEMING_HIDE_COLOPHON" />


Additional available snippets
-----------------------------

The following snippets are always available, as soon as the add-on is activated.

Plone Version Number
""""""""""""""""""""

It will show the currently used Plone major version number.
It will be available as content with the CSS id ``PLONE_THEMING_PLONE_VERSION_${plone_version}``, e.g. ``PLONE_THEMING_PLONE_VERSION_4`` for Plone 4:

.. code-block:: xml

    <rules css:if-content="#PLONE_THEMING_PLONE_VERSION_4">
      <!-- Do some Plone 4 specific stuff -->
    </rules>

    <rules css:if-content="#PLONE_THEMING_PLONE_VERSION_5">
      <!-- Do some Plone 5 specific stuff -->
    </rules>
