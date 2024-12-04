answer = input("What is the answer to the great question of life, the universe and everything? ")

answer = answer.strip().lower()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("yes")
else:
    print("no")
