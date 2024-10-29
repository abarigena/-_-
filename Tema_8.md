# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме #8 выполнил:
- Галанов Данил Николаевич
- ПИЭ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ |---------|---------|
| Задание 1 | +       | +       |
| Задание 2 | +       | +       |
| Задание 3 | +       | +       |
| Задание 4 | +       | +       |
| Задание 5 | +       | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")
```
### Результат.

![Меню](images/task1.png)

### Выводы

Создали класс “Car” с атрибутами производитель и модель.

## №2

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.drive()
```
### Результат.

![Меню](images/task2.png)

### Выводы

добавили метод drive

## №3

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```
### Результат.

![Меню](images/task3.png)

### Выводы

создали наследника класса car и создали ему метод charge
  
## №4


```python
class Car:
    def __init__(self, make, model):
        self._make = make
        self.__model = model

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Toyota", "Corolla")

print(my_car._make)
my_car.drive()
```
### Результат.

![Меню](images/task4.png)

### Выводы

добавили инкапсуляцию, сделав атрибуты приватными

## №5



```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

my_rectangle = Rectangle(5, 4)
my_circle = Circle(5)

print(my_rectangle.area())
print(my_circle.area())
```
### Результат.

![Меню](images/task5.png)

### Выводы

применили полиморфизм переопределив метод area в наследниках

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны
### отличаться, от тех, что указаны в теоретическом материале
### (методичке) и лабораторных заданиях. Результатом выполнения
### задания будет листинг кода и получившийся вывод консоли.

```python
class Animal:
    def __init__(self, hp):
        self.hp = hp

    def get_hp(self):
        return self.hp

my_animal = Animal(5)
print(my_animal.get_hp())
```
### Результат.

![Меню](images/s1.png)

### Выводы

создали класс животное
  
## №2
### Самостоятельно создайте атрибуты и методы для ранее созданного
### класса. Они должны отличаться, от тех, что указаны в
### теоретическом материале (методичке) и лабораторных заданиях.
### Результатом выполнения задания будет листинг кода и
### получившийся вывод консоли.

```python
class Animal:
    def __init__(self, hp, voice):
        self.hp = hp
        self.voice = voice

    def get_hp(self):
        return self.hp

    def say(self):
        return self.voice

my_animal = Animal(5, "краб")
print(my_animal.get_hp())
print(my_animal.say())
```
### Результат.

![Меню](images/s2.png)

### Выводы

классу животное создали метод голос и здоровье
  
## №3
### Самостоятельно реализуйте наследование, продолжая работать с
### ранее созданным классом. Оно должно отличаться, от того, что
### указано в теоретическом материале (методичке) и лабораторных
### заданиях. Результатом выполнения задания будет листинг кода и
### получившийся вывод консоли.


```python
class Animal:
    def __init__(self, hp):
        self.hp = hp
        self.voice = "краб"

    def get_hp(self):
        return self.hp

    def say(self):
        return self.voice

class Cat(Animal):
    def __init__(self, hp):
        super().__init__(hp)
        self.voice = "mey!"

my_animal = Animal(5)
my_cat= Cat(10)

print(my_animal.say())
print(my_cat.say())
```
### Результат.

![Меню](images/s3.png)

### Выводы

создали наследника Cat
  
## №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с
### ранее созданным классом. Она должна отличаться, от того, что
### указана в теоретическом материале (методичке) и лабораторных
### заданиях. Результатом выполнения задания будет листинг кода и
### получившийся вывод консоли.

```python
class Animal:
    def __init__(self, hp):
        self.hp = hp
        self.voice = "краб"

    def get_hp(self):
        return self.hp
    
    def set_hp(self, new_hp):
        if new_hp >= 0:  
            self.__hp = new_hp
        else:
            print("ошибка")

    def say(self):
        return self.voice

class Cat(Animal):
    def __init__(self, hp):
        super().__init__(hp)
        self.voice = "mey!"

my_animal = Animal(5)
my_cat= Cat(10)

print(my_animal.say())
print(my_cat.say())

print(my_animal.get_hp())  
my_animal.set_hp(8)       
print(my_animal.get_hp())  
my_animal.set_hp(-3)
```
### Результат.

![Меню](images/s4.png)

### Выводы

определили гетер и сеттер у класса сделали приватными поля класса
  
## №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и
### лабораторных заданиях. Результатом выполнения задания будет
### листинг кода и получившийся вывод консоли.

```python
class Animal:
    def __init__(self, hp):
        self.__hp = hp  

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_hp):
        if new_hp >= 0:
            self.__hp = new_hp
        else:
            print("Значение здоровья не может быть отрицательным")

    def say(self):
        return "я животное" 


class Dog(Animal):
    def __init__(self, hp):
        super().__init__(hp)

    def say(self):
        return "гав!"  


class Cat(Animal):
    def __init__(self, hp):
        super().__init__(hp)

    def say(self):
        return "мяу!"  

animals = [Animal(5), Dog(10), Cat(8)]

for animal in animals:
    print(animal.say())  
```

### Результат.

![Меню](images/s5.png)

### Выводы

переопределяем метод say в Dog и Cat, таким образом получаем полиморфизм

## Общие выводы по теме
порбатали с ООП посоздавали класса наследников, переопределили методы у наследников
