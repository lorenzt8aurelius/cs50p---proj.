score = int(input("Score: "))

if 90 >= score <= 100:
    print("Grade: 'A'")
elif 80 >= score < 90:
    print("Grade: 'B'")
elif  75 >= score < 79:
    print("Grade: 'C'")
else:
    print("Grade: D")