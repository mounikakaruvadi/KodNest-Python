# add 2 numbers
def add():
    a = 10
    b = 20
    print(a + b)
add()

# Square of number
def square():
    a = 5
    print(a * a)
square()

# Find the largest number in given 3 numbers
def largest():
    a = 10
    b = 20
    c = 30
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
largest()


# Even or Odd
def even_or_odd():
    a = 10
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")
even_or_odd()

#Greet with name
def greet():
    name = "mouni"
    print("Hello", name)
greet()

# No arguments + No return value
def square():
    a = 5
    print(a * a)
square()

# No arguments + Return value
def square():
    a = 5
    return a * a
print(square())

# Arguments + No return value
def square(a):
    print(a * a)
square(5)

# Arguments + Return value
def square(a):
    return a * a
res = square(5)
print(res)
