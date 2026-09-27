# ===========================================
# DAY 8 - FUNCTIONS IN PYTHON
# ===========================================

print("===== DAY 8 : FUNCTIONS =====\n")

# -------------------------------
# Example 1 : Simple Function
# -------------------------------

def greet():
    print("Hello Shruti!")
    print("Welcome to Python Functions.\n")

greet()

# -------------------------------
# Example 2 : Function Called Multiple Times
# -------------------------------

def welcome():
    print("Welcome to Python Class!")

welcome()
welcome()
welcome()

print()

# -------------------------------
# Example 3 : Function with Parameter
# -------------------------------

def student(name):
    print("Student Name:", name)

student("Shruti")
student("Rahul")
student("Priya")

print()

# -------------------------------
# Example 4 : Function with Two Parameters
# -------------------------------

def add(a, b):
    print("Sum =", a + b)

add(10, 20)
add(50, 40)

print()

# -------------------------------
# Example 5 : Function Returning Value
# -------------------------------

def square(num):
    return num * num

result = square(6)
print("Square =", result)

print()

# -------------------------------
# Example 6 : Even or Odd
# -------------------------------

def check(number):
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

check(15)
check(20)

print()

# -------------------------------
# Example 7 : Calculator Function
# -------------------------------

def calculator(a, b):
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)
    print("Division =", a / b)

calculator(20, 5)

print()

# ===========================================
print("Day 8 Functions Completed Successfully!")
# ===========================================
def largest(a, b):
    if a > b:
        print(a, "is Greater")
    else:
        print(b, "is Greater")

largest(50, 90)
largest(100, 20)
print("\n========== DAY 8 PART 2 ==========\n")

# ----------------------------------
# 1. Default Parameter
# ----------------------------------

def country(name="India"):
    print("Country:", name)

country()
country("Canada")
country("Japan")

print()

# ----------------------------------
# 2. Keyword Arguments
# ----------------------------------

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Shruti")

print()

# ----------------------------------
# 3. Arbitrary Arguments (*args)
# ----------------------------------

def numbers(*num):
    print("Numbers:", num)

numbers(10, 20)
numbers(1, 2, 3, 4, 5)

print()

# ----------------------------------
# 4. Keyword Arbitrary Arguments (**kwargs)
# ----------------------------------

def details(**info):
    print(info)

details(name="Shruti", age=20, city="Mohali")

print()

# ----------------------------------
# 5. Lambda Function
# ----------------------------------

square = lambda x: x * x

print("Square of 8 =", square(8))

print()

# ----------------------------------
# 6. Recursion
# ----------------------------------

def countdown(n):
    if n == 0:
        print("Finished!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)

print()

print("DAY 8 PART 2 COMPLETED SUCCESSFULLY!")
