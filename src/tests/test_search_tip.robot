*** Settings ***
Resource  resource.robot

*** Test Cases ***
Searching For Matching Name Works
    Input 1 Command
    Input New Tip  Reading Tip  www.test.test  Book
    Input 5 Command
    Input  Reading Tip
    Input x Command
    Run Application
    Output Should Contain  id:1 Reading Tip, www.test.test

Searching For Name With Missing Letter Works
    Input 1 Command
    Input New Tip  Reading Tip  www.test.test  Book
    Input 5 Command
    Input  Readng Tip
    Input x Command
    Run Application
    Output Should Contain  id:1 Reading Tip, www.test.test

Searching For Name With Extra Letter Works
    Input 1 Command
    Input New Tip  Reading Tip  www.test.test  Book
    Input 5 Command
    Input  Readiing Tip
    Input x Command
    Run Application
    Output Should Contain  id:1 Reading Tip, www.test.test

Searching For Name With Swapped Letters Works
    Input 1 Command
    Input New Tip  Reading Tip  www.test.test  Book
    Input 5 Command
    Input  Raeding Tip
    Input x Command
    Run Application
    Output Should Contain  id:1 Reading Tip, www.test.test

Searching For Something Different Works
    Input 1 Command
    Input New Tip  Reading Tip  www.test.test  Book
    Input 5 Command
    Input  Something
    Input x Command
    Run Application
    Output Should Not Contain  id:1 Reading Tip, www.test.test