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
    
