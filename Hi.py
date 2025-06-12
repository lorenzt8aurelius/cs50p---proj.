#def - defines a function called hello
#to is a parameter that acts as a placeholder. In other words to wild hold whatever name the user types later.
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to):
    print("Hi there,", to)

