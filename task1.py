def math_func(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Ошибка: недопустимая операция"


while True:
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    math_operation = input('Введите математическую операцию (+, -, *, /): ')

    print(f'Результат: {math_func(num1, num2, math_operation)}')

    again = input('Желаете продолжить (да/нет)? ')
    if again.lower() != 'да':
        break





