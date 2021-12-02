*** Settings ***
Resource  resource.robot

*** Test Cases ***
New Reading Tip Can Be Created
    Database Should Contain Tips  0
    Create Tip
    Run Application
    Database Should Contain Tips  1

New Reading Tip Cannot Be Created Without name
    Create Tip Without Name
    Run Application
    Output Should Contain  Name cannot be empty

Reading Tips Can Be Browsed
    Database Should Contain Tips  0
    Create Three Tips
    Input 2 Command
    Run Application
    Database Should Contain Tips  3
    Output Should Contain  id:1 newTip1, newUrl1
    Output Should Contain  id:2 newTip2, newUrl2
    Output Should Contain  id:3 newTip3, newUrl3

Reading Tip Can Be Changed
    Create Tip
    Change Tip
    Input 2 Command
    Run Application
    Output Should Contain  id:1 changedTip, changedUrl

Only Reading Tip Name Can Be Changed
    Create Tip
    Change Tip Name
    Input 2 Command
    Run Application
    Output Should Contain  id:1 changedTip, newUrl

Only Reading Tip Url Can Be Changed
    Create Tip
    Change Tip Url
    Input 2 Command
    Run Application
    Output Should Contain  id:1 newTip, changedUrl

Changing Reading Tip With Empty Values Does Not Change Tip
    Create Tip
    Change Tip With Empty Values
    Input 2 Command
    Run Application
    Output Should Contain  id:1 newTip, newUrl

