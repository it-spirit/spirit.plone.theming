*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/server.robot
Resource  Selenium2Screenshots/keywords.robot

Variables  plone/app/testing/interfaces.py


*** Keywords ***

Setup
    Setup Plone site  spirit.plone.theming.testing.ACCEPTANCE_TESTING
    Import library  Remote  ${PLONE_URL}/RobotRemote

Teardown
    Teardown Plone Site


*** Variables ***

${FOLDER_ID}  a-folder
${DOCUMENT_ID}  a-document
