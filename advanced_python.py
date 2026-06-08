# Phase 0 — Advanced Python
# Topics: Decorators, Generators, *args/**kwargs, Comprehensions

import time
import functools

# ============================================================
# SECTION 1: DECORATORS
# ============================================================

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"{func.__name__} ran in {elapsed:.6f} seconds")
        return result
    return wrapper


def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for v in list(args) + list(kwargs.values()):
            if isinstance(v, (int, float)) and v < 0:
                raise ValueError(f"All arguments must be positive, got {v}")
        return func(*args, **kwargs)
    return wrapper

@timer
@validate_positive
def compute(x, y):
    return x ** y + y ** x


# ============================================================
# SECTION 2: GENERATORS
# ============================================================

def prime_generator():
    n = 2
    while True:
        is_prime = all(n % i != 0 for i in range(2, int(n**0.5) + 1))
        if is_prime:
            yield n
        n += 1

def chunker(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i+size]


# ============================================================
# SECTION 3: *args / **kwargs
# ============================================================
def stats(*numbers):
    return {
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }


def create_profile(**fields):
    for key, value in fields.items():
        print(f"{key}: {value}")

    return fields


def flexible(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


# ============================================================
# SECTION 4: COMPREHENSIONS
# ============================================================

numbers = range(1, 21)

squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
square_map = {x: x**2 for x in numbers}
remainders_mod3 = {x % 3 for x in numbers}


# ============================================================
# QUICK TESTS — run this file to verify
# ============================================================

if __name__ == "__main__":
    print(compute(3, 4))
    
    gen = prime_generator()
    print([next(gen) for _ in range(10)])
    
    print(list(chunker([1,2,3,4,5,6,7], 3)))
    
    print(stats(4, 8, 15, 16, 23, 42))
    create_profile(name="Atomeo", goal="AI engineer", days=5)
    
    print(squares_of_evens)
    print(square_map)
    print(remainders_mod3)