*** Settings ***
Resource  resource.robot

*** Test Cases ***
Tip Can Be Removed With Valid id
    Create Tip
    Remove Tip  1
    Input x Command
    Run Application
    Output Should Contain Colored  green  Tip removed

Tip Cannot Be Removed With Invalid id
    Create Tip
    Remove Tip  2
    Input x Command
    Run Application
    Output Should Contain Colored  red  Invalid ID

Tip Cannot Be Removed With Text
    Create Tip
    Remove Tip  Text
    Input x Command
    Run Application
    Output Should Contain Colored  red  Invalid ID