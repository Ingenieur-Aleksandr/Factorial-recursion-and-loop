"""
Короткий скрипт, позволяющий вычислять факториалы натуральных (!) чисел.
Автор: Шарифуллин Александр (In_genie_ur)
"""
k = input("Введите любое натуральное число: ")
def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
if isInt(k) == True:
 def factorial(n):
  if n == 1:
   return 1
  return factorial(n-1)*n
 print('Методом рекурсии факториал равен: ' + str(factorial(int(k))))
 def factorial_cycle(n):
  result = 1
  for i in range(2,n+1,1):
   result *= i
  return result
 print('Циклический расчёт факториала даёт результат: ' + str(factorial_cycle(int(k))))
else:
 print('Введено не натуральное число!')