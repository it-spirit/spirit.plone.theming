*** Settings ***

Resource  keywords.robot

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Show how to change the settings
    Given a logged-in manager
    and the theming controlpanel

    Page should contain element  id=form
    Capture Element Screenshot
    ...  id=form
    ...  settings.png

    Page should contain element  id=formfield-form-widgets-debug
    Capture Element Screenshot
    ...  id=formfield-form-widgets-debug
    ...  settings-debug.png

    Page should contain element  id=formfield-form-widgets-site_favicon
    Capture Element Screenshot
    ...  id=formfield-form-widgets-site_favicon
    ...  settings-site_favicon.png

    Page should contain element  id=formfield-form-widgets-header_option
    Capture Element Screenshot
    ...  id=formfield-form-widgets-header_option
    ...  settings-header_option.png

    Page should contain element  id=formfield-form-widgets-footer_option
    Capture Element Screenshot
    ...  id=formfield-form-widgets-footer_option
    ...  settings-footer_option.png

    Page should contain element  id=formfield-form-widgets-color_option
    Capture Element Screenshot
    ...  id=formfield-form-widgets-color_option
    ...  settings-color_option.png

    Page should contain element  id=formfield-form-widgets-pattern_option
    Capture Element Screenshot
    ...  id=formfield-form-widgets-pattern_option
    ...  settings-pattern_option.png

    Page should contain element  id=formfield-form-widgets-layout_option
    Capture Element Screenshot
    ...  id=formfield-form-widgets-layout_option
    ...  settings-layout_option.png

    Page should contain element  id=formfield-form-widgets-slogan
    Capture Element Screenshot
    ...  id=formfield-form-widgets-slogan
    ...  settings-slogan.png

    Page should contain element  id=formfield-form-widgets-phone_number
    Capture Element Screenshot
    ...  id=formfield-form-widgets-phone_number
    ...  settings-phone_number.png

    Page should contain element  id=formfield-form-widgets-email
    Capture Element Screenshot
    ...  id=formfield-form-widgets-email
    ...  settings-email.png

    Page should contain element  id=formfield-form-widgets-hide_searchbox
    Capture Element Screenshot
    ...  id=formfield-form-widgets-hide_searchbox
    ...  settings-hide_searchbox.png

    Page should contain element  id=formfield-form-widgets-footer_text
    Capture Element Screenshot
    ...  id=formfield-form-widgets-footer_text
    ...  settings-footer_text.png

    Page should contain element  id=formfield-form-widgets-hide_footer
    Capture Element Screenshot
    ...  id=formfield-form-widgets-hide_footer
    ...  settings-hide_footer.png

    Page should contain element  id=formfield-form-widgets-colophon_text
    Capture Element Screenshot
    ...  id=formfield-form-widgets-colophon_text
    ...  settings-colophon_text.png

    Page should contain element  id=formfield-form-widgets-hide_colophon
    Capture Element Screenshot
    ...  id=formfield-form-widgets-hide_colophon
    ...  settings-hide_colophon.png


*** Keywords ***

the theming control panel
  Go to  ${PLONE_URL}/@@plone-theming-settings
