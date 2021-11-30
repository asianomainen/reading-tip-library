*** Settings ***
Library  ../robotLibrary.py

*** Keywords ***
Input 1 Command
    Input  1

Input 2 Commands
    Input  2

Input New Tip
    [Arguments]  ${name}  ${url}
    Input  ${name}
    Input  ${url}
    Run Application
