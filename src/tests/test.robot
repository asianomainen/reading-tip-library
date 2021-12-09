*** Settings ***
Resource  resource.robot

*** Test Cases ***
New Reading Tip Can Be Created
    Database Should Contain Tips  0
    Create Tip
    Input x Command
    Run Application
    Database Should Contain Tips  1

New Reading Tip Cannot Be Created Without name
    Create Tip Without Name
    Input x Command
    Run Application
    Output Should Contain  Name cannot be empty
    
New Reading Tip Cannot Be Created With Invalid url
    Create Tip With Invalid url
    Input x Command
    Input x Command
    Run Application
    Output Should Contain  Invalid url

New Reading Tip Cannot Be Created Without url
    Create Tip Without url
    Input x Command
    Input x Command
    Run Application
    Output Should Contain  Invalid url

Reading Tips Can Be Browsed
    Database Should Contain Tips  0
    Create Three Tips
    Input 2 Command
    Input x Command
    Run Application
    Database Should Contain Tips  3
    Output Should Contain  id:1 newTip1, www.test.test
    Output Should Contain  id:2 newTip2, www.test.test
    Output Should Contain  id:3 newTip3, www.test.test

Reading Tip Can Be Changed
    Create Tip
    Change Tip
    Input 2 Command
    Input x Command
    Run Application
    Output Should Contain  id:1 changedTip, www.test.test

Only Reading Tip Name Can Be Changed
    Create Tip
    Change Tip Name
    Input 2 Command
    Input x Command
    Run Application
    Output Should Contain  id:1 changedTip, www.test.test

Only Reading Tip Url Can Be Changed
    Create Tip
    Change Tip Url
    Input 2 Command
    Input x Command
    Run Application
    Output Should Contain  id:1 newTip, www.test.test

Changing Reading Tip With Empty Values Does Not Change Tip
    Create Tip
    Change Tip With Empty Values
    Input 2 Command
    Input x Command
    Run Application
    Output Should Contain  id:1 newTip, www.test.test

Searching For Matching Name Works
    Input 1 Command
    Input New Tip  Reading Tip  www.test.test
    Input 5 Command
    Input  Reading Tip
    Input x Command
    Run Application
    Output Should Contain  id:1 Reading Tip, www.test.test

Searching For Name With Missing Letter Works
    Input 1 Command
    Input New Tip  Reading Tip  www.test.test
    Input 5 Command
    Input  Readng Tip
    Input x Command
    Run Application
    Output Should Contain  id:1 Reading Tip, www.test.test

Searching For Name With Extra Letter Works
    Input 1 Command
    Input New Tip  Reading Tip  www.test.test
    Input 5 Command
    Input  Readiing Tip
    Input x Command
    Run Application
    Output Should Contain  id:1 Reading Tip, www.test.test

Searching For Name With Swapped Letters Works
    Input 1 Command
    Input New Tip  Reading Tip  www.test.test
    Input 5 Command
    Input  Raeding Tip
    Input x Command
    Run Application
    Output Should Contain  id:1 Reading Tip, www.test.test

Searching For Something Different Works
    Input 1 Command
    Input New Tip  Reading Tip  www.test.test
    Input 5 Command
    Input  Something
    Input x Command
    Run Application
    Output Should Not Contain  id:1 Reading Tip, www.test.test

Tip Can Be Removed With Valid id
    Create Tip
    Remove Tip  1
    Input x Command
    Run Application
    Output Should Contain  Tip removed

Tip Cannot Be Removed With Invalid id
    Create Tip
    Remove Tip  2
    Input x Command
    Run Application
    Output Should Contain  Invalid ID

Tip Cannot Be Removed With Text
    Create Tip
    Remove Tip  Text
    Input x Command
    Run Application
    Output Should Contain  Invalid ID

Changed Read Status Shows In List
    Create Three Tips
    Change Tip Read Status  1
    Change Read Filter Setting
    Change Read Filter Setting
    Input 2 Command
    Input x Command
    Run Application
    Output Should Contain  id:1 newTip1, www.test.test

Filtering Tips Out From List
    Create Three Tips
    Change Tip Read Status  1
    Change Read Filter Setting
    Input 2 Command
    Input x Command
    Run Application
    Output Should Not Contain  id:1 newTip1, www.test.test

Filtering Tips Out From Search
    Create Three Tips
    Change Tip Read Status  1
    Change Read Filter Setting
    Input 5 Command
    Input  nweTip1
    Input x Command
    Run Application
    Output Should Not Contain  id:1 newTip1, www.test.test

Filtered Tip Shows In Search
    Create Three Tips
    Change Tip Read Status  1
    Change Read Filter Setting
    Change Read Filter Setting
    Input 5 Command
    Input  nweTip1
    Input x Command
    Run Application
    Output Should Contain  id:1 newTip1, www.test.test