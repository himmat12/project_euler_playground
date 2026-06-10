from math import sqrt
from collections import defaultdict

max_count = 718000

square_nums = []

def get_prime_factors(num: int, divisor: int = 2) -> int:
    if num <= 1:
        return []
    
    if num % divisor == 0:
        return [divisor] + get_prime_factors(num // divisor, divisor)
    else:
        return get_prime_factors(num, divisor + 1)

def is_square_num(num: int):
    prime_factors = get_prime_factors(num)
    prime_factors_freq = defaultdict(int)
    
    for factor in prime_factors:
        prime_factors_freq[factor] += 1
    
    for value in prime_factors_freq.values():
        if value % 2 != 0:
            return False
    return True

# for n in range(1, max_count):
#     if (n % 2) != 0:

def main():
    print(is_square_num(1))

if __name__ == "__main__":
    main()
    valid_square_numbers = []
    
    with open("square_numbers.txt", 'r') as f:
        valid_square_numbers = [int(num) for num in f.read().split(',')]
    
    print(valid_square_numbers)
    # squares_list = []
    
    # with open("square_numbers.txt", "a") as f:
    #     for i in range(1, 1001):
    #         squares_list.append(i * i)
            
    #         if i <= (1000 - 1):
    #             f.write(f"{i * i}, ")
    #         else:
    #             f.write(f"{i * i}")
    # print(len(squares_list))
    # print(squares_list)