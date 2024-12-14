def main():
    phrase = input("Plate: ")
    bool1 = two(phrase)
    bool2 = maxi(phrase)
    bool3 = end(phrase)
    bool4 = per(phrase)

    if bool1 and bool2 and bool3 and bool4:  # Todas as condições devem ser verdadeiras
        print("Valid")
    else:
        print("Invalid")

def two(plate):
    # Verifica se a string tem pelo menos 2 caracteres e se os dois primeiros são letras
    if len(plate) >= 2 and plate[0].isalpha() and plate[1].isalpha():
        return True
    return False


#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def maxi(plate):
    tam = len(plate)
    if tam > 6 or tam < 2:
        return False
    return True

#“Numbers cannot be used in the middle of a plate; they must come at the end. For example,
# AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def end(plate):
    has_number_started = False
    for c in plate:
        if c.isdigit():
            if not has_number_started:
                has_number_started = True
                if c == '0':
                    return False
        elif has_number_started:
            return False
    return True
#“No periods, spaces, or punctuation marks are allowed.”
def per(plate):
    for c in plate:
        if c in " ,.":
            return False
    return True

main()


