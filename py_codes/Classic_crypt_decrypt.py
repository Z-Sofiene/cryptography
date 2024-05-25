def construction_horizontal(cle):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cle2 = cle.lower() + alphabet
    NewAlphabet = ""
    for i in cle2:
        if i in alphabet:
            NewAlphabet += i
            alphabet = alphabet.replace(i, '#')
    return NewAlphabet


def construction_vertical(cle):
    cle2 = construction_horizontal(cle)  # Alphabet Chiffrée
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cle = cle.lower()
    cle3 = ""  # cle nettoyé sera inserer ici
    for i in cle:
        if i in alphabet:
            cle3 += i
            alphabet = alphabet.replace(i, '#')

    cleFinal = ""  # alphabet de chiffrement
    tailleCle = len(cle3)
    for i in range(tailleCle):
        for j in range(i, len(cle2), tailleCle):
            cleFinal += cle2[j]
    return cleFinal


def alphabetDesordonne(alphabetDepart, alphabetFinal, message):
    messageChiffree = ""
    for i in message:
        messageChiffree += alphabetDepart[alphabetFinal.index(i)]
    return messageChiffree


def Formatage(text):
    message = ""
    compteur = 0
    for i in text:
        compteur += 1
        message += i
        if compteur % 5 == 0:
            message += " "
    return message.upper()


def deformatage(text):
    message = ""
    for i in text:
        if i == " ":
            continue
        message += i

    return message


