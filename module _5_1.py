class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        for i in range(1, int(new_floor)+1):
            if i <= new_floor and new_floor <= self.number_of_floors:
                print(i)
            else:
                print('"Такого этажа не существует"')
                break
h1 = House('ЖК Первый', 15)
h2 = House('ЖК Андреевский', 24)
h1.go_to(14)
h2.go_to(25)