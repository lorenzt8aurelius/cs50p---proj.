def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter the barks you want: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("arfff")


main()