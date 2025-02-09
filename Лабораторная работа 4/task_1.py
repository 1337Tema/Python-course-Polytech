from typing import Union

class Car:
    """Базовый класс - Автомобили"""
    def __init__(self, name: str, power: Union[int, float], color: str):
        """
        Конструктор базового класса Car

        :param name: Название автомобиля
        :param power: Мощность автомобиля в л.с.
        :param color: Цвет автомобиля
        """
        self.name = name
        self.power = power
        self.color = color
    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Car
        """
        return f'Автомобиль "{self.name}" имеет мощность - {self.power} л.с. Цвет - {self.color}'
    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Car для отладки.
        """
        return f'{self.__class__.__name__}(name={self.name!r}, power={self.power!r}, color={self.color!r})'

    def change_color(self, new_color: str) -> None:
        """
        Изменяет цвет автомобиля.

        :param new_color: Новый цвет.
        """
        self.color = new_color

class PassengerCar(Car):
    """Дочерний класс - Легковые автомобили"""
    def __init__(self, name: str, power: Union[int, float], color: str, capacity: int):
        """
        Конструктор класса PassengerCar.
        Расширяет конструктор базового класса, добавляя атрибут capacity

        :param name: Название легкового автомобиля
        :param power: Мощность легкового автомобиля в л.с.
        :param color: Цвет легкового автомобиля
        :param capacity: Вместимость легкового автомобиля, чел
        """
        super().__init__(name, power, color)
        self.capacity = capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта PassengerCar.
        Перегружает метод __str__ базового класса.
        """
        return f'Легковой автомобиль "{self.name}" имеет мощность - {self.power} л.с., цвет - {self.color}, вместимость - {self.capacity} человек.'

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта PassengerCar для отладки.
        Перегружает метод __repr__ базового класса (добавляет атрибут вместимости).
        """
        return f'{self.__class__.__name__}(name={self.name!r}, power={self.power!r}, color={self.color!r}, passenger_capacity={self.capacity!r})'

class TruckCar(Car):
    """Дочерний класс - Грузовые автомобили"""

    def __init__(self, name: str, power: Union[int, float], color: str, load: Union[int, float]):
        """
        Конструктор класса TruckCar.
        Расширяет конструктор базового класса, добавляя атрибут load.

        :param name: Название грузового автомобиля.
        :param power: Мощность грузового автомобиля в л.с.
        :param color: Цвет грузового автомобиля.
        :param load: Грузоподъемность автомобиля в тоннах.
        """
        super().__init__(name, power, color)
        self.load = load

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта TruckCar.
        Перегружает метод __str__ базового класса.
        """
        return f'Грузовой автомобиль "{self.name}" имеет мощность - {self.power} л.с., цвет - {self.color}, грузоподъемность - {self.load} тонн.'

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта TruckCar для отладки.
        Перегружает метод __repr__ базового класса (добавляет атрибут грузоподъемности).
        """
        return f'{self.__class__.__name__}(name={self.name!r}, power={self.power!r}, color={self.color!r}, load_capacity={self.load!r})'

    def load_cargo(self, weight: Union[int, float]) -> str:
        """
        Загружает груз в грузовой автомобиль.

        :param weight: Вес груза в тоннах.
        :return: Сообщение об успешной или неуспешной загрузке.
        """
        if weight <= self.load:
            return f'В автомобиль "{self.name}" загружено {weight} тонн груза.'
        else:
            return f'Невозможно загрузить {weight} тонн груза в автомобиль "{self.name}". Превышена грузоподъемность ({self.load} тонн).'

if __name__ == "__main__":
    passenger_car = PassengerCar("Toyota Camry", 122, "red", 5)
    print(passenger_car)
    print(repr(passenger_car))
    passenger_car.change_color("silver")
    print(passenger_car)

    truck_car = TruckCar("Volvo FH16", 750, "white", 40)
    print(truck_car)
    print(repr(truck_car))
    print(truck_car.load_cargo(35))
    print(truck_car.load_cargo(50))
    pass
