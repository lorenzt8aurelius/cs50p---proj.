def main():
    greeting = input("Greeting: ")

    greeting = greeting.strip().lower()

    if greeting.startswith("hello"):
        print("0$") 
    elif greeting.startswith("h"):
        print("20$") 
    else:
        print("100$") 

main()