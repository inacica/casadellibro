from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from locators import Locators
from testData import TestData


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

    def click_enter(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.RETURN)

    def double_click(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        actionChains = ActionChains(self.driver)
        actionChains.double_click(element).perform()


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def search(self):
        self.double_click(Locators.SEARCH)
        self.enter_text(Locators.SEARCH, TestData.SEARCH_TERM)
        self.click_enter(Locators.ENTER_SEARCH)

    def filer_books(self):
        self.click(Locators.FILTER_BY)
        self.click(Locators.LANGUAGE)

    def select_book(self):
        self.click(Locators.SELECT_BOOK)


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def add_book(self):
        self.click(Locators.ADD_TO_CART)
        self.driver.implicitly_wait(5)

    def pay_book(self):
        self.click(Locators.PAY_BUTTON)


class CreateAccountAndPay(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def credentials(self):
        self.double_click(Locators.NAME)
        self.enter_text(Locators.NAME_FILL, TestData.NAME)
        self.double_click(Locators.SURNAME)
        self.enter_text(Locators.SURNAME_FILL, TestData.SURNAME)
        self.double_click(Locators.EMAIL)
        self.enter_text(Locators.EMAIL_FILL, TestData.EMAIL)
        self.double_click(Locators.PASSWORD)
        self.enter_text(Locators.PASSWORD_FILL, TestData.PASSWORD)

    def continue_button(self):
        self.click(Locators.CONTINUE_BUTTON)
        self.driver.implicitly_wait(5)

    def address(self):
        self.double_click(Locators.ADDRESS)
        self.enter_text(Locators.ADDRESS, TestData.ADDRESS)

    def postcode(self):
        self.double_click(Locators.POSTCODE)
        self.enter_text(Locators.POSTCODE, TestData.POSTCODE)

    def phone(self):
        self.double_click(Locators.PHONE)
        self.enter_text(Locators.PHONE, TestData.PHONE)

    def accept_policy(self):
        self.click(Locators.ACCEPT_POLICY)

    def final_pay(self):
        self.click(Locators.FINAL_PAY)

    def payment_error_message(self):
        assert self.driver.find_element(*Locators.PAYMENT_ERROR).text == TestData.ERROR_MESSAGE





