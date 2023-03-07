from pages import pase_selectors
from pages.base_page import BasePage


class ElementsPage(BasePage):

    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)
        self.select = pase_selectors.ElementsPage

    def click_check_box_in_menu(self):
        self.click_element(self.select.CHECK_BOX_IN_MENU)

    def click_home_toggle(self):
        self.click_element(self.select.HOME_TREE_TOGGLE)

    def click_downloads_toggle(self):
        self.click_element(self.select.DOWNLOADS_TREE_TOGGLE)

    def click_word_file_in_tree(self):
        self.click_check_box_in_tree(pase_selectors.ID.WORD_FILE_IN_TREE)

    def click_check_box_in_tree(self, check_box_id):
        self.click_element(self.select.CHECK_BOX_TREE_LABEL.format(check_box_id))

    def should_be_success_text(self):
        self.assert_exp_act(self.wait_text_appear(self.select.RESULT_TEXT, "You have selected : wordFile"),
                            "Файл был выбран, но текст об успешном выборе файла не отобразился")

    def should_be_word_file_checked(self):
        self.assert_presence(self.select.CHECK_BOX_TREE_CHECKED.format(pase_selectors.ID.WORD_FILE_IN_TREE),
                             f"Чек бокс {pase_selectors.ID.WORD_FILE_IN_TREE} не поставился после клика на него")

    def should_be_expand_download_tree(self):
        self.assert_exp_act(
            self.wait_contain_attribute_value(self.select.DOWNLOADS_TREE_NODE, 'class', 'rct-node-expanded', 5),
            'Дерево DOWNLOAD не раскрылось')

    def should_be_expand_home_tree(self):
        self.assert_exp_act(
            self.wait_contain_attribute_value(self.select.HOME_TREE_NODE, 'class', 'rct-node-expanded', 5),
            'Дерево HOME не раскрылось')

    def should_be_tree_node(self):
        self.assert_presence(pase_selectors.ElementsPage.CHECK_BOX_TREE, "Дерево CheckBox не обнаружено на странице")

    def should_be_elements_page(self):
        self.assert_presence(pase_selectors.ElementsPage.MAIN_HEADER, "Страница Elements не загрузилась")
