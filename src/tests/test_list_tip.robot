*** Settings ***
Resource  resource.robot

*** Test Cases ***
Reading Tips Can Be Browsed
    Database Should Contain Tips  0
    Create Three Tips
    Input 2 Command
    Input x Command
    Run Application
    Database Should Contain Tips  3
    Output Should Contain  id:1 newTip1, www.test.test, tags: Book
    Output Should Contain  id:2 newTip2, www.test.test, tags: Book
    Output Should Contain  id:3 newTip3, www.test.test, tags: Book