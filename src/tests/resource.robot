*** Settings ***
Library  ../robotLibrary.py

*** Keywords ***
Input 1 Command
    Input  1

Input 2 Command
    Input  2

Input 3 Command
    Input  3

Input 5 Command
    Input  5
    
Input 4 Command
    Input  4

Input x Command
    Input  x

Input 6 Command
    Input  6

Input 7 Command
    Input  7

Input h Command
    Input  h

Input New Tip
    [Arguments]  ${name}  ${url}
    Input  ${name}
    Input  ${url}

Create Tip
    Input 1 Command
    Input New Tip  newTip  www.test.test

Change Tip
    Input 3 Command
    Input  1
    Input New Tip  changedTip  www.test.test

Change Tip Name
    Input 3 Command
    Input  1
    Input New Tip  changedTip  \

Change Tip Url
    Input 3 Command
    Input  1
    Input New Tip  \  www.test.test

Change Tip With Empty Values
    Input 3 Command
    Input  1
    Input New Tip  \  \

Create Three Tips
    Input 1 Command
    Input New Tip  newTip1  www.test.test
    Input 1 Command
    Input New Tip  newTip2  www.test.test
    Input 1 Command
    Input New Tip  newTip3  www.test.test

Create Tip Without name
    Input 1 Command
    Input New Tip  \  www.test.test
    
Create Tip Without url
    Input 1 Command
    Input New Tip  test  \ 

Create Tip With Invalid url
    Input 1 Command
    Input New Tip  test  ww.

Remove Tip
    [Arguments]  ${id}
    Input 4 Command
    Input  ${id}

Change Tip Read Status
    [Arguments]  ${id}
    Input 6 Command
    Input  ${id}

Change Read Filter Setting
    Input 7 Command