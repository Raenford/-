from typing import Any


if __name__ == "__main__":

    class AnyNetwork:
        """
        Базовый класс для социальных сетей.
        """

        def __init__(self, name: str):
            self.name = name

        def __str__(self) -> str:
            return f"Социальная сеть: {self.name}"

        def __repr__(self) -> str:
            return f"AnyNetwork(name={self.name})"


    class VK(AnyNetwork):
        """
        Класс для социальной сети ВКонтакте.
        """

        def __init__(self, name: str, user_id: int):
            super().__init__(name)
            self.user_id = user_id

        def __str__(self) -> str:
            return f"Социальная сеть: {self.name}, ID пользователя: {self.user_id}"

        def __repr__(self) -> str:
            return f"VK(name={self.name}, user_id={self.user_id})"


    class Facebook(AnyNetwork):
        """
        Класс для социальной сети Facebook.
        """

        def __init__(self, name: str, username: str):
            super().__init__(name)
            self.username = username

        def __str__(self) -> str:
            return f"Социальная сеть: {self.name}, Имя пользователя: {self.username}"

        def __repr__(self) -> str:
            return f"Facebook(name={self.name}, username={self.username})"

    pass
