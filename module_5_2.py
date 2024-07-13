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
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f'Название:{self.name}, кол-во этажей: {self.number_of_floors}')

h1 = House('ЖК Первый', 15)
h2 = House('ЖК Андреевский', 24)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