def ChAffine(a, b, message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    messageChiffree = ""
    message=deformatage(message)
    for i in message:
        messageChiffree += alphabet[((alphabet.index(i) * a + b) % 26)]
    return messageChiffree


def inverseMod26(a):
    for i in range(1, 26, 2):
        if i == 13:
            continue
        if (a * i) % 26 == 1:
            return i


def DechAffine(a, b, message):
    c = inverseMod26(a)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    messageDechiffree = ""
    for i in message.lower():
        messageDechiffree += alphabet[(((alphabet.index(i) - b) * c) % 26)]
    return messageDechiffree


def ChiffPorta(message, cle):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = ["ABCDEFGHIJKLM", "NOPQRSTUVWXYZ", "ZNOPQRSTUVWXY", "YZNOPQRSTUVWX", "XYZNOPQRSTUVW", "WXYZNOPQRSTUV",
             "VWXYZNOPQRSTU", "UVWXYZNOPQRST", "TUVWXYZNOPQRS", "STUVWXYZNOPQR", "RSTUVWXYZNOPQ", "QRSTUVWXYZNOP",
             "PQRSTUVWXYZNO", "OPQRSTUVWXYZN"]

    message = message.upper()
    message = deformatage(message)
    cle = cle.upper()
    cle = deformatage(cle)
    messagC = ""

    for i in range(len(message)):
        a = alphabet.index(cle[i % len(cle)]) // 2 + 1
        if message[i] in alpha[0]:
            messagC += alpha[a][alpha[0].index(message[i])]
        else:
            messagC += alpha[0][alpha[a].index(message[i])]

    return messagC


def DechiffPorta(message, cle):
    return ChiffPorta(message, cle).lower()


def CleNumerique(cle):
    cle = cle.upper()
    cle = cle.replace(" ", "")
    cle2 = sorted(cle)
    position = []
    for char in cle:
        position.append(cle2.index(char))
        cle2[cle2.index(char)] = None
    return position


def ChiffTransposition(message, cle):
    message = message.replace(" ", "").upper()
    CleNum = CleNumerique(cle)
    if len(message) % len(cle) != 0:
        for i in range(len(cle) - len(message) % len(cle)):
            message += "X"
        # while len(message)%len(cle) != 0 :
    # message+="X"
    compteur = 0
    bloc = []
    for i in range(0, len(message), len(cle)):
        bloc.append(message[i:i + len(cle)])
    return bloc


def textCount(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    IC = 0
    text = text.replace(" ", "")
    message = "|"
    for i in alphabet:
        for j in range(len(text)):
            if i == text[j]:
                count += 1
        IC += (count * (count - 1)) / (len(text) * (len(text) - 1))
        message += "{}={}|".format(i, count)
        count = 0
    return message + "\nIC={}\nLongueur du text = {}".format(IC, len(text))


def LenCle(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    text = text.replace(" ", "")
    pas = 1
    while True:
        text2 = ""
        IC = 0
        for i in range(0, len(text), pas):
            text2 += text[i]
        for i in alphabet:
            for j in range(len(text2)):
                if i == text2[j]:
                    count += 1
            IC += (count * (count - 1)) / (len(text2) * (len(text2) - 1))
            count = 0
        if IC > 0.07:
            break
        pas += 1
    n = 0
    cleFinal = ""
    while True:
        cle = {}
        message = ""
        for i in range(n, len(text), pas):
            message += text[i]
        message += "\n"
        for i in alphabet:
            for j in range(len(message)):
                if i == message[j]:
                    count += 1
            IC += (count * (count - 1)) / (len(message) * (len(message) - 1))
            message += "{}={}|".format(i, count)
            cle[count] = {}
            cle[count] = i
            count = 0
        cleFinal += alphabet[alphabet.index(cle[max(cle)]) - 4]
        print("Text N°:{}\n{}\nIC={}\n".format(n + 1, message, IC))
        n += 1
        if n == pas:
            break
    print("Cle = {}".format(cleFinal))
    return cleFinal


def chiCesar(pas, text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.replace(" ", "")
    message = ""
    compteur = 0
    text = text.lower()
    for i in text:  # // salut mes amis // X
        message += alphabet[(alphabet.index(i) + pas) % 26].upper()
        compteur += 1
        if compteur == 5:
            message += " "
            compteur = 0
    return message


def dechiCesar(pas, text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.replace(" ", "")
    text = text.lower()
    message = ""
    for i in text:
        message += alphabet[(alphabet.index(i) - pas) % 26]
    return message


def chiVeg(cle, txt):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    txt1 = txt.replace(" ", "")
    lent = len(txt)
    txtChiff = ""
    for i in range(lent):
        postxt = alphabet.index(txt1[i])
        poscle = alphabet.index(cle[i % len(cle)])
        pos = (postxt + poscle)
        if pos > 25:
            pos = pos % 26
        txtChiff += alphabet[pos]
    return txtChiff


def decVeg(cle, txt):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cle = cle.lower()
    txt1 = txt.replace(" ", "")
    txt1 = txt1.lower()
    lent = len(txt1)
    txtClair = ""
    j = 0
    for i in range(lent):
        postxt = alphabet.index(txt1[i])
        poscle = alphabet.index(cle[j])
        pos = (postxt - poscle)
        if pos < 0:
            pos = pos + 26
        txtClair += alphabet[pos]
        j += 1
        if j == len(cle):
            j = 0
    return txtClair

def main():
    while True:
        print("Choisissez une option :")
        print("1. Construction Horizontale")
        print("2. Construction Verticale")
        print("3. Affine")
        print("4. Porta")
        print("5. Transposition")
        print("6. César")
        print("7. Vigenère")
        print("8. Quitter")

        choice = input("Entrez votre choix (1-8) : ")

        if choice == '8':
            print("Sortie...")
            break

        try:
            choice = int(choice)
        except ValueError:
            print("Veuillez entrer un nombre entre 1 et 8.")
            continue

        if choice < 1 or choice > 8:
            print("Veuillez entrer un nombre entre 1 et 8.")
            continue

        if choice == 1:
            cle = input("Entrez la clé : ")
            result = construction_horizontal(cle)
        elif choice == 2:
            cle = input("Entrez la clé : ")
            result = construction_vertical(cle)
        elif choice == 3:
            choix = input("Chiffrement (C) ou Déchiffrement (D) ? : ").upper()
            if choix == 'C':
                try:
                    a = int(input("Entrez la valeur de 'a' : "))
                    b = int(input("Entrez la valeur de 'b' : "))
                except ValueError:
                    print("Veuillez entrer des entiers pour 'a' et 'b'.")
                    continue
                message = input("Entrez le message : ")
                result = Formatage(ChAffine(a, b, message))
            elif choix == 'D':
                try:
                    a = int(input("Entrez la valeur de 'a' : "))
                    b = int(input("Entrez la valeur de 'b' : "))
                except ValueError:
                    print("Veuillez entrer des entiers pour 'a' et 'b'.")
                    continue
                message = input("Entrez le message : ")
                result = DechAffine(a, b, deformatage(message))
            else:
                print("Choix invalide")
                continue
        elif choice == 4:
            choix = input("Chiffrement (C) ou Déchiffrement (D) ? : ").upper()
            if choix == 'C':
                message = input("Entrez le message : ")
                cle = input("Entrez la clé : ")
                result = Formatage(ChiffPorta(message, cle))
            elif choix == 'D':
                message = input("Entrez le message : ")
                cle = input("Entrez la clé : ")
                result = DechiffPorta(deformatage(message), cle)
            else:
                print("Choix invalide")
                continue
        elif choice == 5:
            message = input("Entrez le message : ")
            cle = input("Entrez la clé : ")
            result = ChiffTransposition(message, cle)
        elif choice == 6:
            choix = input("Chiffrement (C) ou Déchiffrement (D) ? : ").upper()
            if choix == 'C':
                try:
                    pas = int(input("Entrez la valeur de décalage : "))
                except ValueError:
                    print("Veuillez entrer un entier pour le décalage.")
                    continue
                message = input("Entrez le message : ")
                result = Formatage(chiCesar(pas, message))
            elif choix == 'D':
                try:
                    pas = int(input("Entrez la valeur de décalage : "))
                except ValueError:
                    print("Veuillez entrer un entier pour le décalage.")
                    continue
                message = input("Entrez le message : ")
                result = dechiCesar(pas, deformatage(message))
            else:
                print("Choix invalide")
                continue
        elif choice == 7:
            choix = input("Chiffrement (C) ou Déchiffrement (D) ? : ").upper()
            if choix == 'C':
                cle = input("Entrez la clé : ")
                message = input("Entrez le message : ")
                result = Formatage(chiVeg(cle, message))
            elif choix == 'D':
                cle = input("Entrez la clé : ")
                message = input("Entrez le message : ")
                result = decVeg(cle, deformatage(message))
            else:
                print("Choix invalide")
                continue
        else:
            print("Choix invalide")
            continue

        print("Résultat :", result)


if __name__ == "__main__":
    main()
