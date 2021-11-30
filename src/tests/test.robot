*** Settings ***
Resource  resource.robot

*** Test Cases ***
No items when 0 items added
    Number Of Items  0

No Of Items 1 After Creating New Tip
    Input 1 Command
    Input New Tip Name  newTip
    Input New Tip Url  newUrl
    Number Of Items  1  

