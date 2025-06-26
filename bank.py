def main():
    greeting = input("Greeting: ")

    greeting = greeting.strip().lower()

    if greeting.starstwith("hello"):
        print("0$") 
    elif greeting.starstwith("h"):
        print("20$") 
    else:
        print("0$") 

main()