import tkinter as tk
from tkinter import filedialog, messagebox
import json

def read_key_from_json(file_path):
    with open(file_path, 'r') as file:
        key_data = json.load(file)
    if 'e' in key_data and 'n' in key_data:
        return key_data['e'], key_data['n']
    elif 'd' in key_data and 'n' in key_data:
        return key_data['d'], key_data['n']
    else:
        raise ValueError("Invalid key format in JSON file")

def cryptRSA(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

def decryptRSA(encrypted_message, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in encrypted_message])

def encrypt_message():
    message = entry_message.get("1.0", "end-1c")
    public_key_file = filedialog.askopenfilename(title="Select Public Key JSON File")
    if not public_key_file:
        messagebox.showerror("Error", "Please select a public key file.")
        return
    try:
        public_key = read_key_from_json(public_key_file)
        encrypted_message = cryptRSA(message, public_key)
        entry_result.delete("1.0", "end")
        entry_result.insert("end", str(encrypted_message))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_message():
    encrypted_message_str = entry_message.get("1.0", "end-1c")
    encrypted_message = json.loads(encrypted_message_str)
    private_key_file = filedialog.askopenfilename(title="Select Private Key JSON File")
    if not private_key_file:
        messagebox.showerror("Error", "Please select a private key file.")
        return
    try:
        private_key = read_key_from_json(private_key_file)
        decrypted_message = decryptRSA(encrypted_message, private_key)
        entry_result.delete("1.0", "end")
        entry_result.insert("end", decrypted_message)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("RSA Encryption/Decryption")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_message = tk.Label(frame_input, text="Message:")
label_message.grid(row=0, column=0)

entry_message = tk.Text(frame_input, height=5, width=50)
entry_message.grid(row=0, column=1)

button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message)
button_encrypt.pack(pady=5)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message)
button_decrypt.pack(pady=5)

frame_result = tk.Frame(root)
frame_result.pack(pady=10)

label_result = tk.Label(frame_result, text="Result:")
label_result.grid(row=0, column=0)

entry_result = tk.Text(frame_result, height=5, width=50)
entry_result.grid(row=0, column=1)

root.mainloop()
