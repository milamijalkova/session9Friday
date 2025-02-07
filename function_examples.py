def greet():
    """
    Simple function printing hello
    :return: 0
    """
    print("Hello!")
    return 0

def greet_improved(name):
    """
    mMore complex greet that takes a name as a parameter
    :param name: the name of the person to greet
    :return: None
    """
    print("Hello", name)

greet_improved ("Andrej")
greet_improved ("Mila")

def custom_op(x=0, y=0):
    """
    Custom op: 10x +y
    :param x: the first number
    :param y: the second number
    :return: number, 10x + y
    """
    result= 10*x + y
    return result

print(custom_op(5,8))
x=custom_op(5,9) #arguments by position!
print(f"the result of custom_op is: {x}")
x=custom_op(y=9, x=5) #arguments by name!
print(f"the result of custom_op is {x}")
print(custom_op(5)) #using custom values for y
print(custom_op()) #defult values for both
print(custom_op(y=9)) #defult value for x

def bond_intro(name):
    print("the name is:", name)

def bond_name(first, last):
    return f"{last}, {first}, {last}"

print(bond_name("Mila", "Mijalkova"))
bond_intro(bond_name("Mila", "Mijalkova"))
bond_intro(bond_name())



