# My first PRNG
from sys import set_int_max_str_digits
number = int(input('Type some random numbers: '))
set_int_max_str_digits(0)
rng = number
for i in range(10):
    rng = ((rng ** 4 + 782) // 56 - 139 % 8765 * 2) // 23 % 99999999999999
print(rng)