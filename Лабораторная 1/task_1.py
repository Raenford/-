import doctest


class character:
    def __init__(self, nickname: str, lvl: int, gameclass: int):
        # Предполагается деление классов по int, к примеру shaman == 1, warrior == 2. Допустим классов 6, уровней 60.
        """
        :param nickname: Имя персонажа
        :param lvl: Уровень персонажа
        :param gameclass: Класс персонажа

        Пример:
        >>> shammy = character("Jonny", 32, 1) # Инициализация экземпляра класса
        """
        if not isinstance(nickname, (str)):
            raise TypeError("Error type nickname")
        # later ctrl+C ctrl+v
        if not isinstance(gameclass, (int)):
            raise TypeError("Error type gameclass")
        if not isinstance(lvl, (int)):
            raise TypeError("Error type lvl")
        if 0 > lvl or lvl > 60:
            raise ValueError("Неверный параметр уровня")
        if 0 > gameclass or gameclass > 6:
            raise ValueError("Неверный параметр класса")

        self.level = lvl
        self.nn = nickname
        self.gclass = gameclass

    def switch_nickname(self, newnickname: str) -> None:
        ...
        """
        Меняет игровой ник
        :param newnickname: Новый ник
        """
    def level_UP(self):
        # Повышает уровень (level)
        ...

class favoritealcohol:
    def __init__(self, title: str, countrymaker: str, degree: float):
        # Предполагается деление классов по int, к примеру shaman == 1, warrior == 2. Допустим классов 6, уровней 60.
        """
        :param title: Название фирмы
        :param countrymaker: Страна изготовитель
        :param degree: Градус алкогольного напитка

        Пример:
        >>> JackDaniels = favoritealcohol("jack Daniel's", "USA", 40.5) # Инициализация экземпляра класса
        """
        if not isinstance(title, (str)):
            raise TypeError("Error type title")
        if not isinstance(countrymaker, (str)):
            raise TypeError("Error type gameclass")
        if not isinstance(degree, (float)):
            raise TypeError("Error type degree")
        if degree < 0 or degree > 99.99:
            raise ValueError("Error what a hell with degree?")

        self.name = title
        self.make = countrymaker
        self.GRADUS = degree

    def find_lowGRADUS(self):
        # Ищет самый высокий градус
        ...

    def delete_drink(self):
        # удаляет из любимых напиток
        ...

class cars:
    def __init__(self, brand: str, classauto: int, carmodel: str):
        # Что-то вроде вики по машинам, только написана студентом с 1-го курса
        """
        :param brand: Бренд
        :param classauto: Тип кузова в Int форме, по типу 1 - Хэтчбек, всего 8
        :param carmodel: Модель машины

        Пример:
        >>> Whatiscar = cars("reno", 5, "arcana") # Инициализация экземпляра класса
        """
        if not isinstance(brand, (str)):
            raise TypeError("Error type brand")
        if not isinstance(classauto, (int)):
            raise TypeError("Error type classauto")
        if not isinstance(carmodel, (str)):
            raise TypeError("Error type carmodel")
        if classauto < 0 or classauto > 8:
            raise ValueError("Неверный тип кузова")

        self.brand = brand
        self.type = classauto
        self.model = carmodel

    def find_brand(self, findbrand: str):
        # Ищет бренд
        ...

    def find_type(self, findtype: int):
        # ищет тип кузова
        ...

    def new_brand(self, newbrand: str, types: int, newcarmodel: None) -> None:
        # Добавляет новый бренд и возможно новую машину, или новую машину, по приходи администратора
        ...


if __name__ == "__main__":
    doctest.testmod()