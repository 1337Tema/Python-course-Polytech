class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}. Страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Длительность аудиокниги должна быть числом")
        if value <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительной")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()}. Длительность: {self.duration} ч."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"



book = Book("Мастер и Маргарита", "Булгаков")
print(book)
print(repr(book))

paper_book = PaperBook("Мертвые души", "Гоголь", 350)
print(paper_book)
print(repr(paper_book))

audio_book = AudioBook("Собачье сердце", "Булгаков", 4.5)
print(audio_book)
print(repr(audio_book))
