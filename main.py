from Calculate import Calculate
import roman
import re


while(True):
    is_arabic = True
    expression = input('Введите выражение: ')
    if '+' in expression:
        expression = expression.replace(' ', '')
        expression = expression.split('+')
        first_number = expression[0]
        second_number = expression[1]
        operation = '+'
    elif '-' in expression:
        expression = expression.replace(' ', '')
        expression = expression.split('-')
        first_number = expression[0]
        second_number = expression[1]
        operation = '-'
    elif '*' in expression:
        expression = expression.replace(' ', '')
        expression = expression.split('*')
        first_number = expression[0]
        second_number = expression[1]
        operation = '*'
    elif '/' in expression:
        expression = expression.replace(' ', '')
        expression = expression.split('/')
        first_number = expression[0]
        second_number = expression[1]
        operation = '/'
    if (first_number.isdigit() and not second_number.isdigit()) or \
            (not first_number.isdigit() and second_number.isdigit()):
        print('Нельзя производить операцию с арабским и римским числом')
        continue
    elif not first_number.isdigit() and not second_number.isdigit():
        first_number = roman.fromRoman(first_number.upper())
        second_number = roman.fromRoman(second_number.upper())
        is_arabic = False
    elif first_number.isdigit() and second_number.isdigit():
        first_number = int(first_number)
        second_number = int(second_number)
    test = Calculate(first_number, second_number)
    if operation == '+':
        if is_arabic:
            print(test.addition())
        elif not is_arabic:
            print(roman.toRoman(test.addition()))
    elif operation == '-':
        if is_arabic:
            print(test.substraction())
        elif not is_arabic:
            print(roman.toRoman(test.substraction()))
    elif operation == '*':
        if is_arabic:
            print(test.multiplication())
        elif not is_arabic:
            print(roman.toRoman(test.multiplication()))
    elif operation == '/':
        if is_arabic:
            if second_number == 0:
                try:
                    test.division()
                except ZeroDivisionError as e:
                    print('На ноль делить нельзя, попробуйте еще раз')
            else:
                print(test.division())
        elif not is_arabic:
            if second_number == 0:
                try:
                    test.division()
                except ZeroDivisionError as e:
                    print('На ноль делить нельзя, попробуйте еще раз')
            else:
                print(roman.toRoman(int(test.division())))
