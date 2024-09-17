# Тема 2. Базовые операции языка Python
Отчет по Теме #2 выполнил(а):
- Галанов Данил Николаевич
- ПИЭ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | + |
| Задание 7 | + | + |
| Задание 8 | + | + |
| Задание 9 | + | + |
| Задание 10 | + | + |



знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №2
#1.
  ```python
  print(123)
  print('123')
  print(1.23)
```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/lab2/ex1.png)

#2.
  ```python
  print(1823-486)
  print(5.1 + 8.37)
  print(3+7.04+2.33)
```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/lab2/ex2.png)
#3.
  ```python   
  print('Привет, Мир!')
  
  world = 'Мир!'
  print(f"Привет, {world}")
  
  one = 'Привет, '
  two = 'Мир!'
  print(one+two)
```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/lab2/ex3.png)
#4.
  ```python
  one = 'hello'
  print(bool(one))
  
  two = 142
  print(float(two))
  
  three = None
  print(str(three))
```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/lab2/ex4.png)
#5.
  one = input('one:')
  two = input('two:')
  three = input('three:')
  
  print(one, two, three)
  ```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/lab2/ex5.png)
#6.
  ```python
  a =12
  b = 5
  print('Возведение в степеню:', a**b)
  print('Обычное деление:', a/b)
  print('Целочисленное деление:', a//b)
  print('Нахождение остатка деления:', a%b)
```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/lab2/ex6.png)
#7.
  ```python
  line = 'Hello!'
  print(line*6)
```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/lab2/ex7.png)
#8.
  ```python
  sentence = 'hello World!'
  print(sentence.count('o'))
```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/lab2/ex8.png)
#9.
  ```python
  print('Hello \nWorld')
```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/lab2/ex9.png)
#10.
  ```python
  sentence = 'Hello World'
  print(sentence[1])
  print(sentence[:5])
```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/lab2/ex10.png)
## Самостоятельная работа №2

1.
  ```python
  str = ''
  print(bool(str))
  ```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/sam2/ex1.png)
2.
  ```python
  a , b, c = 1, 2, 3
  print(a,b,c)
  ```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/sam2/ex2.png)
3.
  ```python
  num = int(input())
  print(num)
  ```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/sam2/ex3.png)
4.
  ```python
  s = input()[:5]
  print(s*16)
  ```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/sam2/ex4.png)
5.
  ```python
  day, month , year = int(input()),str(input()) ,int(input())
  print(f"Сегодня {day} {month} {year}", end = ' Всего хорошего!')
  ```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/sam2/ex5.png)
6.
  ```python
  sentence = "Hello World"; print(sentence.replace(" ", " my "))
  ```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/sam2/ex6.png)
7.
  ```python
  sentence = "Hello World"
  print("Длина строки:", len(sentence))
  ```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/sam2/ex7.png)
8.
  ```python
  sentence = "HELLO WORLD"
  print(sentence.lower())
  ```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/sam2/ex8.png)
9.
  Введите два чтсла и выведите сумму разность произведение и частное код в две строки
  ```python
  a = int(input("первое число: "))
  b = int(input("второе число: "))
  ```
  print(f"Сумма: {a + b}, Разность: {a - b}, Произведение: {a * b}, Частное: {a / b if b != 0 else 'деление на ноль'}")
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/sam2/ex9.png)
10.
  Пользовотель вводит строку ее нужно развернуть код в две строки
  ```python
  string = input("Введите строку: ")
  print(string[::-1])
```
  ![Меню](https://github.com/abarigena/Software_Engineering/blob/Tema_2/sam2/ex10.png)
