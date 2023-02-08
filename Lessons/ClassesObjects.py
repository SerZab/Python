class Person:
    def print_info(self, n):
        for i in range(n):
            print(f"Name: {self.name}, Surname: {self.surname}, Place of birth: {self.place_of_birth}")
    def get_age(self, current_year):
        print(f"Age: {current_year - self.year_birth}")


p1 = Person()
p1.name = "Elon"
p1.surname = "Mask"
p1.place_of_birth = "UAR"
p1.year_birth = 1971

p2 = Person()
p2.name = "Sergei"
p2.surname = "Korolev"
p2.place_of_birth = "Russia"
p2.year_birth = 1907

p1.print_info(3)
p2.print_info(5)
p1.get_age(2023)
p2.get_age(2023)