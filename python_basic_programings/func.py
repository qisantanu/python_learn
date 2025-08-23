def greet():
    print("Hello, how are you?")

greet()

def greet_person(name):
    print("Hello, " + name + "!")

greet_person("Alice")
greet_person("Bob")

def describe_pet(animal, name):
    print("I have a " + animal + ".")
    print("Its name is " + name + ".")

describe_pet("dog", "Buddy")
describe_pet("cat", "Whiskers")


def add_numbers(x, y):
    result = x + y
    return result

sum_of_nums = add_numbers(5, 7)
print(sum_of_nums)

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_func_scope():
    x = "local"
    print("Inside function:", x)

my_func_scope()


def my_func():
  x = 300
  print(x)

my_func()

y = 10  # Global variable
def my_func_scope_global():
    global y
    print("Inside function:", y)

my_func_scope_global()