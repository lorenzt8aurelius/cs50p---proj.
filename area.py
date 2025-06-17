def area(lenght, width):
    return lenght * width
    print(str(lenght * width) + "square feet")

def main():
    house = area(50, 20)
    yard = area(50, 50)
    total = house + yard
    print(str(total) + "total square feet")

(main)