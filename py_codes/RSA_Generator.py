import random


def not_prime(nombre):
    if nombre == 2:
        return False
    if nombre % 2 == 0:
        return True
    k = 0
    for i in range(3, nombre // 2 + 1, 2):
        if nombre % i == 0:
            k += 1
            if k == 2:
                return True
    return False


def prime(start, end):
    tab = []
    for i in range(start, end):
        if not not_prime(i):
            tab.append(i)
    return tab


def pgcd(a, b):
    while b != 0:
        # a=b
        # b=a%b
        a, b = b, a % b
    return a


def InvMod(b, n):
    n0 = n
    b0 = b
    t0 = 0
    t = 1
    q = n // b
    r = n - q * b
    i = 0
    while r > 0:
        temp = t0 - q * t
        if temp >= 0:
            temp = temp % n
        else:
            temp = n - ((-temp) % n)
        t0 = t
        t = temp
        n0 = b0
        b0 = r
        q = n0 // b0
        r = n0 - q * b0
        i += 1
    if (b0 != 1):
        return -1
    else:
        return t


def rand(x, y):
    return random.randint(x, y)


def gen_key(start, end):
    tab = prime(start, end)
    rand1 = rand(0, len(tab))
    rand2 = rand(0, len(tab))
    while rand1 == rand2:
        rand2 = rand(0, len(tab))
    p = tab[rand1]
    q = tab[rand2]
    n = p * q
    fi_n = (p - 1) * (q - 1)
    e = 0
    for i in range(rand(1, fi_n), fi_n, 1):
        if pgcd(fi_n, i) == 1:
            e = i
            break
    d = InvMod(e, fi_n)
    print("Private Exponent 'd' = " + str(d) + "\nPublic Exponent 'e' = " + str(e) + "\nModulus 'n' = " + str(n) +
          "\nThese components are integral to the RSA algorithm :"
          "\nThe public exponent and the modulus form the public key."
          "\nThe private exponent et the modulus form the private key.")

    return (e, n), (d, n)


public_key, private_key = gen_key(100, 1000)


def cryptRSA(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]


def decryptRSA(encrypted_message, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in encrypted_message])


def generate_rsa_scripts(username, public_key, private_key):
    with open(f"KeyRSA_{username}.py", "w") as KeyRSA:
        KeyRSA.write("""#!/usr/bin/env python
e, n = {0}
d, n = {1}

def encrypt_public(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def encrypt_private(message, d, n):
    return [pow(ord(char), d, n) for char in message]

def decrypt_public(message, e, n):
    return ''.join([chr(pow(char, e, n)) for char in message])

def decrypt_private(message, d, n):
    return ''.join([chr(pow(char, d, n)) for char in message])

def main():
    while True:
        print('Choose an option:')
        print('\\t1. Crypt with Private Key')
        print('\\t2. Decrypt with Private Key')
        print('\\t3. Crypt with Public Key')
        print('\\t4. Decrypt with Public Key')
        print('\\t5. Exit')

        choice = input('Enter choice: ')

        if choice == '1':
            message = input('Enter message to encrypt with private key: ')
            encrypted = encrypt_private(message, d, n)
            print('Encrypted message:', encrypted)

        elif choice == '2':
            message = input('Enter encrypted message to decrypt with private key (space-separated numbers): ')
            message = message.replace('[', '').replace(']', '').replace(',', '').split()
            message = [int(x) for x in message]
            decrypted = decrypt_private(message, d, n)
            print('Decrypted message:', decrypted)

        elif choice == '3':
            message = input('Enter message to encrypt with public key: ')
            encrypted = encrypt_public(message, e, n)
            print('Encrypted message:', encrypted)

        elif choice == '4':
            message = input('Enter encrypted message to decrypt with public key (space-separated numbers): ')
            message = message.replace('[', '').replace(']', '').replace(',', '').split()
            message = [int(x) for x in message]
            decrypted = decrypt_public(message, e, n)
            print('Decrypted message:', decrypted)

        elif choice == '5':
            break

        else:
            print('Invalid choice, please try again.')

if __name__ == '__main__':
    main()
""".format(public_key, private_key))

def main():
    username = input("Enter the name of the new key owner: ")
    public_key, private_key = gen_key(1000, 10000)
    generate_rsa_scripts(username, public_key, private_key)
    print("RSA key pairs and executable scripts generated successfully.")


if __name__ == "__main__":
    main()
