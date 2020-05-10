"""
from math import *
name1 = "Danniel Rand"
age = 31
name2 = "Danny"
city1 = "K'un-Lun"
city2 = "Newyork"
business = "Rand Enterprises"
partner = "Ward's"
gf_name = "Colleen"
gf_age = 28
ismale = True
#intro = "When Danny Rand was 10-years old, he survived a mysterious plane crash that claimed the lives of his extremely wealthy parents. Rescued by warrior monks, Danny grew up in the of city of K'un-Lun, where he endured harsh conditions, but also trained to be a fierce warrior. Years later, Danny returns home to New York, where he wants to reconnect with his past and take his rightful place at his family's company, which is being run by his father's former business partner. Danny hopes to restore his family legacy by defeating the people who threaten it."
# print(f" when {name1} was 10-years old, he survived a mysterious plane crash that claimed the lives of his extremely wealthy parents. He was called with nickname {name2}.\n Rescued by warrior monks, {name2} grew up in the of city of {city1}, where he endured harsh conditions, but also trained to be a fierce warrior.\n Years later, when {name2} turned {age} returned home to {city2}, where he wants to reconnect with his past and take his rightful place at his family's company {business}, which is being run by his father's former business partner, {partner} .\n Danny hopes to restore his family legacy by defeating the people who threaten it. {name2} has girlfriend name {gf_name} and her age is {gf_age}")
print(sqrt(36)) 
"""
"""
loan_number = input("Loan number: ")
print(f"{loan_number} , Welcome to Bayview")

num1 = input("Enter the number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)
"""
""" #Lists
list = ["Milk", "Butter", "Eggs"]
#print(list[1])
#print(list[-1])
#print(list[1:])
#print(list[1:3])
list[2] = "Bread"
print(list)
x = [1,22,33,44]
print(x[0:3])
x= [0,1,2,3,4,5,6]
print(x[0:4:2])
"""
""" #How to call multi variables
name = "Skumar"
place = "Florida"
age = 22
print(f"{name} is my name, I live in {place} and I'm {age} years old")
"""
""" #function-Extend
list_a = [22,33,44,551,2,3]
list_b = ["hasd", "ajshd", "ajaj", "josdjap"]
list_a.append("asdf") #you can add a value in the begging
list_a.insert(3, 55) #insert a value
list_b.remove("hasd") #remove a value
list_a.extend(list_b) #Adding 2 lists in simgle print
#print(list_a.index(551)) #To find out the index number of an value
list_c = list_a.copy() #copy a variables
print(list_c)
"""
#Tuples
lista = ("asdf", "addededed", "oeoeoe")
print(lista[2])

""" #Functions
def new_func(name, age):
    print("Hellooooo "+ name +" your "+ str(age) +" years old ")

new_func("Sai", 23)
"""
"""#Return statement
def square_root(num):
    return num*num
result = square_root(2)
print(result)
"""
"""#If else Statements - Boolean
is_veg = False
is_vegan = False

if is_veg and is_vegan:
    print("you're Vegan")
elif is_veg and not(is_vegan):
    print("you are a vegetarian")
else:
    print("You're a meat eater")
"""
""" #If else Statements - Operator
def numbers(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

results = numbers(12,12,14)
print(results)
"""
"""#If else - Mini calculator
fn1 = input("Enter a number: ")
operator = input("Enter operator: ")
fn2 = input("Enter a number: ")

if operator == "+":
    print(float(fn1 + fn2))
elif operator == "-":
    print(float(fn1 - fn2))
elif operator == "*":
    print(float(fn1 * fn2))
else:
    print("Invalid Operator")
"""    
""" #Dictionary - Key:Values
week_conversion = {
    "Mon" : "Monday",
    "Tue" : "Tuesday",
    "Wed" : "Wednesday",
    "Thu" : "Thursday",
    "Fri" : "Friday",
    "Sat" : "Saturday",
    "Sun" : "Sunday"
    }
#print(week_conversion["Mon"])
#print(week_conversion.get("Tue"))
print(week_conversion.get("SAT", "Not a valid key"))
 """
""" #While loop
i = 1
while i <= 5:
    print(i)
    i += 1

print("Condition reached")
"""
"""#While loop - Mini game
phone = "iphone"
guess = ""

while guess != phone:
    guess = input("Guess the best phone: ")

print("Yaayy !! You Win")
"""  

phone = "iphone"
guess = ""
guess_count = 0

while guess != phone:
    guess = input("Guess the best phone: ")
    guess_count += 1

print("Yaayy !! You Win")
