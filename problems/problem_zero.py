import json
from math import sqrt
from time import perf_counter
from collections import defaultdict

max_count = 718000

square_nums = []


# this recursive algorithm is not viable while computing massive numbers like 100k
def get_prime_factors_recur(num: int, divisor: int = 2) -> int:
    if num <= 1:
        return []

    if num % divisor == 0:
        return [divisor] + get_prime_factors_recur(num // divisor, divisor)
    else:
        return get_prime_factors_recur(num, divisor + 1)


def get_prime_factors(num: int, divisor: int = 2) -> int:
    if num <= 1:
        return []

    prime_factors = []
    current_factor = num
    while True:
        if current_factor == 1:
            break
        if current_factor % divisor != 0:
            divisor += 1
            continue
        current_factor = current_factor // divisor
        prime_factors.append(divisor)
    return prime_factors


# this recursive algorithm is not viable while computing massive numbers like 100k
def is_square_num_recur(num: int) -> bool:
    prime_factors = get_prime_factors(num)
    prime_factors_freq = defaultdict(int)

    for factor in prime_factors:
        prime_factors_freq[factor] += 1

    for value in prime_factors_freq.values():
        if value % 2 != 0:
            return False
    return True


def is_square_num(num: int) -> bool:
    prime_factors = get_prime_factors(num)
    factor_freq = defaultdict(int)

    for factor in prime_factors:
        factor_freq[factor] += 1

    for freq in factor_freq.values():
        if freq % 2 != 0:
            return False
        continue
    return True


def generate_k_square_nums(k: int) -> list[int]:
    n = 1
    square_nums = []

    while True:
        start = perf_counter()
        if len(square_nums) >= k:
            break
        if is_square_num(n):
            square_nums.append(n)
        n += 1
        end = perf_counter()

        with open("./docs/problem_zero/problem_zero_computation.json", "a") as f:
            f.write(f"{json.dumps(
                    {
                        "iteration": n,
                        "square_nums": len(square_nums),
                        "duration": end - start,
                    }
                )},\n")
        print(f"iteration: {n}\ncount: {len(square_nums)}\nduration: {end - start}\n")
    return square_nums


def main():

    start = perf_counter()

    try:
        with open("./docs/problem_zero/problem_zero_computation.json", "a") as f:
            f.write(f"{json.dumps({"start": start})},\n")
        square_nums = generate_k_square_nums(1000)
    except KeyboardInterrupt:
        end = perf_counter()
        duration = end - start
        with open("./docs/problem_zero/problem_zero_computation.json", "a") as f:
            f.write(f"{json.dumps({"end": end})},\n")
            f.write(f"{json.dumps({"duration": duration})}")
    print(f"Duration: {duration}")
    print(square_nums)


if __name__ == "__main__":
    main()
