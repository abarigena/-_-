# Тема 3. Операторы, условия, циклы
Отчет по Теме #3 выполнил:
- Галанов Данил Николаевич
- ПИЭ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ |---------|---------|
| Задание 1 | +       | +       |
| Задание 2 | +       | +       |
| Задание 3 | +       | +       |
| Задание 4 | +       | +       |
| Задание 5 | +       | +       |
| Задание 6 | +       | -       |
| Задание 7 | +       | -       |
| Задание 8 | +       | -       |
| Задание 9 | +       | -       |
| Задание 10 | +       | -       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №3

### Задание 1


```python
one = int(input("first: "))
two = int(input("second: "))

if one == two:
    print("выполняется")
else:
    print("не выполняется")
```
### Результат.

![Меню]()

### Выводы

Ввели две переменные и сравнили их

### Задание 2


```python
a = int(input("знач: "))
if a < 0:
    print("меньше 0")
elif 0 < a < 10:
    print("большн 0 и меньшн 10")
else:
    print("больше 10")
```
### Результат.

![Меню]()

### Выводы

при помощи if elif else узнали в каком диапазоне находится введеное число

### Задание 3


```python
numbers = [1, 3, 2, 5, 6, 7]
n = int(input("число: "))

if n in numbers:
    print("есть")
else:
    print("нет")
```
### Результат.

![Меню]()

### Выводы

`условие if узнает естьли число в массиве
  
### Задание 4


```python
numbers = [1,23,24,25,34,54,67,876,4357,32314]
n = int(input("число: "))
if n in numbers:
    if n % 2 == 0:
        print("есть в массиве и четная")
    else:
        print("есть в массиве и нечетная")
else:
    print(f"переменной {n} нет")
```
### Результат.

![Меню]()

### Выводы

при помощи if этой узнаем содержится ли число в массиве и проверяем на четность

### Задание 5


```python
for i in range(10):
    print("i = ", i)
    if i == 0:
        i += 2
    if i == 1:
        continue
    if i == 2 or i == 3:
        print("переменная равна 2 или 3")
    elif i in [4, 5, 6]:
        print("переменная равна 4, 5 или 6")
    else:
        break
```
### Результат.

![Меню]()

### Выводы

цикл из 10 итераций с условиями

### Задание 6


```python
string = "привет, всем изучающим питон!"
value = input()
for i in string:
    if i == value:
        index = string.find(value)
        print(f"буква  {value}  есть в строке под  {index} индексом")
        break
else:
    print(f"буквы {value} нет  в указ строке")
```
### Результат.

![Меню]()

### Выводы

функция find находит букву по индексу

### Задание 7


```python
value = 100
for i in range(10, -1, -1):
    value -= i
    print(i, value)
```
### Результат.

![Меню]()

### Выводы

`for i in range(100, -1, -1):` обратный цикл for

### Задание 8


```python
value = 0
while value < 100:
    if value == 0:
        value += 10
    elif value // 5 > 1:
        value *= 5
    else:
        value -= 5
    print(value)
```
### Результат.

![Меню]()

### Выводы

цикл while с условиями 

### Задание 9



```python
value = 0
for i in range(10):
    for j in range(10):
        if i != j:
            value += j
        else:
            pass

print(value)
```
### Результат.

![Меню]()

### Выводы

используем вложенный цикл, `pass` оператор, который служит для проверки роботоспособности кода

### Задание 10


```python
array = [2, 4, 6, 8, 9]
flag = False
for value in array:
    if value % 2 == 1:
        flag = True

if flag is True:
    print("в массиве есть нечетное ")
else:
    print("в массиве есть четное")
```
### Результат.

![Меню]()

### Выводы

используем флаг для проверки

## Самостоятельная работа №3
### 1

```python
n = 1
for i in range(2):
    n *= 5
    n += 1

print(n)
```
### Результат.

![Меню]()

### Выводы

`for i in range(2):` цикл выполняется 2 раза
  
### Задание 2

```python
string = "Hello world"
for i in range(len(string) - 1, -1, -1):
    print(string[i])
```
### Результат.

![Меню]()

### Выводы

`for i in range(len(string) - 1, -1, -1):` обратный цикл по строке
  
### Задание 3

```python
num = int(input())
if 0 <= num <= 3:
    print(" число больше >= 0 и меньше 3")
elif 3 < num < 6:
    print("больше 3 и n меньше 6")
elif 6 <= num <= 10:
    print(" больше 6 и n меньше 10")
else:
    print("число должно быть в диапазоне от 0 до 10")
```
### Результат.

![Меню]()

### Выводы

конструкция if elif else
  
### Задание 4

```python
sentence = input()
print(len(sentence))
lower_sentence = sentence.lower()
print(lower_sentence)
count = 0
glas = "aeiou"
for glas in lower_sentence:
    if glas in glas:
        count += 1
print(count)
print(sentence.replace("ugly", "beauty"))
print(sentence.startswith("The"))
print(sentence.endswith("end"))

```
### Результат.

![Меню]()

### Выводы

1. `len(sentence)` выводим длину строки
2. `sentence.lower()` приводим строку к нижнему регистру
3. `sentence.replace("ugly", "beauty")` заменяем слово
4. `sentence.startswith("The")` проверяем начало
5. `sentence.endswith("end")` проверяем конец
  
### Задание 5

```python
string = 'hello'
memory = ' world'
counter = 0
while counter != 10:
    print(string + memory)
    print(string)
    counter += 1
string = string + ' world'
memory = string
print(memory)
```
### Результат.

![Меню]()

### Выводы



## Общие выводы по теме
поработал с базовами операциями повторил условия if while и for
