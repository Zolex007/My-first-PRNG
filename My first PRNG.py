# My first PRNG
from sys import set_int_max_str_digits
number = int(input('Type some random numbers: '))
set_int_max_str_digits(0)
rng1 = number ** 23
rng2 = rng1 - number
rng3 = rng2 + 9867
rng = rng3 // 8
print(f'your random number is {rng}')