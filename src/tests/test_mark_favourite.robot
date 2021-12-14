*** Settings ***
Resource  resource.robot

*** Test Cases ***
Favourited Tip Shows Star
    Create Three Tips
    Change Tip Favourite Status  1
    Input 2 Command
    Input x Command
    Run Application
    Output Should Contain Favourited  id:1 newTip1, www.test.test, tags: Book
    