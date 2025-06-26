def main():
    file = input("File name: ")

    file = file.strip().lower()

    if file.endswith (".gif"):
        print("")
    elif file.endswith (".jpg") or file.endswith(".jpeg"):
        print("")
    elif file.endswith (".png"):
        print("")
    else:
        print("application/octet-stream")

        
main()