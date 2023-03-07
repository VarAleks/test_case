from pages import pase_selectors
from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    """
    Страница CheckBox
    """

    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)
        self.select = pase_selectors.CheckBoxPage
        self.url = self.url + "/checkbox"

    def click_home_toggle(self):
        """
        Клик на элемент разворачивания дерева Home
        """
        self.click_element(self.select.HOME_TREE_TOGGLE)

    def click_downloads_toggle(self):
        """
        Клик на элемент разворачивания поддерева Downloads
        """
        self.click_element(self.select.DOWNLOADS_TREE_TOGGLE)

    def click_word_file_in_tree(self):
        """
        Клик на чек бокс водрд файла в дереве чекбоксов
        """
        self.click_check_box_in_tree(pase_selectors.ID.WORD_FILE_IN_TREE)

    def click_check_box_in_tree(self, check_box_id):
        """
        Клик на любой чекбокс в дереве чекбоксов
        :param check_box_id: айдишник чекбокса в дереве ДОМ
        """
        self.click_element(self.select.CHECK_BOX_TREE_LABEL.format(check_box_id))

    def should_be_text_selected_word_file(self):
        """
        Проверка отображнеия текста об успешности выбора ворд файла в дереве
        """
        self.assert_exp_act(self.wait_text_appear(self.select.RESULT_TEXT, "You have selected : wordFile"),
                            "Файл был выбран, но текст об успешном выборе файла не отобразился")

    def should_be_word_file_checked(self):
        """
        Проверка выбора ворд файла в дереве
        """
        self.assert_presence(self.select.CHECK_BOX_TREE_CHECKED.format(pase_selectors.ID.WORD_FILE_IN_TREE),
                             f"Чек бокс {pase_selectors.ID.WORD_FILE_IN_TREE} не поставился после клика на него")

    def should_be_expand_download_tree(self):
        """
        Проверка раскрытия элемента дерева download
        """
        self.assert_exp_act(
            self.wait_contain_attribute_value(self.select.DOWNLOADS_TREE_NODE, 'class', 'rct-node-expanded'),
            'Дерево DOWNLOAD не раскрылось')

    def should_be_expand_home_tree(self):
        """
        Проверка раскрытия дерева home
        """
        self.assert_exp_act(
            self.wait_contain_attribute_value(self.select.HOME_TREE_NODE, 'class', 'rct-node-expanded', 5),
            'Дерево HOME не раскрылось')

    def should_be_check_box_page(self):
        """
        Проверка, что страница checkbox загрузилась (дерево home присутствует на странице)
        """
        self.assert_presence(self.select.CHECK_BOX_TREE, "Страница CheckBox не загрузилась")
