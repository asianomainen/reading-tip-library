*** Settings ***
Resource  resource.robot

*** Test Cases ***
Tip Can Be Created With Tag
    Create Tip
    Input x Command
    Run Application
    Database Should Contain Tips  1

Tip Can Be Created Without Tag
    Create Tip Without tag
    Input x Command
    Run Application
    Database Should Contain Tips  1