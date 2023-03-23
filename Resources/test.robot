*** Settings ***
Library     SeleniumLibrary
Variables   ../POM/locators.py
Resource    ../Resources/keys.robot
Library           pyautogui
Library           ImageHorizonLibrary

#*** Variables ***
#${UploadFiletest}           xpath=//span[contains(text(),'Upload files')]
#${AddFile}          C:\Users\KloverCloud\PycharmProjects\project\WebBots\instagram\upload\filpng.png
#
#*** Test Cases ***
#Test for Upload
#    open browser    https://imagetopdf.com/jpg-to-pdf   chrome
#    Upload file
#
#*** Keywords ***
#Upload file
#    Wait Until Page Contains Element   ${UploadFiletest}   60s
#    click element   ${UploadFiletest}
#    Choose File     UploadFiletest     ${AddFile}

*** Variables ***
${UploadFiletest}           css=[type='file']
${AddFile}          C:/download.jpg
*** Test Cases ***
Test for Upload
    Open Browser      https://imagetopdf.com/jpg-to-pdf    Chrome
    Upload file
*** Keywords ***
Upload file
    Wait Until Page Contains Element   ${UploadFiletest}   60s
    Scroll Element Into View     ${UploadFiletest}
    Choose File     ${UploadFiletest}     ${AddFile}