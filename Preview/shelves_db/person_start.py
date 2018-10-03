class Person:
    def __init__(self, name, age, pay=0, job=None):
        self._name = name
        self._age = age
        self._pay = pay
        self._job = job

    def __str__(self):
        return ('<%s => %s: age = %s, pay = %s>' % 
                (self.__class__.__name__, self._name, self._age, self._pay))

    @property
    def lastName(self):
        return self._name.split()[-1]

    @lastName.setter
    def lastName(self):
        raise AttributeError('Last name cannot be changed directly')

    @property
    def fullName(self):
        return self._name

    @fullName.setter
    def fullName(self, value):
        self._fullname = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self, value):
        self._pay += pay

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    tom = Manager('Tom Jones', 50)

    print("*"*80)
    print(bob.lastName)
    print(bob)
    print("*"*80)
    print(tom)
