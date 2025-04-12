#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


greet_programmer()

def greet(name):
    print(f"Hello, {name}!")


greet("programmer")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


greet_with_default("John")

def add(num1, num2):
    return num1+num2


sum=add(1,3)
print(sum)

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2
