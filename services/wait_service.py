import time


class WaitService:
    """
    Класс для выполнения действий в течение таймаута.
    """

    def __init__(self, timeout, poll_frequency=0.5, ignored_except=None):
        self._timeout = timeout
        self._poll = poll_frequency
        exceptions = list()
        try:
            exceptions.extend(iter(ignored_except))
        except TypeError:
            exceptions.append(ignored_except)
        self._ignored_exceptions = tuple(exceptions)

    def until(self, method, message="", *args):
        """
        Вызывает method в течение интервала, пока method не вернет not None значение.
        Если метод за интервал так и не выполнился (выкидывал Exceptions), пробрасываем их дальше.

        :param method: метод, который будет выполняться за интервал timeout
        :param message: сообщение, добавляемое к стеку, если method не смог выполнится за timeout (выкидывал Exceptions)
        :param args: аргументы, подаваемые в method
        """
        exception = None
        end_time = time.time() + self._timeout
        value = None
        while True:
            try:
                value = method(*args)
                if value is not None:
                    return value
            except self._ignored_exceptions as exc:
                exception = exc
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        if exception is not None:
            if message:
                raise Exception("{0} {1}".format(message, exception.args), exception)
            raise Exception(exception)
        elif value is None:
            raise Exception("method returned None value")

