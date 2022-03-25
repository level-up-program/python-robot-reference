*** Settings ***
Documentation     Example test cases using the data-driven testing approach.
...
...               The _data-driven_ style works well when you need to repeat
...               the same workflow multiple times.
...
...               Tests use ``Calculate`` keyword created in this file, that in
...               turn uses keywords in ``CalculatorLibrary.py``. An exception
...               is the last test that has a custom _template keyword_.
...
...               Notice that one of these tests fails on purpose to show how
...               failures look like.
Test Template     Calculate
Library           CalculatorLibrary.py

*** Test Cases ***    Expression    Expected
Addition              12,2          14
                      2,-3          -1


*** Keywords ***
Calculate
    [Arguments]    ${expression}    ${expected}
    Enters values  ${expression}
    Add
    Result should be    ${expected}
    Clear
