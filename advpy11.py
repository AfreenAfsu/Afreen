# 1
def non_negative_integer_only(func):
    def wrapper(x):
        if not isinstance(x, int) or x < 0:
            return f"Invalid input: {x} is not a non-negative integer"
        return func(x)
    return wrapper

@non_negative_integer_only
def calculate_square_root(x):
    return x ** 0.5

print(calculate_square_root(9))    
print(calculate_square_root(-9))   
print(calculate_square_root(4.5))

# 2
def debug(func):
    def wrapper(*args):
        print("Function:", func.__name__)
        print("Arguments:", args)
        result = func(*args)
        print("Returned:", result)
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

@debug
def greet(name):
    return f"Hello, {name}!"

# Test
add(2, 4)
greet("Afsana")

# 3
def repeat(times):
    def decorator(func):
        def wrapper():
            for i in range(times):
                print(f"Run {i + 1}:")
                func()
        return wrapper
    return decorator

@repeat(3)  # Repeat 3 times
def say_hello():
    print("Hello!")

say_hello()

# 4
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call number: {wrapper.calls}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

def greet(name):
    print(f"Hello, {name}!")

greet("Afsana")
greet("Afsana")
greet("Afsana")

