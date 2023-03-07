from not_ui_helpers.assert_exception import AssertException
from pages import pase_selectors
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from not_ui_helpers.wait_service import WaitService


class BasePage:
    """
    Базовый класс всех страниц, содержащий общие методы для всех страниц. Не имеет url.
    """
    ELEM_TIMEOUT = 30

    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        self._browser = browser
        if browser is not None:
            self.url = browser.browser_config.get_browser_base_url()

    def open(self):
        """
        Открывает страницу по собственному url.
        """
        # self.assert_page_load()
        return self.open_url(self.url)

    def open_url(self, url):
        """
        Открывает заданный url на странице.

        :param url: открываемый url
        """
        if "http" not in url:
            url = "http://" + url
        self._browser.get_driver().get(url)
        return self

    def find_element(self, selector, timeout=ELEM_TIMEOUT):
        """
        Ищет элемент в течение заданного интервала.

        :param selector: селектор
        :param timeout: интервал, в течение которого элемент будет переискиваться, если не был сразу найден
        :return: найденный элемент, или исключение с причиной, почему элемент не найден
        """
        locator = self.get_locator(selector)
        return WaitService(timeout=timeout, ignored_except=WebDriverException).until(
            lambda driver: driver.find_element(*locator), "Ошибка при поиске элемента.",
            self._browser.get_driver())

    def find_element_safety(self, selector, timeout=ELEM_TIMEOUT):
        """
        Находит элемент, не выбрасывая Exception, если элемент не найден.

        :param selector: селектор для нахождения элемента
        :param timeout: время ожидания элемента
        :return: найденный элемент или None, если элемент не найден
        """
        try:
            return self.find_element(selector, timeout)
        except Exception:
            return None

    def click_element_safety(self, selector, timeout=ELEM_TIMEOUT):
        """
        Кликает на элемент, не выбрасывая Exception если кликнуть не удалось.

        :param selector: селектор для нахождения элемента
        :param timeout: время ожидания элемента
        """
        try:
            elem = self.find_element_safety(selector, timeout).click()
        except Exception:
            pass

    def click_element(self, selector, timeout=ELEM_TIMEOUT):
        """
        Кликает на элемент.

        :param selector: селектор
        :param timeout: интервал, в течение которого будут предприниматься попытки кликнуть на элемент
        """

        def click_element(driver):
            web_elem = driver.find_element(*self.get_locator(selector))
            if web_elem.get_attribute("disabled") is None:
                web_elem.click()
                return True
            else:
                raise WebDriverException("Element {0} is disabled".format(selector))

        self.elem_act_until(click_element, timeout)

    def click_with_move(self, selector, timeout=ELEM_TIMEOUT):
        """
        Смещает курсор в точку 0.0 и перемещает на элемент, после чего кликает на него.

        :param selector: селектор
        :param timeout: интервал, в течение которого будут предприниматься попытки кликнуть на элемент со смещением
        """

        def click_with_move(driver):
            action = ActionChains(driver)
            action.move_by_offset(0, 0)
            action.move_to_element(driver.find_element(*self.get_locator(selector))).perform()
            self.click_element(selector, 0)
            return True

        self.elem_act_until(click_with_move, timeout)

    def click_with_scroll(self, selector, timeout=ELEM_TIMEOUT):
        def click_with_scroll(driver):
            elem = driver.find_element(*self.get_locator(selector))
            driver.execute_script('arguments[0].scrollIntoView(true);', elem)
            self.click_element(selector, 0)
            return True

        self.elem_act_until(click_with_scroll, timeout)

    def move_to_element(self, selector, timeout=ELEM_TIMEOUT):
        """
        Перемещает курсор на элемент.

        :param selector: селектор элемента
        :param timeout: таймаут, в течение которого будет производится попытка переместить курсор на элемент
        """

        def move_to_element(driver):
            action = ActionChains(driver)
            action.move_to_element(driver.find_element(*self.get_locator(selector))).perform()
            return True

        self.elem_act_until(move_to_element, timeout)

    def scroll_to_element(self, selector, timeout=ELEM_TIMEOUT):
        """
        Скрол до элемента. Помещает элемент в верхнюю часть окна при проматывании.

        :param selector: селектор элемента
        :param timeout: таймаут, в течение которого будет производится попытка найти элемент
        """
        elem = self.find_element(selector, timeout)
        self.get_browser().get_driver().execute_script('arguments[0].scrollIntoView(true);', elem)

    def elem_act_until(self, elem_func, timeout=ELEM_TIMEOUT):
        """
        Вызывает функцию elem_func в течение интервала, игнорируя все исключения.
        Если функция не вернула значение, выбрасывает исключение.

        :param timeout: таймаут, в течение которого будет вызываться elem_func
        :param elem_func: функция без аргументов, которая будет вызываться
        """
        return WaitService(timeout=timeout, ignored_except=Exception). \
            until(elem_func, "Ошибка при взаимодействии с элементом.", self._browser.get_driver())

    def clear_input(self, selector):
        """
        Очищает текстовое поле input от содержимого.

        :param selector: селектор для нахождения элемента
        """
        self.find_element(selector).send_keys(Keys.CONTROL + "a" + Keys.DELETE)

    # def select_by_text(self, selector, text):
    #     """
    #     Выбирает элемент в выпадающем списке, находя его по тексту.
    #     """
    #     Select(self, selector).select_by_visible_text(text)
    #
    # def select_by_number(self, selector, number):
    #     """
    #     Выбирает элемент в выпадающем списке, находя его по порядоковому номеру в выпадающем списке (начиная с 0).
    #     """
    #     Select(self, selector).select_by_number(number)
    #
    # def select_yes_no_radio(self, radio_group_id, value=None, is_boolean_value=False, is_int_value=False):
    #     """
    #     Кликает на один из двух radiobutton ('yes' или 'no').
    #
    #     :param radio_group_id: идентификатор группы radiobutton
    #     :param value: если задан параметр ('yes' или 'no' true' или 'false'), кликает на соответствующую клавишу,
    #      иначе выбирает случайную и кликает по ней
    #     :param is_boolean_value: true определяет, что в качестве значения будет выбираться 'true', 'false' (а не 'yes', 'no')
    #     :param is_int_value: true определяет, что в качестве значения будет выбираться '0' или '1'
    #     :return: выбранное значение radiobutton, на который был произведен клик
    #     """
    #     if is_boolean_value:
    #         yes_no = ['true', 'false']
    #     elif is_int_value:
    #         yes_no = ['1', '0']
    #     else:
    #         yes_no = ['yes', 'no']
    #     if value is None:
    #         elem = random.choice(yes_no)
    #     else:
    #         elem = str(value).lower()
    #     self.click_element(selectors.Page.RADIO_BUTTON_WRAPPER.format(radio_group_id, elem))
    #     return elem

    # def add_custom_value_to_select(self, selector, value):
    #     """
    #     Добавляет свое значение в поле выпадающего списка.
    #
    #     :param selector: селектор для нахождения элемента
    #     :param value: добавляемое значение
    #     """
    #     Select(self, selector).add_custom_value(value)

    def is_presence_safety(self, selector, timeout=ELEM_TIMEOUT):
        """
        Проверяет присутствие элемента на странице, не выбрасывая исключение.

        :param timeout: максимальное время ожидания присутствия элемента
        :param selector: селектор для нахождения элемента
        """
        try:
            self.find_element(selector, timeout)
            return True
        except Exception:
            return False

    def is_presence(self, selector, timeout=ELEM_TIMEOUT):
        """
        Проверяет в течение интервала, если ли элемент на странице.
        Если за интервал элемент не появился на странице, выбрасывает Exception.

        :param selector: селектор
        :param timeout: таймаут, в течение которого будет проверяться присутствие элемента, пока он не появится
        """

        def is_presence(driver):
            driver.find_element(*self.get_locator(selector))
            return True

        try:
            return self.elem_act_until(is_presence, timeout)
        except Exception as ex:
            raise Exception(
                "Проверка присутствия элемента {1} на странице провалилась. {0} ".format(ex.args[0], selector))

    def is_no_presence(self, selector, load_dom_timeout=1, timeout=ELEM_TIMEOUT):
        """
        Проверяет в течение интервала, исчез ли элемент на странице.
        Если за интервал элемент не исчез на странице, выбрасывает Exception.

        :param selector: селектор
        :param load_dom_timeout: таймаут, в течение которого идет ожидание загрузки элементов страницы
        :param timeout: таймаут, в течение которого будет проверяться отсутстие элемента, пока он не исчезнет
        """

        def is_not_present(driver):
            try:
                self.is_presence(selector, load_dom_timeout)
            except Exception:
                return True

        try:
            return self.elem_act_until(is_not_present, timeout)
        except Exception:
            raise Exception("Проверка отсутствия элемента {0} на странице провалилась. ".format(selector))

    def is_no_presence_safety(self, selector, load_dom_timeout=1, timeout=ELEM_TIMEOUT):
        """
        Проверяет отсутствие элемента на странице в течение таймаута, пока элемент не исчезнет, не выбрасывая исключение.

        :param timeout: максимальное время ожидания исчезновения элемента
        :param load_dom_timeout: таймаут, в течение которого идет ожидание загрузки элементов DOM дерева
        :param selector: селектор для нахождения элемента
        """
        try:
            return self.is_no_presence(selector, load_dom_timeout, timeout)
        except Exception:
            return False

    def is_enabled_safety(self, selector, timeout=ELEM_TIMEOUT):
        """
        Проверяет, активирован элемент или нет на странице.

        :param timeout: максимальное время проверки
        :param selector: селектор для нахождения элемента
        """

        def is_enabled_safety(driver):
            if driver.find_element(*self.get_locator(selector)).get_attribute("disabled") is None:
                return True
            else:
                raise Exception(f'Элемент {selector} is disabled')

        try:
            return self.elem_act_until(is_enabled_safety, timeout)
        except Exception:
            return False

    # def fill_input(self, selector, text=None):
    #     """
    #     Заполняет текстовое поле текстом.
    #
    #     :param selector: селектор
    #     :param text: текст, который будет введен в текстовое поле
    #     """
    #     set_text = string_service.get_random_str() if text is None else text
    #     self.set_text(selector, set_text)
    #     return set_text

    def get_element_text(self, selector, timeout=ELEM_TIMEOUT):
        """
        :param selector: селектор
        :param timeout: таймаут, в течение которого будет ожидаться появление элемента на странице
        :return текст, внутри элемента (inner text)
        """
        return self.find_element(selector, timeout).text

    def get_attribute(self, selector, attr, timeout=ELEM_TIMEOUT):
        """
        Возвращает значение атрибута.

        :param selector: селектор
        :param attr: атрибут, значение которого надо возвратить
        :param timeout: таймаут, в течение которого будет ожидаться появление элемента на странице
        """
        return self.find_element(selector, timeout).get_attribute(attr)

    def get_value_attr(self, selector, timeout=ELEM_TIMEOUT):
        return self.get_attribute(selector, "value", timeout)

    def wait_contain_value(self, selector, expected_value, timeout=ELEM_TIMEOUT):
        """
        Ожидание, пока значение атрибута "value" элемента на странице не будет содержать в себе expected_value.

        :param selector: селектор
        :param expected_value: ожидаемое значение атрибута "value"
        :param timeout: максимальное время ожидания
        """
        return self.wait_contain_attribute_value(selector, "value", expected_value, timeout)

    def wait_input_value(self, selector, expected_value, timeout=ELEM_TIMEOUT):
        """
        Ожидание, пока в input не появится значение.

        :param selector: селектор для нахождения input wrapper
        :param expected_value: ожидаемое значение
        :param timeout: время ожидания значения
        """
        return self.wait_contain_value(selector + " input", expected_value, timeout)

    def wait_text_appear(self, selector, expected, timeout=ELEM_TIMEOUT):
        """
        Ожидание, пока текстовое содержимое элемента не будет равно ожидаемому тексту.

        :param selector: селектор
        :param expected: ожидаемый текст
        :param timeout: максимальное время ожидания
        """

        def wait_contain_text(driver):
            actual = self.get_element_text(selector, 0).replace(' ', '').replace('\n', '')
            if expected == actual:
                return AssertException(expected, expected)
            else:
                raise AssertException(expected, actual)

        try:
            expected = expected.replace(' ', '').replace('\n', '')
            return self.elem_act_until(wait_contain_text, timeout)
        except Exception as ex:
            if isinstance(ex.args[1], AssertException):
                return ex.args[1]
            else:
                return AssertException(expected, ex)

    def wait_contain_attribute_value(self, selector, attr, expected_value, timeout=ELEM_TIMEOUT):
        """
        Ожидание, пока значение атрибута attr не будет содержать в себе expected_value.

        :param selector: селектор
        :param attr: атрибут
        :param expected_value: ожидаемое значение атрибута
        :param timeout: максимальное время ожидания
        """

        def wait_contain_attribute(driver):
            actual_value = self.get_attribute(selector, attr, 0)
            if expected_value in actual_value:
                return AssertException(expected_value, expected_value)
            else:
                raise AssertException(expected_value, actual_value)

        try:
            return self.elem_act_until(wait_contain_attribute, timeout)
        except Exception as ex:
            if isinstance(ex.args[1], AssertException):
                return ex.args[1]
            else:
                return AssertException(expected_value, ex)

    def assert_page_load(self, msg="", timeout=ELEM_TIMEOUT):
        """
        Ожидание и проверка, что страница загрузилась.
        """
        pass
        self.assert_presence(pase_selectors.BasePage.APP, \
                             "Страница '{0}' не загрузилась".format(msg), timeout)

    def assert_exp_act(self, assert_exception, msg=""):
        """
        Проверка результата ожидания на странице.

        :param assert_exception: объект классса AssertException, возвращаемый методами not_url_page.wait...
        :param msg: сообщение, выдаваемое в случае несовпадения ожидаемого значения и фактического
        """
        assert assert_exception.expected == assert_exception.actual, msg + assert_exception.assert_msg

    #
    def assert_presence(self, selector, msg="", timeout=ELEM_TIMEOUT):
        """
        Ожидание и проверка присутсвия элемента на странице в течение таймаута.

        :param selector: селектор
        :param msg: сообщение, в случае отсутствия элемента на странице
        :param timeout: максимальное время ожидания
        :return: raise AssertionError если элемент не был найден за интервал timeout
        """
        try:
            self.is_presence(selector, timeout)
        except Exception as ex:
            raise AssertionError("{0}\n{1}".format(msg, ex.args[0]))

    def refresh_page(self):
        self.get_browser().refresh_page()

    def get_browser(self):
        return self._browser

    def get_url(self):
        return self._browser.get_driver().current_url

    def get_locator(self, selector):
        """
        :param selector: селектор
        :return: tuple - (как искать, селектор), созданный из поданного в качестве параметра селектора
        """
        if selector[0] == "/":
            return By.XPATH, selector
        else:
            return By.CSS_SELECTOR, selector
