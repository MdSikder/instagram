*** Settings ***
Library     SeleniumLibrary
Variables   ../POM/locators.py
Resource    ../Resources/keys.robot
Library           BuiltIn
Library           ImageHorizonLibrary



*** Variables ***
${UploadFiletest}           ${upload_button}
${AddFile}          C:\Users\KloverCloud\PycharmProjects\project\WebBots\instagram\upload\filpng.png


*** Test Cases ***
LogIn
    open browser    https://www.instagram.com/      chrome
    maximize browser window
    sleep    5

    input text    ${username}   usemany5@gmail.com
    sleep    1
    input text    ${password}   Qwer1234!!@@
    sleep    1
    click button    ${submit}
    sleep    5

    press keys      NONE    ENTER
    sleep    2

#    click button     ${notification}}
#    sleep    2

    wait until element is visible    ${Create_button}   120


    click element    ${Create_button}
    sleep    4

    Upload file

    click element    ${next_button}
    sleep    2

    click element     ${next_button}
    sleep    2

    click element    ${next_button}
    sleep    5

*** Keywords ***
Upload file
    Wait Until Page Contains Element   ${UploadFiletest}   60s
    click element   ${UploadFiletest}
    Choose File     UploadFiletest     AddFile
    sleep    10