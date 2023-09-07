def math_func(a, b):
    if math_operation == "+":
        return a + b
    elif math_operation == "-":
        return a - b
    elif math_operation == "*":
        return a * b
    elif math_operation == "/":
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Ошибка: недопустимая операция"


num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
math_operation = input('Введите математическую операцию (+, -, *, /): ')


print(f'Результат: {math_func(num1, num2)}')




