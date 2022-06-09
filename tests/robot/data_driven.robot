*** Settings ***
Documentation     
...               Example test case using the data-driven (table) syntax.
...               http://arcbotics.com/wp-content/uploads/2015/12/sparki-driver-icon.png
...
Test Template     Start new game with player
Library           GameControllerLibrary.py


*** Test Cases ***      Provided     Actual
Provided player name    Arbitrary    Arbitrary
Blank player name       ${EMPTY}     Player


*** Keywords ***
Start new game with player
    [Arguments]    ${provided}    ${actual}
    Initialize controller
    Create player with name  ${provided}
    Player name should be    ${actual}
