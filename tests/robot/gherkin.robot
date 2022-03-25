*** Settings ***
Documentation     Example test case using the gherkin syntax.
...
...               This test has a workflow similar to the keyword-driven
...               examples. The difference is that the keywords use higher
...               abstraction level and their arguments are embedded into
...               the keyword names.
...
...               This kind of _gherkin_ syntax has been made popular by
...               [http://cukes.info|Cucumber]. It works well especially when
...               tests act as examples that need to be easily understood also
...               by the business people.
Library           CalculatorLibrary.py

*** Test Cases ***
Addition operation works correctly
    Given calculator has been cleared
    When provided integers "1,2"
    and asked to calculate the sum
    Then result is "3"

*** Keywords ***
Calculator has been cleared
    Clear

Provided integers "${expression}"
    Enters values    ${expression}

Asked to calculate the sum
    Add

Result is "${result}"
    Result should be    ${result}
