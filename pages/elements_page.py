from pages import pase_selectors
from pages.base_page import BasePage


class ElementsPage(BasePage):
    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)

    def click_check_box_in_menu(self):
        self.click_element(pase_selectors.ElementsPage.CHECK_BOX_IN_MENU)

    def click_home_toggle(self):
        self.click_element(pase_selectors.ElementsPage.HOME_TREE_TOGGLE)

    def should_be_tree_node(self):
        self.assert_presence(pase_selectors.ElementsPage.CHECK_BOX_TREE, "Дерево CheckBox не обнаружено на странице")

    def should_be_elements_page(self):
        self.assert_presence(pase_selectors.ElementsPage.MAIN_HEADER, "Страница Elements не загрузилась")
