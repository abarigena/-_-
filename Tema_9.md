# Тема 9. ООП на Python: концепции, принципы и примеры реализации
Отчет по Теме #9 выполнил:
- Галанов Данил Николаевич
- ПИЭ-22-1

| Задание    | Лаб_раб | Сам_раб |
|------------|---------|---------|
| Задание 1  | +       | +       |
| Задание 2  | +       | +       |
| Задание 3  | +       | +       |
| Задание 4  | +       | +       |
| Задание 5  | +       | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
```python
class Ivan:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Иван':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Иван"

person1 = Ivan('Алексей')
person2 = Ivan('Иван')
print(person1.name)
print(person2.name)
```
### Результат.

![Меню](images/task1.png)

### Выводы

`__slots__ = ['name']` параметры класса

## №2
```python
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print("Обычное мороженое")

icecream = Icecream()
icecream.composition()
icecream = Icecream('шоколадом')
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```
### Результат.

![Меню](images/task2.png)

### Выводы

 проверяем, что переменная относится к стринг

## №3

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        if hasattr(self, '_value'):
            return self._value
        else:
            return "value удалено"

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
```
### Результат.

![Меню](images/task3.png)

### Выводы

Создали для класса геттер и сеттер, а также функцию удаления значения
Ошибка выводилась тк мы пытались выводить удаленное значение
  
## №4

```python
class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"Dog is {cat.className}, but they say {cat.sounds}")
```
### Результат.

![Меню](images/task4.png)

### Выводы

создаем класс млекопитающие и два его наследника кошку и собаку

## №5



```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")

class English:
    @staticmethod
    def greeting():
        print("Hello")

def greet(language):
    language.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)
```
### Результат.

![Меню](images/task5.png)

### Выводы
Использовали статичные методы

## Задания для самостоятельного выполнения: Задание Садовник и помидоры.


```python
class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(num_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: ухаживайте за растениями, чтобы они созревали. "
              "Собирайте урожай только, когда все плоды созрели.")

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"{self.name} ухаживает за растением.")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Все томаты созрели. Садовник собирает урожай.")
            self._plant.give_away_all()
        else:
            print("Томаты еще не созрели! Пожалуйста, продолжайте ухаживать за растением.")


Gardener.knowledge_base()

bush = TomatoBush(5)
gardener = Gardener("Иван", bush)

gardener.work()
gardener.work()

gardener.harvest()

gardener.work() 
gardener.harvest()
```
### Результат.

![Меню](images/test1.png)
![Меню](images/test2.png)
![Меню](images/test3.png)
![Меню](images/test4.png)
![Меню](images/test5.png)

### Выводы

Этот код моделирует процесс выращивания томатов:
Класс Tomato: представляет томат с разными стадиями созревания. Он может расти (метод grow) и проверять, созрел ли он (метод is_ripe).
Класс TomatoBush: управляет несколькими томатами, предоставляя методы для роста всех томатов (grow_all) и проверки их спелости (all_are_ripe).
Класс Gardener: садовник, который ухаживает за растениями (метод work) и собирает урожай, если все томаты созрели (метод harvest).
Также есть справочная функция (knowledge_base), которая выводит информацию по уходу за растениями.

## Общие выводы по теме
Закрепили на практике ООП, отлично его освоив в питоне.
