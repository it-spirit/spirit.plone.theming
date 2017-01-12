Diazo Theme Setup
=================


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

A theme could add the records on installation time using the ``registry.xml`` GenersicSetup import step:

.. code-block:: xml

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
To do this, add a ``registry.xml`` file to your uninstall profile with the following content:

.. code-block:: xml

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
To enable this, add the following lines to your theme's manifest.cfg:

.. code-block:: ini

  [theme:genericsetup]
  install = install
  uninstall = uninstall

Add the two folders ``install`` and ``uninstall`` next to your manifest.cfg and copy over the ``registry.xml`` files from above.


.. _`collective.themesitesetup`: https://github.com/collective/collective.themesitesetup
