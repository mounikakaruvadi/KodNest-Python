c = 10
def add():
    global a
    a = 10
    b = 20 # local variable
    print(a + b)
    print(c) # global variable
add()

x = 100 # global variable
def display():
    x = 50 # local variable
    print("Local x:", x)
display()
print("Global x:", x)


x=10
def display():
    print(x)
    # x = 20 # global variable
    # print(x) # local variable
display()
x = 30
print(x)


def add(a, b):
    print(a +b)

def add(a, b, c):
    print(a + b + c) 

def add(a, b, c, d):
    print(a + b + c + d)     



def add(a, b = 0, c = 0):
    print(a + b + c) 

add(10, 20, 30)
add(10, 20)
add(10)    


def add(*a):
    print(sum(a))

add(10, 20)
add(10,20,30)
add(10)

# **kwargs - 0 ... n arguments can be passed
def stu_info(**kwargs):
    print(f"name is {kwargs.get("name")}", end = " ")
    print(f"age is {kwargs.get("age")}", end = " ")
    print(f"gender is {kwargs.get("gender")}", end = " ")
    
stu_info(name = "mounika", age = 23, gender = "female")
