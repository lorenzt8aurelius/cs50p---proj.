score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: 'A'")
elif score >= 80 and score < 90:
    print("Grade: 'B'")
elif score >= 75 and score < 79:
    print("Grade: 'C'")
else:
    print("Grade: D")