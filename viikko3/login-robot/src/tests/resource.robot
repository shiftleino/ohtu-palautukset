*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Input Command
    [Arguments]  ${command}
    Input  ${command}