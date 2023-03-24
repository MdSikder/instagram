*** Settings ***
Library     SeleniumLibrary
Variables   ../POM/locators.py
Library  PyWindowsGuiLibrary

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


    wait until element is visible    ${Create_button}   120

    click element    ${Create_button}
    sleep    4

    click element    xpath=//button[text()='Select from computer']"
    sleep    3

    PyWindowsGuiLibrary.input text    C:\\Users\\KloverCloud\\PycharmProjects\\project\\WebBots\\instagram\\upload\\filpng.png
    sleep    2

#    pyautogui.typewrite("C:\\Users\\KloverCloud\\PycharmProjects\\project\\WebBots\\instagram\\upload\\filpng.png")

    press keys    ENTER

    sleep    3

    click element    ${next_button}
    sleep    2

    click element     ${next_button}
    sleep    2

    input text    ${write}
    sleep    4

    click element    ${share_button}}
    sleep    5

*** Keywords ***
Upload file
    Wait Until Page Contains Element   ${UploadFiletest}   60s
    scroll element into view    ${UploadFiletest}
    sleep    3
    Scroll Element Into View     ${UploadFiletest}
    Choose File     ${UploadFiletest}     ${AddFile}
    sleep    3