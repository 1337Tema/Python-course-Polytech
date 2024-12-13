import doctest
from typing import Union

class CarEngine:
    def __init__(self, engine_volume: Union[int, float], engine_name: str):
        """
        Создание и подготовка к работе объекта Машина

        :param engine_volume: Объём двигателя (л)
        :param engine_name: Название двигателя

        Примеры:
        >>> car_engine = CarEngine(6.4,"bmw")
        """
        if not isinstance(engine_volume, (int, float)):
            raise TypeError("Неверно задан тип данных для объёма двигателя")
        if engine_volume <= 0 or engine_volume > 20:
            raise ValueError("Неверно задан объём двигателя")
        self.engine_volume = engine_volume

        if not isinstance(engine_name, str):
            raise TypeError("Неверно задан тип данных для названия двигателя")
        self.engine_name = engine_name

    def sort_engine_volume(self) -> bool:
        """
        Функция, которая сортирует двигатели на малолитражные и крупнолитражные.

        :return: Является ли двигатель крупнолитражным(True) или малолитражным(False)

        Примеры:
        >>> car_engine1 = CarEngine(1.6, "Lada Vesta")
        >>> car_engine_fail = CarEngine("1.6", "Lada Vesta")
        >>> car_engine1.sort_engine_volume()
        """
        ...
    def edit_engine_volume(self, engine_volume) -> None:
        """
        Функция, которая позволяет изменить объём двигателя.

        :param engine_volume: Изменяемый объём двигателя (л).

        :raise ValueError: Если объём двигателя не соответствует требованиям, то
        возвращается ошибка

        :raise TypeError: Если тип данных объёма двигателя введен неверно, то
        возвращается ошибка

        :return: Измененный объём двигателя (л).

        Примеры:
        >>> car_engine2 = CarEngine(2, "Lada Vesta")
        >>> car_engine2.edit_engine_volume(2.4)
        """
        ...


class Furniture:
    def __init__(self,
                 material: str,
                 height: Union[int, float],
                 width: Union[int, float],
                 length: Union[int, float]):
        """
        Создание объекта Мебель.

        :param material: Материал мебели.
        :param height: Высота мебели (м).
        :param width: Ширина мебели (м).
        :param length: Длина мебели (м).

        Примеры:
        >>> table = Furniture("дерево", 0.75, 0.6, 1.6)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть задан как строка.")
        self.material = material

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть задана как число.")
        if height <= 0:
            raise ValueError("Высота должна быть положительной.")
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть задана как число.")
        if width <= 0:
            raise ValueError("Ширина должна быть положительной.")
        self.width = width

        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть задана как число.")
        if length <= 0:
            raise ValueError("Длина должна быть положительной.")
        self.length = length

    def move(self, new_location: str) -> None:
        """
        Перемещение мебели в новое место.

        :param new_location: Новое местоположение мебели.

        Примеры:
        >>> table = Furniture("дерево", 0.75, 1.2, 0.6)
        >>> table.move("гостиная")
        """
        ...

    def repair(self, damage_description: str) -> None:
        """
        Ремонт мебели.

        :param damage_description: Описание повреждения.

        Примеры:
        >>> chair = Furniture("металл", 0.9, 0.5, 1.5)
        >>> chair.repair("Сломана ножка")

        """
        ...

    def clean(self) -> None:
        """
        Очистка мебели, например, протирание от пыли.

        Примеры:
        >>> table = Furniture("дерево", 0.75, 1.2, 3.0)
        >>> table.clean()
        """
        ...
class SocialNetwork:
    def __init__(self, name: str, users_count: int):
        """
        Создание объекта Социальная сеть.

        :param name: Название социальной сети.
        :param users_count: Количество пользователей.

        Примеры:
        >>> facebook = SocialNetwork("Facebook", 2000000000)

        """

        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой.")
        self.name = name

        if not isinstance(users_count, int):
            raise TypeError("Количество пользователей должно быть целым числом.")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.users_count = users_count

    def add_user(self, user_id: int) -> None:
        """
        Добавление пользователя в социальную сеть.

        :param user_id: ID нового пользователя.

        :raise ValueError: Если ID нового пользователя не является целым числом, то
        возвращается ошибка

        :raise TypeError: Если тип данных ID нового пользователя неверный, то
        возвращается ошибка

        Примеры:
        >>> facebook = SocialNetwork("Facebook", 2000000000)
        >>> facebook.add_user(202)
        """
        ...

    def remove_user(self, user_id: int) -> None:
        """
        Удаление пользователя из социальной сети.

        :param user_id: ID удаляемого пользователя.

        :raise ValueError: Если ID пользователя не является целым числом, то
        возвращается ошибка

        :raise TypeError: Если тип данных ID пользователя неверный, то
        возвращается ошибка

        :raise Error: Если ID удаляемого пользователя не найден, то
        возвращается ошибка

        Примеры:
        >>> vk = SocialNetwork("Vkontakte", 10000000)
        >>> vk.remove_user(1337)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
