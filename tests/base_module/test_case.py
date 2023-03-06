from pages.elements_page import ElementsPage
from pages.main_page import MainPage
from tests.test_base import TestBase


class TestClass(TestBase):
    def test_sign_up_user(self, browser):
        """

        """
        main_page = MainPage(browser).open()
        main_page.assert_page_load("Главная страница сайта")
        main_page.click_elements()

        elements_page = ElementsPage(browser)
        elements_page.should_be_elements_page()


        pass


