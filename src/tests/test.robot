*** Settings ***
Resource  resource.robot

*** Test Cases ***
Create New Tip
    Input 1 Command
    Input New Tip Name  newTip
    Input New Tip Url  newUrl
    Input 2 Command
    Run Application
    Output Should Contain  id:1 newTip, newUrl

