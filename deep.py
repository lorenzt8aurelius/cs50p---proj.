def deep():
    text = input("What's the Answer to the Great Question of Life, the Universe and Everything? ") 

    text = text.strip().lower()

    if text == "42" or text == "forty two" or text == "forty-two":
        print("Yes")
    else:
        print("No")

deep()
        
        

