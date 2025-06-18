def convert(text):
    text.replace = (":(", "😔")
    text.replace = (":)", "😊")
    return text


def main():
    user_input = input("Say something: ")
    print(convert, user_input)

main()

