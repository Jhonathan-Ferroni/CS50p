greetings = input("Greetings: ")

greetings = greetings.strip().lower()


if greetings.startswith("hello"):
    print("$0" ,  end="")
elif greetings[0] == 'h':
    print("$20",  end="")
else:
    print("$100",  end="")


