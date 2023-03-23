*** Settings ***
Library     SeleniumLibrary
Variables   ../POM/locators.py





#*** Test Cases ***
#test
#    open browser    https://the-internet.herokuapp.com/upload   chrome
#    maximize browser window
#    sleep    3
#    click element    ${fil}
#    sleep    2
#    Choose File     ${fil}        C://filpng.png
#    sleep    5




*** Variables ***
${UploadFiletest}           xpath=//input[@id='file-upload']
${AddFile}          C://filpng.png

*** Test Cases ***
Test for Upload
    open browser    https://the-internet.herokuapp.com/upload   chrome
    sleep    4
    Upload file

*** Keywords ***
Upload file
    Wait Until Page Contains Element   ${UploadFiletest}   10s
    click element   ${UploadFiletest}
    sleep    2



    Choose File     ${UploadFiletest}     ${AddFile}
    sleep    2


#Choose File   ${PO_AddShell}    E://Project/Publish/SampleTest.1500/rose.jpg



#*** Variables ***
#${UploadFiletest}           css=[type='file']
#${AddFile}          C:/download.jpg
#*** Test Cases ***
#Test for Upload
#    Open Browser      https://imagetopdf.com/jpg-to-pdf    Chrome
#    Upload file
#*** Keywords ***
#Upload file
#    Wait Until Page Contains Element   ${UploadFiletest}   60s
#    Scroll Element Into View     ${UploadFiletest}
#    Choose File     ${UploadFiletest}     ${AddFile}