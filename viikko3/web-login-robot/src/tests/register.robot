*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  helloworld123
    Confirm Password  helloworld123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  h
    Set Password  helloworld123
    Confirm Password  helloworld123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  ville
    Set Password  hello1
    Confirm Password  hello1
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  helloworld123
    Confirm Password  helloworld124
    Submit Credentials
    Register Should Fail With Message  The passwords do not match

*** Keywords ***
Create User And Go To Register Page
    Create User  foo  1234helloworld
    Go To Register Page
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}