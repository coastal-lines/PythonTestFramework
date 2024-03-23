@my_tag_1
Feature:
  As an User
  I want to open browser
  Navigate into TestGorilla exam
  And validate some UI elements of the page

Background:
  Given open browser

@pytest.mark.ui
Scenario Outline: Validate exam UI elements
  Given navigate into exam page
  And maximize browser window
  When select answer number <item_number>
  Then answered item has <answered_item_colour> colour
  And question text is <question_text>

  Examples: Table
  |item_number|answered_item_colour   |question_text                                                     |
  |100        |("212", "16", "170")   |"What type of dependency should you set between these two tasks?" |