*** Settings ***

Resource  keywords.robot

Suite Setup  Setup
Suite Teardown  Teardown


*** Test cases ***

Show how to change the settings
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/@@plone-theming-settings

    Page should contain element  id=form
    Capture and crop page screenshot
    ...  settings.png
    ...  id=form

    Page should contain element  id=formfield-form-widgets-debug
    Capture and crop page screenshot
    ...  settings-debug.png
    ...  id=formfield-form-widgets-debug

    Page should contain element  id=formfield-form-widgets-site_favicon
    Capture and crop page screenshot
    ...  settings-site_favicon.png
    ...  id=formfield-form-widgets-site_favicon

    Page should contain element  id=formfield-form-widgets-header_option
    Capture and crop page screenshot
    ...  settings-header_option.png
    ...  id=formfield-form-widgets-header_option

    Page should contain element  id=formfield-form-widgets-footer_option
    Capture and crop page screenshot
    ...  settings-footer_option.png
    ...  id=formfield-form-widgets-footer_option

    Page should contain element  id=formfield-form-widgets-color_option
    Capture and crop page screenshot
    ...  settings-color_option.png
    ...  id=formfield-form-widgets-color_option

    Page should contain element  id=formfield-form-widgets-pattern_option
    Capture and crop page screenshot
    ...  settings-pattern_option.png
    ...  id=formfield-form-widgets-pattern_option

    Page should contain element  id=formfield-form-widgets-layout_option
    Capture and crop page screenshot
    ...  settings-layout_option.png
    ...  id=formfield-form-widgets-layout_option

    Page should contain element  id=formfield-form-widgets-slogan
    Capture and crop page screenshot
    ...  settings-slogan.png
    ...  id=formfield-form-widgets-slogan

    Page should contain element  id=formfield-form-widgets-phone_number
    Capture and crop page screenshot
    ...  settings-phone_number.png
    ...  id=formfield-form-widgets-phone_number

    Page should contain element  id=formfield-form-widgets-email
    Capture and crop page screenshot
    ...  settings-email.png
    ...  id=formfield-form-widgets-email

    Page should contain element  id=formfield-form-widgets-hide_searchbox
    Capture and crop page screenshot
    ...  settings-hide_searchbox.png
    ...  id=formfield-form-widgets-hide_searchbox

    Page should contain element  id=formfield-form-widgets-slideshow_fullscreen
    Capture and crop page screenshot
    ...  settings-slideshow_fullscreen.png
    ...  id=formfield-form-widgets-slideshow_fullscreen

    Page should contain element  id=formfield-form-widgets-footer_text
    Capture and crop page screenshot
    ...  settings-footer_text.png
    ...  id=formfield-form-widgets-footer_text

    Page should contain element  id=formfield-form-widgets-hide_footer
    Capture and crop page screenshot
    ...  settings-hide_footer.png
    ...  id=formfield-form-widgets-hide_footer

    Page should contain element  id=formfield-form-widgets-colophon_text
    Capture and crop page screenshot
    ...  settings-colophon_text.png
    ...  id=formfield-form-widgets-colophon_text

    Page should contain element  id=formfield-form-widgets-hide_colophon
    Capture and crop page screenshot
    ...  settings-hide_colophon.png
    ...  id=formfield-form-widgets-hide_colophon
