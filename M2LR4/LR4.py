from typing import Any


class Vehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация базового класса Vehicle.
        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля
        """
        self._brand = brand  # Закрытый атрибут, так как изменение марки автомобиля нежелательно
        self._model = model  # Закрытый атрибут, так как модель неизменяема
        self.year = year

    def __str__(self) -> str:
        return f"{self._brand} {self._model}, {self.year}"

    def __repr__(self) -> str:
        return f"Vehicle(brand='{self._brand}', model='{self._model}', year={self.year})"

    def start_engine(self) -> str:
        """
        Метод для запуска двигателя.
        """
        return "Двигатель запущен."


class Car(Vehicle):
    """
    Дочерний класс, представляющий легковой автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int, passengers: int) -> None:
        """
        Инициализация класса Car.
        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля
        :param passengers: Количество пассажирских мест
        """
        super().__init__(brand, model, year)
        self.passengers = passengers

    def __str__(self) -> str:
        return f"Легковой автомобиль {self._brand} {self._model}, {self.year}, пассажиров: {self.passengers}"

    def __repr__(self) -> str:
        return f"Car(brand='{self._brand}', model='{self._model}', year={self.year}, passengers={self.passengers})"

    def start_engine(self) -> str:
        """
        Перегруженный метод запуска двигателя.
        В легковых автомобилях обычно присутствует кнопочный или автоматический запуск.
        """
        return "Двигатель легкового автомобиля запущен кнопкой."


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 5)
    print(car)
    print(repr(car))
    print(car.start_engine())
