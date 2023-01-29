if __name__ == "__main__":

    class Weapon:
        def __init__(self, name: str, number: int):
            """
            Создание и подготовка к работе объекта "оружие" класса Weapon
            :param name: Название боевой единицы, оно не должно меняться поэтому этот параметр не публичны,
            имеет getter и не имеет setter
            :param number: колличество произведенных боевых единиц, чтобы пользователь не использовал некорректные типы
            данных устанавливаем getter setter для проверки корректности
            Примеры:
            >>> gun = Weapon("пистолет Glock", 5000)  # инициализация экземпляра класса
            """

            if not isinstance(name, str):
                raise TypeError('название должно быть str')
            self._name = name

            if not isinstance(number, int):
                raise TypeError('колличество должно быть int')
            if number < 0:
                raise ValueError("Колличество не может быть отрицательным")
            self._number = number

        @property
        def name(self):
            return self._name

        @property
        def number(self):
            return self._number

        @number.setter
        def number(self, number: int) -> None:
            if not isinstance(number, int):
                raise TypeError
            if number < 0:
                raise ValueError
            self._number = number

        def __str__(self) -> str:
            return f'Боевая единица "{self.name}", Колличество: {self.number}'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(name={self.name!r}, number={self.number})'

        @staticmethod
        def kinetic_energy(mass: float, speed: float) -> str:
            """
            статический метод который позволяет найти кинетическую энергию снаряда выпущенного из оружия
            если извесны его масса и скорость
            :param mass: масса снаряда, положительное число килограмм
            :param speed: скорость снаряда в метрах в секунду
            :raise ValueError: если масса отрицательна то возвращается ошибка.
            :return: кинетическая энергия снаряда с данными параметрами в джоулях
            Примеры:
            >>> gun = Weapon("пистолет Glock", 5000)
            >>> gun.kinetic_energy(0.01, 400)
            """
            if not isinstance(mass, (float, int)):
                raise TypeError
            if mass < 0:
                raise ValueError
            if not isinstance(speed, (float, int)):
                raise TypeError
            return f'энергия снаряда: {mass*speed**2} Джоулей'

        def increase_number(self, difference: int) -> None:
            """
            метод который позволяет увеличить (со знаком +) или уменьшить (со знаком -)
            на величину difference колличество боевых единиц
            :param difference: насколько изменилось колличество
            :raise ValueError: если колличество уменьшилось на величину большую чем изначально было боевых единиц
            Примеры:
            >>> gun = Weapon("пистолет Glock", 5000)
            >>> gun.increase_number(100)
            """
            if not isinstance(difference, int):
                raise TypeError
            if -difference > self._number:
                raise ValueError
            self._number += difference

    class Firearms(Weapon):
        def __init__(self, name: str, number: int, caliber: str):
            """
            Создание и подготовка к работе объекта "огнестрельное оружие" класса Firearms подкласса Weapon
            :param number и name: наследуются из родительского класса
            :param caliber калибр пули огнестрельного оружия
            Примеры:
            >>> AK47 = Firearms("Автомат АК-47", 50000, "7,62 мм")  # инициализация экземпляра класса
            """
            super().__init__(name=name, number=number)
            if not isinstance(caliber, (float, str)):
                raise TypeError
            self._caliber = caliber
            """наследуем конструктор родительского класса"""

        @property
        def caliber(self):
            return self._caliber

        @caliber.setter
        def caliber(self, caliber: str) -> None:
            if not isinstance(caliber, str):
                raise TypeError
            self._caliber = caliber

        """Перегружаем магические методы __str__ и __repr__"""
        def __str__(self) -> str:
            return f'Огнестрельное оружие "{self.name}", Колличество: {self.number}, Калибр: {self.caliber}'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(name={self.name!r}, number={self.number}, caliber={self.caliber!r})'
        """наследуем пользовательский метод increase_number"""
        def increase_number(self, difference: int) -> None:
            super().increase_number(difference)
        """Перегружаем метод с целью изменить сообщение для пользователя"""
        def kinetic_energy(self, mass: float, speed: float) -> str:
            if not isinstance(mass, (float, int)):
                raise TypeError
            if mass < 0:
                raise ValueError
            if not isinstance(speed, (float, int)):
                raise TypeError
            return f'энергия пули калибра {self._caliber}: {mass*speed**2} Джоулей'

    class Explosives(Weapon):
        def __init__(self, name: str, number: int, explosive_power: float):
            """
            Создание и подготовка к работе объекта "взрывчатое вещество" класса Explosives подкласса Weapon
            :param number и name: наследуются из родительского класса
            :param explosive_power сила взрыва в Джоулях
            Примеры:
            >>> C4 = Explosives("Пластид СИ-4", 500, "30000000000")  # инициализация экземпляра класса
            """
            super().__init__(name=name, number=number)
            if not isinstance(explosive_power, (float, int)):
                raise TypeError
            if explosive_power < 0:
                raise ValueError
            self._explosive_power = explosive_power

        @property
        def explosive_power(self):
            return self._explosive_power

        @explosive_power.setter
        def explosive_power(self, explosive_power: float) -> None:
            if not isinstance(explosive_power, (float, int)):
                raise TypeError
            if explosive_power < 0:
                raise ValueError
            self.explosive_power = explosive_power

        def __str__(self) -> str:
            return f'Взрывчатое вещество "{self.name}", Колличество: {self.number}, Сила взрывa: {self.explosive_power}'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(name={self.name!r}, ' \
                   f'number={self.number}, explosive_power={self.explosive_power})'

        def increase_number(self, difference: int) -> None:
            super().increase_number(difference)

        """Перегружаем метод kinetic_energy чтобы изменить метод подсчета"""
        def kinetic_energy(self, mass: float, effectivity: float) -> str:
            """
            функция отличается от функции базового класса только методом подсчета и аргументом
            :param effectivity какая доля энергии передается осколку от 0 до 1
            :param mass имеет тот же смыл массы осколка
            """
            if not isinstance(mass, (float, int)):
                raise TypeError
            if mass < 0:
                raise ValueError
            if not isinstance(effectivity, (float, int)):
                raise TypeError
            if effectivity < 0 or effectivity > 1:
                raise ValueError
            return f'энергия осколка: {mass*effectivity*self.explosive_power} Джоулей'

    pass
