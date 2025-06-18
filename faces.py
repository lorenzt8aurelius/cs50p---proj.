def convert(text):
    text = text.replace = (":(", "😔")
    text = text.replace = (":)", "😊")
    return text


def main():
    user_input = input("Say something: ")
    print(convert, user_input)

main()

