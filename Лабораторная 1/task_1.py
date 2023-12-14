import doctest


class Character:
    def __init__(self, nickname: str, lvl: int, game_class: int):
        # Предполагается деление классов по int, к примеру shaman == 1, warrior == 2. Допустим классов 6, уровней 60.
        """
        :param nickname: Имя персонажа
        :param lvl: Уровень персонажа
        :param game_class: Класс персонажа

        Пример:
        >>> shammy = Character("Jonny", 32, 1) # Инициализация экземпляра класса
        """
        if not isinstance(nickname, (str)):
            raise TypeError("Error type nickname")
        # later ctrl+C ctrl+v
        if not isinstance(game_class, (int)):
            raise TypeError("Error type gameclass")
        if not isinstance(lvl, (int)):
            raise TypeError("Error type lvl")
        if 0 > lvl or lvl > 60:
            raise ValueError("Неверный параметр уровня")
        if 0 > game_class or game_class > 6:
            raise ValueError("Неверный параметр класса")

        self.level = lvl
        self.nick = nickname
        self.classes = game_class

    def switch_nickname(self, newnickname: str) -> None:
        ...
        """
        Меняет игровой ник
        :param newnickname: Новый ник
        """
    def level_up(self):
        # Повышает уровень (level)
        ...

class FavoriteAlcohol:
    def __init__(self, title: str, country_maker: str, degree: float):
        # Предполагается деление классов по int, к примеру shaman == 1, warrior == 2. Допустим классов 6, уровней 60.
        """
        :param title: Название фирмы
        :param country_maker: Страна изготовитель
        :param degree: Градус алкогольного напитка

        Пример:
        >>> jack_daniels = FavoriteAlcohol("jack Daniel's", "USA", 40.5) # Инициализация экземпляра класса
        """
        if not isinstance(title, (str)):
            raise TypeError("Error type title")
        if not isinstance(country_maker, (str)):
            raise TypeError("Error type gameclass")
        if not isinstance(degree, (float)):
            raise TypeError("Error type degree")
        if degree < 0 or degree > 99.99:
            raise ValueError("Error what a hell with degree?")

        self.name = title
        self.make = country_maker
        self.gradus = degree

    def find_low_gradus(self):
        # Ищет самый высокий градус
        ...

    def delete_drink(self):
        # удаляет из любимых напиток
        ...

class Cars:
    def __init__(self, brand: str, class_auto: int, car_model: str):
        # Что-то вроде вики по машинам, только написана студентом с 1-го курса
        """
        :param brand: Бренд
        :param class_auto: Тип кузова в Int форме, по типу 1 - Хэтчбек, всего 8
        :param car_model: Модель машины

        Пример:
        >>> what_is_car = Cars("reno", 5, "arcana") # Инициализация экземпляра класса
        """
        if not isinstance(brand, (str)):
            raise TypeError("Error type brand")
        if not isinstance(class_auto, (int)):
            raise TypeError("Error type classauto")
        if not isinstance(car_model, (str)):
            raise TypeError("Error type carmodel")
        if class_auto < 0 or class_auto > 8:
            raise ValueError("Неверный тип кузова")

        self.brand = brand
        self.type = class_auto
        self.model = car_model

    def find_brand(self, find_brand: str):
        # Ищет бренд
        ...

    def find_type(self, find_type: int):
        # ищет тип кузова
        ...

    def new_brand(self, new_brand: str, types: int, new_car_model: None) -> None:
        # Добавляет новый бренд и возможно новую машину, или новую машину, по приходи администратора
        ...


if __name__ == "__main__":
    doctest.testmod()
