*** Settings ***
Library     SeleniumLibrary
Variables   ../POM/locators.py

*** Variables ***
${UploadFiletest}        xpath=/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]
${AddFile}          C:\\Users\\KloverCloud\\Desktop\\file\\fil.png

#${AddFile}          upload//filpng.png


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
    sleep    10

    press keys      NONE    TAB
    sleep    1

    press keys      NONE    ENTER
    sleep    1

#    handle alert




#    RELOAD PAGE
#
#    press keys      NONE    ENTER
#    sleep    3

    wait until element is visible    ${Create_button}   120

    click element    ${Create_button}
    sleep    4

    press keys      NONE    TAB
    sleep    1

    press keys      NONE    ENTER
    sleep    4

    press keys      NONE    TAB
    sleep    1
    press keys      NONE    TAB
    sleep    1
    press keys      NONE    TAB
    sleep    1
    press keys      NONE    TAB
    sleep    1
    press keys      NONE    TAB
    sleep    1
    press keys      NONE    TAB
    sleep    1
    press keys      NONE    TAB
    sleep    1
    press keys      NONE    TAB
    sleep    1
    press keys      NONE    TAB
    sleep    5



#    Drag And Drop      file:${CURDIR}${/}${FILENAME}       id:demo-upload


#    Wait Until Page Contains Element   ${UploadFiletest}   60
#    sleep    2

#    Choose File     ${UploadFiletest}     ${AddFile}
#    sleep    10
#
#    press keys      NONE    TAB
#    sleep    2
#
#    press keys      NONE    TAB
#    sleep    2
#
#    press keys      NONE    ENTER
#    sleep    3

#    click element    ${next_button}
#    sleep    2
#
#    click element     ${next_button}
#    sleep    2
#
#    click element    ${next_button}
#    sleep    5

*** Keywords ***
Upload file
    Wait Until Page Contains Element   ${UploadFiletest}   60s
    scroll element into view    ${UploadFiletest}
    sleep    3
    Scroll Element Into View     ${UploadFiletest}
    Choose File     ${UploadFiletest}     ${AddFile}
    sleep    3