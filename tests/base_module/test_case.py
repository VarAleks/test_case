from pages.check_box_page import CheckBoxPage
from pages.elements_page import ElementsPage
from pages.main_page import MainPage
from tests.test_base import TestBase


class TestClass(TestBase):
    def test_choose_word_file(self, browser):
        """
        Тестовый кейс
        """
        main_page = MainPage(browser).open()
        main_page.assert_page_load("Главная страница сайта")
        main_page.click_elements()

        elements_page = ElementsPage(browser)
        elements_page.should_be_elements_page()

        elements_page.click_check_box_in_menu()
        check_box_page = CheckBoxPage(browser)
        check_box_page.should_be_check_box_page()

        check_box_page.click_home_toggle()
        check_box_page.should_be_expand_home_tree()

        check_box_page.click_downloads_toggle()
        check_box_page.should_be_expand_download_tree()

        check_box_page.click_word_file_in_tree()
        check_box_page.should_be_text_selected_word_file()

