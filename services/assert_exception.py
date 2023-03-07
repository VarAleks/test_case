from selenium.common.exceptions import WebDriverException


class AssertException(WebDriverException):
    """
    Предназначен для выбрасывания exceptions с дополнительной информацией
    об ожидаемом и полученном значении в ходе проверки в тесте.
    """

    def __init__(self, expected, actual):
        super().__init__(msg="", screen=None, stacktrace=None)
        self.assert_msg = "\n\tExpected: {0}\n\tActual: {1}".format(expected, actual)
        self.expected = expected
        self.actual = actual
