import doctest


class Kitten:
    def __init__(self, name: str, weight: float, age: int):
        """
        Создание и подготовка к работе объекта "Котенок"
        :param name: Имя котенка
        :param weight: Вес котенка в килограммах
        :param age: Возраст котенка в целых годах
        Примеры:
        >>> kitten = Kitten("fifi", 4.2, 5)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя Котенка должно быть str")
        self.name = name

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть int или float")
        if weight <= 0:
            raise ValueError("Вес не может быть меньше или равен 0")
        self.weight = weight

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть int")
        if age < 0:
            raise ValueError("Возраст не может быть меньше 0")
        self.age = age

    def kitten_feed(self) -> bool:
        """
        Функция которая проверяет, кормили ли Котенка
        :return: Если котенок покормлен вернется Тrue。если нет - False
        Примеры:
        >>> kitten = Kitten("fifi", 4.2, 5)
        >>> kitten.kitten_feed()
        """
        ...

    def one_more_year(self) -> None:
        """
        Увеличение возраста котенка на 1 год.
        Примеры:
        >>> kitten = Kitten("fifi", 4.2, 5)
        >>> kitten.one_more_year()
        """

    def kitten_weight_groth(self, dif_weight: float) -> float:
        """
        Увеличение (уменьшение) веса котенка.
        :param dif_weight: Насколько котенок похудел (отрицательное число) или поправился (положительное число)
        :raise ValueError: Если dif_weight больше чем weight, текущий вес котенка
        то возвращается ошибка.
        :return: Новый вес котенка (на текущий момент)
        Примеры:
        >>> kitten = Kitten("fifi", 4.2, 5)
        >>> kitten.kitten_weight_groth(1.25)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class Weather:
    def __init__(self, temperature: float, pressure: float):
        """
        Создание и подготовка к работе объекта "Погода"
        :param temperature: температура воздуха в градусах Цельсия
        :param pressure: давление в мм ртутного столба
        Примеры:
        >>> deadly_hot_day = Weather(60, 760)  # инициализация экземпляра класса
        """
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть int или float")
        self.temperature = temperature

        if not isinstance(pressure, (int, float)):
            raise TypeError("Давление должно быть int или float")
        if pressure < 0:
            raise ValueError("Давление не может быть отрицательным числом")
        self.pressure = pressure

    def is_it_cold(self, cold_temperature: float) -> bool:
        """
        Функция которая проверяет холодно ли на улице, опустилась ли температура ниже определенного порогf
        :param: cold_temperature - порог температуры ниже которого погода считается холодной
        :return: На улице холод или нет
        Примеры:
        >>> weather = Weather(5, 760)
        >>> weather.is_it_cold(10)
        """
        ...

    def hypertonia(self, extra_pressure: float) -> bool:
        """
        Функция определеяет опасно ли повышение и понижение давления на улице на величина extra_pressure от текущего
        значения на улице для гипертоников
        :param extra_pressure: Повышение давление на улице, насколько она стала больше
        по сравнению с предыдущим измерением
        :return: опасно ли давление для гипертоников
        Примеры:
        >>> weather = Weather(5, 760)
        >>> weather.hypertonia(20)
        """
        if not isinstance(extra_pressure, (int, float)):
            raise TypeError("Повышение давления должно быть типа int или float")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class Car:
    def __init__(self, horse_powers: float, fuel_consumption: float):
        """
        Создание и подготовка к работе объекта "Машина"
        :param horse_powers: Колличество лошадиных сил
        :param fuel_consumption: Расход топлива в литрах на 100 км
        Примеры:
        >>> lada = Car(60, 10)  # инициализация экземпляра класса
        """
        if not isinstance(horse_powers, (int, float)):
            raise TypeError("Мощность должна быть типа int или float")
        if horse_powers <= 0:
            raise ValueError("Мощность должна быть положительным числом")
        self.horse_powers = horse_powers

        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if fuel_consumption <= 0:
            raise ValueError("Расход топливадолжен быть положительным числом")
        self.fuel_consumption = fuel_consumption

    def distance(self, tau) -> float:
        """
        Функция которая показывает путь который преодалеет автомобиль за tau часов
        :return: Путь пройденный автомомбилем
        Примеры:
        >>> lada = Car(60, 10)
        >>> lada.distance(10)
        """
        if not isinstance(tau, (int, float)):
            raise TypeError("Время должно быть int или float")
        if tau <= 0:
            raise ValueError("Время должно быть положительным числом")
        ...

    def turbo(self, power: float) -> float:
        """
        Функция находит какого будет изменение расхода топлива при изменении мощности на величину power.
        :param power: величина на которую будет увеличина (со знаком плюс) или
        уменьшена (со знаком минус) мощность автомобиля
        Примеры:
        >>> lada = Car(60, 10)
        >>> lada.turbo(30)
        """
        if not isinstance(power, (int, float)):
            raise TypeError("Добавляемая мощность должна быть типа int или float")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
