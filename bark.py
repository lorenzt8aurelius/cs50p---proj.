def main():
    number = get_number()
    meow()

def get_number():
    while True:
        n = int(input("Enter the barks you want: "))
            if n > 0:
                return n

def meow(n):
    for _ in range(n):
        print("arfff")


main()