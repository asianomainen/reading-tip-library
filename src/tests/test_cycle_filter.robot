*** Settings ***
Resource  resource.robot

*** Test Cases ***
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