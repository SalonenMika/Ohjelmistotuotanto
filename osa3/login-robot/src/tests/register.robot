*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  validuser  Valid1234!
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  existinguser  Valid1234!
    Output Should Contain  New user registered

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  us  Valid1234!
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  invalid@user  Valid1234!
    Output Should Contain  Username must only contain letters a-z

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  validuser  short
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  validuser  onlyletters
    Output Should Contain  Password must contain at least one non-letter character
