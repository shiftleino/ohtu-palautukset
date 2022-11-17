*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  hello  hello1world
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  foo  hello1world
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  fo  hello1world
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  hello  hello1
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  hello  helloworld
    Output Should Contain  Invalid password

*** Keywords ***
Input New Command And Create User
    Create User  foo  helloworld123
    Input Command  new