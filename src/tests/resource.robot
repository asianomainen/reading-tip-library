*** Settings ***
Library  ../robotLibrary.py

*** Keywords ***
Input 1 Command
    Input  1

Input 2 Commands
    Input  2

Input New Tip Name
    [Arguments]  ${name}
    Input  ${name}

Input New Tip Url
    [Arguments]  ${url}
    Input  ${url}
