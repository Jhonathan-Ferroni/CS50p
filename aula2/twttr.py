def main():
    phrase = input("Input: ")
    txt = remvowels(phrase)
    print("Output:",txt)

def remvowels(text):
    result = ""
    for c in text:
        if c.lower() in "aeiou":
            continue
        else:
            result += c
    return result

main()
