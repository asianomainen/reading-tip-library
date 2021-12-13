*** Settings ***
Resource  resource.robot

*** Test Cases **
Input h Displays Instructions
    Input h Command
    Input x Command
    Run Application
    Output Should Contain Help