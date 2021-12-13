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
    Output Should Contain Colored  red  Name cannot be empty
    
New Reading Tip Cannot Be Created With Invalid url
    Create Tip With Invalid url
    Input x Command
    Input x Command
    Run Application
    Output Should Contain Colored  red  Invalid url

New Reading Tip Cannot Be Created Without url
    Create Tip Without url
    Input x Command
    Input x Command
    Run Application
    Output Should Contain Colored  red  Invalid url