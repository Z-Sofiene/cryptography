import tkinter as tk
from tkinter import messagebox, filedialog
import json
import random
import subprocess


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
    return (e, n), (d, n)


def cryptRSA(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]


def decryptRSA(encrypted_message, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in encrypted_message])


def generate_rsa_keys():
    username = entry_username.get()
    if username:
        public_key, private_key = gen_key(1000, 10000)

        with open(f"public_key_{username}.json", "w") as public_key_file:
            json.dump({"e": public_key[0], "n": public_key[1]}, public_key_file)

        with open(f"private_key_{username}.json", "w") as private_key_file:
            json.dump({"d": private_key[0], "n": private_key[1]}, private_key_file)

        messagebox.showinfo("Success", "RSA key pairs generated and saved successfully.")
    else:
        messagebox.showerror("Error", "Please enter your name.")


root = tk.Tk()
root.title("RSA Key Generator")
frame = tk.Frame(root)
frame.pack(padx=50, pady=50)

label_username = tk.Label(frame, text="Enter your name:")
label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=10, pady=10)

btn_generate = tk.Button(frame, text="Generate RSA Keys", command=generate_rsa_keys)
btn_generate.grid(row=1, columnspan=2, padx=10, pady=10)

root.mainloop()
