'''1. Найти сумму и произведение цифр трехзначного числа,
    которое вводит пользователь.'''

number = input('Введите число: ')

sum_of_numbers = 0
the_product_of_numbers = 1

for f in number:
    sum_of_numbers += int(f)
    the_product_of_numbers *= int(f)
print(f"Сумма цифр числа: {number}: {sum_of_numbers}")
print(f"Произведение цифр числа: {number}: {the_product_of_numbers}")