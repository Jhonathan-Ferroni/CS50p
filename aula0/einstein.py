def main():
    M = int(input("Digit the mass to discover the energy equivalent: \n"))
    result = mult(M)
    print (result)
def mult(mass):
    c = int(300000000)
    E = mass*c*c
    return E

main()


