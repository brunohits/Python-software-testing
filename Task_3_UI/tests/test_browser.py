from Task_3_UI.page_objects import page
from Task_3_UI.page_objects.locators import MainPageLocators


class TestSurroundedRegions():
    def test_title_matches(self, browser):
        main_page = page.MainPage(browser)
        assert main_page.get_title() == 'App'

    def test_input_exists(self, browser):
        main_page = page.MainPage(browser)
        element = main_page.find_element(*MainPageLocators.INPUT)
        assert element is not None

    def test_case_match(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_input('[["X"]]')
        main_page.click_submit_button()
        results_page = page.ResultPage(browser)
        assert results_page.get_result() == "[['X']]"


