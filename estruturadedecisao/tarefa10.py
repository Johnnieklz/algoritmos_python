def turno_escola():
    turno = input(
        "Digite apenas a inicial do seu turno. \n (M) - Matutino \n (V) - Vespertino \n (N) - Noturno: ").upper()

    if turno == 'M':
        print("Bom dia!!")

    elif turno == 'V':
        print("Boa tarde!!")

    elif turno == 'N':
        print("Boa noite!!")

    else:
        print("Valor inválido!!")


turno_escola()