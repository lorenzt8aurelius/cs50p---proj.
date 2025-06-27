def main():
    number = get_number()
    meow()

def get_number():
    while True:
        n = int(input("Enter the barks you want: "))

def meow(n):
    for _ in range(n):
        print("arfff")


main()