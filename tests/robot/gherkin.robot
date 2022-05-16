*** Settings ***
Documentation     Example test case using the gherkin syntax.
Library           GameControllerLibrary.py

*** Test Cases ***
Game controller initialized with player name
    Given controller has been initialized
    When player is created with name "ArbitraryName"
    Then actual player name is "ArbitraryName"

Game controller initialized without player name
    Given controller has been initialized
    When player is created with name ""
    Then actual player name is "Player"

*** Keywords ***
Controller has been initialized
    Initialize controller

Player is created with name "${provided}"
    Create player with name   ${provided}

Actual player name is "${actual}"
    Player name should be   ${actual}
