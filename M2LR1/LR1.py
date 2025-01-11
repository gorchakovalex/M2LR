import doctest

class Phone: # телефон
        """
        Класс описывает модель смартфона
        """
        def __init__(self, charging_percentage: int, screen_brightness: int):
            """
                    Создание и подготовка к работе объекта "Телефон"

                    :param charging_percentage: процент зарядки
                    :param screen_brightness: яркость экрана

                    Примеры:
                    >>> phone = Phone(100, 50)  # инициализация экземпляра класса
                    """
            if not isinstance(charging_percentage, int):
                raise TypeError("Процент зарядки должен быть типа int")
            if charging_percentage <= 0:
                raise ValueError("Процент зарядки должен быть положительным числом")
            if charging_percentage > 100:
                raise ValueError("Процент зарядки не может быть больше 100%")
            self.charging_percentage = charging_percentage # атрибут процента зарядки

            if not isinstance(screen_brightness, int):
                raise TypeError("Процент яркости экрана должен быть типа int")
            if screen_brightness <= 0:
                raise ValueError("Процент яркости экрана должен быть положительным числом")
            if screen_brightness > 100:
                raise ValueError("Процент яркости экрана не может быть больше 100%")
            self.screen_brightness = screen_brightness # атрибут яркости экрана

        def is_phone_charged(self) -> int:
            """
                    Функция которая проверяет процент зарядки на телефоне

                    :return: сколько процентов зарядки

                    Примеры:
                    >>> phone = Phone(100, 50)
                    >>> phone.is_phone_charged()
                    """
            ...
        def is_phone_bright(self) -> int:
            """
                    Функция которая проверяет проверяет процент яркости

                    :return: сколько процентов яркости

                    Примеры:
                    >>> phone = Phone(100, 50)
                    >>> phone.is_phone_bright()
                    """
            ...



class Printer:
    """
            Класс описывает модель принтера
            """
    def __init__(self, color_percentage: int, wifi_connection: bool):
        """
                          Создание и подготовка к работе объекта "Принтер"

                          :param color_percentage: количество чернил
                          :param wifi_connection: подключение к wifi

                          Примеры:
                          >>> printer = Printer(100, True)  # инициализация экземпляра класса
                          """
        if not isinstance(color_percentage, int):
            raise TypeError("Процент количества чернил должен быть типа int")
        if color_percentage <= 0:
            raise ValueError("Процент количества чернил быть положительным числом")
        if color_percentage > 100:
            raise ValueError("Процент количества чернил не может быть больше 100%")
        self.color_percentage = color_percentage

        if not isinstance(wifi_connection, bool):
            raise TypeError("Подключение принтера должно быть типа bool")
        self.wifi_connection = wifi_connection

    def is_printer_charged(self) -> int:  # проверяет количество чернил
        """
                             Функция которая проверяет количество чернил

                             :return: Количество процентов чернил

                            Примеры:
                            >>> printer = Printer(100, True)
                            >>> printer.is_printer_charged()
                            """
        ...

    def is_printer_connected(self) -> bool:  # проверяет подключение
        """
                            Функция которая проверяет подключение к wifi

                            :return: Подключен ли принтер

                            Примеры:
                            >>> printer = Printer(100, True)
                            >>> printer.is_printer_connected()
                            """
        ...

class WashingMachine:
    """
            Класс описывает модель стиральной машины
            """
    def __init__(self, washing_time: int, door_closed: bool):
        """
                          Создание и подготовка к работе объекта "Стиральная машина"

                          :param washing_time: сколько времени будет стирка в минутах
                          :param door_closed: закрыта ли дверь стиральной машины

                          Примеры:
                          >>> washingmachine = WashingMachine(100, True)  # инициализация экземпляра класса
                          """
        if not isinstance(washing_time, int):
            raise TypeError("Количества минут должно быть типа int")
        if washing_time <= 0:
            raise ValueError("Количества минут должно быть положительным числом")
        self.washing_time = washing_time

        if not isinstance(door_closed, bool):
            raise TypeError("Закрыта ли дверь должно быть типа bool")
        self.door_closed = door_closed

    def time_of_washing(self) -> int:  # время стирки
        """
                             Функция которая узнает время стирки

                             :return: Количество минут

                            Примеры:
                            >>> washingmachine = WashingMachine(100, True)
                            >>> washingmachine.time_of_washing()
                            """
        ...

    def is_door_closed(self) -> bool:
        """
                            Функция которая проверяет закрыта ли дверца

                            :return: Закрыта ли дверца

                            Примеры:
                            >>> washingmachine = WashingMachine(100, True)
                            >>> washingmachine.is_door_closed()
                            """
        ...

if __name__ == "__main__":
    doctest.testmod()