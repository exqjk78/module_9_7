def is_prime(func):
    def wrapper(*args, **kwargs):
        number = func(*args, **kwargs)
        if number <= 1:
            print(f'Число {number} не является ни простым, ни составным.')
            return number
        for i in range(1, number):
            if number % i == 0 and number != i:
                print('Простое')
                return number
            else:
                print('Составное')
                return number
    return wrapper

@is_prime
def sum_three(*number):
    sum_number = sum(number)
    return sum_number

res = sum_three(2, 3, 6)
print(res)