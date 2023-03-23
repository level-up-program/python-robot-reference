*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***         StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Valid Case #1              0             0             1                     NORTH         0           1           2
Invalid Case #2            0             0             5                     SOUTH         0           0           6
Valid Case #3              0             0             7                     EAST          1           0           8
Valid Case #4              0             0             9                     WEST          0           0           10
Inalid Case #5             9             9             13                    NORTH         9           9           14
Inalid Case #6             9             9             17                    SOUTH         9           8           18
Inalid Case #7             9             9             21                    EAST          9           9           22
Inalid Case #8             9             9             57                    WEST          8           9           58

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}
