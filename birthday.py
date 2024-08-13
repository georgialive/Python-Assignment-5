# Name: Georgia Vrana
# Date Submitted: Friday, March 1st, 2024
# Assignment-4: Birthday
# Description: The program `birthday.py` calculates age using birth and present year.


def getAge(presentYear, birthYear):
    return presentYear - birthYear

birthYear = int(input("What is your birth year? : "))
presentYear = int(input("What is the present year? : "))
age = getAge(presentYear, birthYear)

print(f"Your age is {age} years old")