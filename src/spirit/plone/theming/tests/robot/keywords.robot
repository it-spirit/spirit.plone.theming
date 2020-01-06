*** Settings ***

Resource  plone/app/robotframework/keywords3.robot

Library  Remote  ${PLONE_URL}/RobotRemote
Library  SeleniumLibrary
Library  SeleniumScreenshots


*** Variables ***

${FIXTURE}  spirit.plone.theming.testing.ACCEPTANCE_TESTING
@{DIMENSIONS}  1024  800
${RESOURCE_DIR}  ${CURDIR}

# ${BROWSER}  chrome

${FOLDER_ID}  a-folder
${DOCUMENT_ID}  a-document


*** Keywords ***

a logged-in manager
  Enable autologin as  Manager

a logged-in site administrator
  Enable autologin as  Site Administrator  Contributor  Reviewer
