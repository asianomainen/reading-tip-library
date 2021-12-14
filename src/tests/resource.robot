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

Input 8 Command
    Input  8

Input h Command
    Input  h

Input New Tip
    [Arguments]  ${name}  ${url}  ${tag}
    Input  ${name}
    Input  ${url}
    Input  ${tag}

Create Tip
    Input 1 Command
    Input New Tip  newTip  www.test.test  Book

Change Tip
    Input 3 Command
    Input  1
    Input New Tip  changedTip  www.test.test  Book

Change Tip Name
    Input 3 Command
    Input  1
    Input New Tip  changedTip  \  Book

Change Tip Url
    Input 3 Command
    Input  1
    Input New Tip  \  www.test.test  Book

Change Tip With Empty Values
    Input 3 Command
    Input  1
    Input New Tip  \  \  \

Create Three Tips
    Input 1 Command
    Input New Tip  newTip1  www.test.test  Book
    Input 1 Command
    Input New Tip  newTip2  www.test.test  Book
    Input 1 Command
    Input New Tip  newTip3  www.test.test  Book

Create Tip Without name
    Input 1 Command
    Input New Tip  \  www.test.test  Book
    
Create Tip Without url
    Input 1 Command
    Input New Tip  test  \  Book

Create Tip Without tag
    Input 1 Command
    Input New Tip  newTip  www.test.test  \

Create Tip With Invalid url
    Input 1 Command
    Input New Tip  test  ww.  Book

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

Change Tip Favourite Status
    [Arguments]  ${id}
    Input 8 Command
    Input  ${id}