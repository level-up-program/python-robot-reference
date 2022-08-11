*** Settings ***
Documentation     Example test case using the data-driven (table) syntax.
Test Template     Start new game with character
Library           GameControllerLibrary.py

*** Test Cases ***      Provided     Actual
Arbitrary name          Trogdor      Trogdor
Blank character name    ${EMPTY}     Character


*** Keywords ***
Start new game with character
    [Arguments]    ${provided}    ${actual}
    Initialize controller
    Create character with name  ${provided}
    Character name should be    ${actual}
