import os
from dotenv import load_dotenv

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Викликається функція: {func.__name__} з аргументами {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат виконання: {result}")
        return result
    return wrapper




