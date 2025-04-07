def consoante_ou_vogal():
    letra = input("Digite alguma letra do alfabeto (A té o Z): ").strip().upper()

    if letra.isalpha() and len(letra) == 1:
        if letra in ("AEIOU"):
            print("Vogal!")
        else:
            print("Consoante!")
    else:
        print("Digite algo válido!")


consoante_ou_vogal()



