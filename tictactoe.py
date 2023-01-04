# definiraj ploču od 9 polja
ploca = [" "] * 9

# prvi igrač je igrač X
igrac = 'X'

# petlja
while True:
    # print trenutnog stanja ploče
    print(f" {ploca[0]} | {ploca[1]} | {ploca[2]} ")
    print("-----------")
    print(f" {ploca[3]} | {ploca[4]} | {ploca[5]} ")
    print("-----------")
    print(f" {ploca[6]} | {ploca[7]} | {ploca[8]} ")

    # unesi potez
    potez = int(input(f"Na redu je igrač: {igrac}. Unesi svoj potez (1-9): "))
    
    # provjera da polje nije zauzeto
    if ploca[potez-1] != ' ':
        print("To polje je već zauzeto.")
        continue
    ploca[potez-1] = igrac

    # dobitne kombinacije
    # 1 - 2 - 3
    if (ploca[0] == igrac and ploca[1] == igrac and ploca[2] == igrac):
        print(f"{igrac} je pobijedio!")
        break
    # 4 - 5 - 6
    elif (ploca[3] == igrac and ploca[4] == igrac and ploca[5] == igrac):
        print(f"{igrac} je pobijedio!")
        break
    # 7 - 8 - 9
    elif (ploca[6] == igrac and ploca[7] == igrac and ploca[8] == igrac):
        print(f"{igrac} je pobijedio!")
        break
    # 1 - 4 - 7
    elif (ploca[0] == igrac and ploca[3] == igrac and ploca[6] == igrac):
        print(f"{igrac} je pobijedio!")
        break
    # 2 - 5 - 8
    elif (ploca[1] == igrac and ploca[4] == igrac and ploca[7] == igrac):
        print(f"{igrac} je pobijedio!")
        break
    # 3 - 6 - 9
    elif (ploca[2] == igrac and ploca[5] == igrac and ploca[8] == igrac):
        print(f"{igrac} je pobijedio!")
        break
    # 1 - 5 - 9
    elif (ploca[0] == igrac and ploca[4] == igrac and ploca[8] == igrac):
        print(f"{igrac} je pobijedio!")
        break
    # 3 - 5 - 7
    elif (ploca[2] == igrac and ploca[4] == igrac and ploca[6] == igrac):
        print(f"{igrac} je pobijedio!")
        break
    # Provjera da li je završilo neriješeno?
    elif ploca.count(" ") == 0:
         print(f"Igra je završila neriješeno.")   
         break

    # prebaci na novog igrača
    if igrac == 'X':
        igrac = 'O'
    else:
         igrac = 'X'