from selenium.common import NoSuchElementException

from Task_3.page_objects.locators import MainPageLocators, SearchResultsPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def find_element(self, *locator):
        try:
            element = self.driver.find_element(*locator)
        except NoSuchElementException:
            return None


class MainPage(BasePage):

    def click_submit_button(self):
        element = self.find_element(*MainPageLocators.SUBMIT_BUTTON)
        element.click()

    def fill_input(self, data):
        element = self.find_element(*MainPageLocators.INPUT)
        element.send_keys(data)


class ResultPage(MainPage):
    def get_result(self):
        element = self.find_element(*SearchResultsPageLocators.RESULT)
        return element.text
