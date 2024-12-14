def main():
    palavra = input("Type camel case: ")
    palavrasnake = snake_case(palavra)
    print(palavrasnake)

def snake_case(word):
    ##definindo string vazia pra ir armazenando os caracteres
    result = ""
    for c in word:
        if c.isupper():
            result += "_" + c.lower()
        else:
            result += c
    return result

main()
