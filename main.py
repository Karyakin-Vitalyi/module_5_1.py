# Домашняя работа по уроку "Атрибуты и методы объекта"

class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка, существует ли указанное количество этажей
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("'Такого этажа не существует'")
        else:
            # Вывод этажей от 1 до new_floor включительно
            for floor in range(1, new_floor + 1):
                print(floor)

# Пример использования класса
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)  # Ожидаемый вывод: 1 2 3 4 5
h2.go_to(10) # Ожидаемый вывод: "Такого этажа не существует"
