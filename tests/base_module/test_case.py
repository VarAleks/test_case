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

        elements_page.click_check_box_in_menu()
        elements_page.should_be_tree_node()

        elements_page.click_home_toggle()
        elements_page.should_be_expand_home_tree()

        elements_page.click_downloads_toggle()
        elements_page.should_be_expand_download_tree()

        elements_page.click_word_file_in_tree()
        elements_page.should_be_success_text()

        pass


