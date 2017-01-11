Diazo Snippets
==============

Base snippets
"""""""""""""


Additional available snippets
-----------------------------

The following snippets are always available, as soon as the add-on is activated.

Plone Version Number
""""""""""""""""""""

It will show the currently used Plone major version number.
It will be available as content with the CSS id ``PLONE_THEMING_PLONE_VERSION_${plone_version}``, e.g. ``PLONE_THEMING_PLONE_VERSION_4`` for Plone 4.

Diazo example:

.. code-block:: xml

    <rules css:if-content="#PLONE_THEMING_PLONE_VERSION_4">
      <!-- Do some Plone 4 specific stuff -->
    </rules>

    <rules css:if-content="#PLONE_THEMING_PLONE_VERSION_5">
      <!-- Do some Plone 5 specific stuff -->
    </rules>
