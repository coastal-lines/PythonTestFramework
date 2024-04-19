from pages.base_mobile_page import BaseMobilePage
from pages.mobile.aptitude.main_screen_page import MainScreenPage


def test_validate_test_ui(mobile_driver_wrapper):
    BaseMobilePage(mobile_driver_wrapper).open_application()

    # Step 1
    # Open 'Take A Test' dialog
    main_screen_page = MainScreenPage(mobile_driver_wrapper)
    take_a_test_dialog = main_screen_page.open_test_dialog()

    # Step 2
    # Open 'Select Test' page and select 'Test' type
    select_test_screen_page = take_a_test_dialog.select_test_type()
    choose_your_test_option_dialog = select_test_screen_page.select_test_and_start()

    # Step 3
    # Select 'Normal' option and take a test
    test_screen_page = choose_your_test_option_dialog.select_normal_option()

    # Step 4
    # Validate the question text
    expected_text = "The sum of ages of 5 children born at the intervals of 3 years each is 50 years. What is the age of the youngest child?"
    actual_text = test_screen_page.get_question_text()
    assert expected_text == actual_text
