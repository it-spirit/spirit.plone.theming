*** Settings ***

Resource  keywords.robot

Suite Setup  Setup
Suite Teardown  Teardown


*** Test cases ***

Show how to activate the add-on
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/prefs_install_products_form

    Page should contain element  xpath=//*[@value='spirit.plone.theming']
    Assign id to element
    ...  xpath=//*[@value='spirit.plone.theming']/ancestor::li
    ...  addons-spirit-plone-theming
    Assign id to element
    ...  xpath=//*[@value='spirit.plone.theming']/ancestor::ul/parent::*/parent::*
    ...  addons-enabled

    Highlight  addons-spirit-plone-theming
    Capture and crop page screenshot
    ...  setup_select_add_on.png
    ...  id=addons-enabled

    Click button  xpath=//*[@value='spirit.plone.theming']/ancestor::form//input[@type='submit']

    Page should contain element  xpath=//*[@value='spirit.plone.theming']

    Assign id to element
    ...  xpath=//*[@value='spirit.plone.theming']/ancestor::li
    ...  addons-spirit-plone-theming
    Assign id to element
    ...  xpath=//*[@value='spirit.plone.theming']/ancestor::ul/parent::*/parent::*
    ...  addons-enabled

    Highlight  addons-spirit-plone-theming
    Capture and crop page screenshot
    ...  setup_select_add_on_installable.png
    ...  id=addons-enabled
