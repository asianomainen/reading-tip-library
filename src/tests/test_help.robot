*** Settings ***
Resource  resource.robot

*** Test Cases **
Input h Displays Instructions
    Input h Command
    Input x Command
    Run Application
    Output Should Contain Help

Print commands after every Input
    Input 2 Command
    Input x Command
    Run Application
    Output Should Contain Commands