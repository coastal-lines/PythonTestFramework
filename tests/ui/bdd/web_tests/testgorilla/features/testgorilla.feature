@allure.description("BDD tests")
Feature:
  As an User
  I want to open browser
  Navigate into TestGorilla exam
  And validate some UI elements of the page

Background:
  Given open browser

@allure.description("TC10")
Scenario Outline: Validate exam UI elements
  Given navigate into exam page
  And maximize browser window
  When select item number <item_number>
  Then answered item has <answered_item_colour> colour
  And question text is <question_text>

  Examples: Table
  |item_number|answered_item_colour   |question_text                                                     |
  |-1         |("212", "16", "170")   |What type of dependency should you set between these two tasks?   |

@allure.description("TC10")
Scenario: Validate question text
  When navigate into exam page
  Then question text is 'What type of dependency should you set between these two tasks?'

