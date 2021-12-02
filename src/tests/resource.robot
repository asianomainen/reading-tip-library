*** Settings ***
Library  ../robotLibrary.py

*** Keywords ***
Input 1 Command
    Input  1

Input 2 Command
    Input  2

Input New Tip
    [Arguments]  ${name}  ${url}
    Input  ${name}
    Input  ${url}

Create Tip
    Input 1 Command
    Input New Tip  newTip  newUrl

Create Three Tips
    Input 1 Command
    Input New Tip  newTip1  newUrl1
    Input 1 Command
    Input New Tip  newTip2  newUrl2
    Input 1 Command
    Input New Tip  newTip3  newUrl3

Create Tip Without name
    Input 1 Command
    Input New Tip  \  newUrl
    
