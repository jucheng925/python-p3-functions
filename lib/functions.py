#!/usr/bin/env python3

def greet_programmer():
    print('Hello, programmer!')

def greet(name):
    print(f'Hello, {name}!')

def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')

def add(num1, num2):
    return num1 + num2

# def halve(number):
#     if number != int(number)) or (int(number) != float):
#         print("fail")
#     else:
#         print(number / 2)
# print(halve(10))

def halve(number):
    return number / 2

print(halve(10))