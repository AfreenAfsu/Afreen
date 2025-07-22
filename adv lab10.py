# 1
def prime_number_generator():
    num = 2
    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

gen = prime_number_generator()
for _ in range(15):
    print(next(gen))

# 2
import random

def temperature_simulator():
    for _ in range(10):
        yield random.randint(-10, 35)

for temp in temperature_simulator():
    print("Temperature:", temp, "°C")

# 3
def fibonacci_generator():
    x, y = 0, 1
    count = 0
    while True:
        yield x
        x, y = y, x + y

def sum_first_fibonacci(count):
    return sum(next(fib) for _, fib in zip(range(count), [fibonacci_generator().__next__() for _ in range(count)]))

def sum_fibonacci(n):
    gen = fibonacci_generator()
    return sum(next(gen) for _ in range(n))

print("Sum of first 10 Fibonacci numbers:", sum_fibonacci(10))

# 4
def filter_strings(data):
    return (value for value in data if type(value) is str)

mixed_data = [1, "hello", 3.14, "world", 42]

for item in filter_strings(mixed_data):
    print(item)
