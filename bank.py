def main():
    greeting = input("Greeting: ")

    greeting = greeting.strip().lower()

    if greeting.startwith("hello"):
        print("0$") 
    elif greeting.startwith("h"):
        print("20$") 
    else:
        print("0$") 

main()