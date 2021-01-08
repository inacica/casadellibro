import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import Locators
from pages import HomePage, CartPage, CreateAccountAndPay


class Test_Search_Base(unittest.TestCase):

    def setUp(self):

        option = Options()
        option.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome('./chromedriver.exe', options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://www.casadellibro.com")
        self.driver.implicitly_wait(5)
        self.driver.find_element(*Locators.ACCEPT_COOKIES).click()
        self.driver.implicitly_wait(5)


class Test_Book_Search(Test_Search_Base):

    def setUp(self):
        super().setUp()

    def test_payment_error(self):
        '''Search for a book'''
        self.homePage = HomePage(self.driver)
        self.homePage.search()
        self.homePage.filer_books()
        self.homePage.select_book()

        '''Add the book to the cart and proceed paying'''
        self.cartPage = CartPage(self.homePage.driver)
        self.cartPage.add_book()
        self.cartPage.pay_book()

        '''Create an account and add all the data required, except the card details'''
        self.createAccount = CreateAccountAndPay(self.cartPage.driver)
        self.createAccount.credentials()
        self.createAccount.continue_button()
        self.createAccount.address()
        self.createAccount.postcode()
        self.createAccount.phone()
        time.sleep(1)
        self.createAccount.continue_button()
        time.sleep(1)
        self.createAccount.continue_button()
        time.sleep(1)
        self.createAccount.continue_button()
        time.sleep(1)
        self.createAccount.continue_button()
        time.sleep(1)
        self.createAccount.accept_policy()
        self.createAccount.final_pay()
        time.sleep(1)
        self.createAccount.payment_error_message()


if __name__ == "__main__":
    unittest.main()
