*** Settings ***
Documentation     Test initialization of game. That character should be like https://raw.githubusercontent.com/level-up-program/python-robot-reference/main/tests/robot/images/gamerErin.png
Test Template     Start new game with character
Library           GameControllerLibrary.py

*** Test Cases ***      providedCharacterName      characterName      numPositions     startingPositionX    startingPositionY  startingMoveCount
Blank character name    ${EMPTY}                   Character          100              0                    0                  0


*** Keywords ***
Start new game with character
    [Arguments]    ${providedCharacterName}  ${characterName}  ${numPositions}  ${startingPositionX}  ${startingPositionY}  ${startingMoveCount}
    Initialize controller
    Create character with name         ${providedCharacterName}
    Character name should be           ${characterName}
    Number of map positions should be  ${numPositions}
    Starting X coordinate should be    ${startingPositionX}
    Starting Y coordinate should be    ${startingPositionY}
    Starting move count should be      ${startingMoveCount}
