from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SUBMIT_BUTTON = (By.ID, 'submit')
    INPUT = (By.ID, 'input')
    PAGE_TITLE = (By.TAG_NAME, 'title')


class SearchResultsPageLocators(object):
    RESULT = (By.ID, 'result')
