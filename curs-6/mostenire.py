import random

class Animal(object):
    def __init__(self, age):
        self.years = age
        self.name = None

    def get_age(self):
        return self.years

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.years = new_age

    def set_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.years)


class Cat(Animal):
    def speak(self):
        print("miau")

    def __str__(self):
        return "cat:" + str(self.name) + ":" +str(self.years)


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friends(self, friend_name):
        if friend_name not in self.friends:
            self.friends.append(friend_name)

    def speak(self):
        print("hello!")

    def age_diff(self, other):
        diff = self.years - other.years
        print(abs(diff), "year difference")

    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.years)


class Student(Person):
    def __init__(self, name, age, major = None):
        Person.__init__(self, name, age)
        self.set_name(name)
        self.friends = []
        self.major = major

    def get_major(self):
        return self.major

    def speak(self):
        speak_list = ['studiez', 'dorm', 'mananc', 'ma uit la netflix']
        print(random.choice(speak_list))

    def change_major(self, new_major):
        self.major = new_major

    def __str__(self):
        return "Student:" + str(self.name) + " " + str(self.years) + " " + str(self.major)


class Rabbit(Animal):
    # class variable
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    # def __eq__(self, other):
    #     parents_same = (self.parent1.rid == other)
    #

    def __str__(self):
        return "rabbit: " + self.get_rid()
# dog = Animal(4)
# print(dog.years)
# dog.years = 5
# dog.new_attribute = "ceva"
# print(dog.new_attribute)
# dog.set_name("Lucky")
# print(dog.get_name())
# print(dog)


# dog = Animal(4)
# cat = Cat(5)
# cat.set_name("Tom")
# cat.set_age(8)
#
#
# print(dog)
# print(cat)
#
# p1 = Person("Ion", 30)
# p2 = Person("Maria", 25)
#
# print(p1.get_name())
# print(p2.get_name())
#
# print(p1)
# print(p2)
#
# p1.speak()
# p2.speak()
#
# p1.age_diff(p2)

# s1 = Student("Ana", 20)
# s2 = Student("Cristi", 21)
#
# print(s1)
# s1.change_major("AC")
# print(s1)
# print(s2)

r1 = Rabbit(1)
r2 = Rabbit(2)
r3 = Rabbit(3)

print("r1", r1)
print("r2", r2)
print("r3", r3)

print(r1.get_age())
print(r2.get_age())
print(r3.get_age())
#
# print(r1.get_parent1())
# print(r2.get_parent2())
#
# r4 = Rabbit(8, r1, r2)
# print(r4)
#
# r5 = r4 + r3
#
# print(r5)
# print(r5.get_parent1())
# print(r5.get_parent2())

