def main():
    phrase = input("Digite a phrase with a emoticon like :) or :(  ")
    print (convert(phrase))
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text
main()
