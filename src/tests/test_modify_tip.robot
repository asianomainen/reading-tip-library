*** Settings ***
Resource  resource.robot

*** Test Cases ***
Reading Tip Can Be Changed
    Create Tip
    Change Tip
    Input 2 Command
    Input x Command
    Run Application
    Output Should Contain  id:1 changedTip, www.test.test, tags: Book

Only Reading Tip Name Can Be Changed
    Create Tip
    Change Tip Name
    Input 2 Command
    Input x Command
    Run Application
    Output Should Contain  id:1 changedTip, www.test.test, tags: Book

Only Reading Tip Url Can Be Changed
    Create Tip
    Change Tip Url
    Input 2 Command
    Input x Command
    Run Application
    Output Should Contain  id:1 newTip, www.test.test, tags: Book

Changing Reading Tip With Empty Values Does Not Change Tip
    Create Tip
    Change Tip With Empty Values
    Input 2 Command
    Input x Command
    Run Application
    Output Should Contain  id:1 newTip, www.test.test, tags: Book