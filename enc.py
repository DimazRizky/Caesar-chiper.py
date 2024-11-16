
# import library tkinter dengan alias tk
# from lib tkinter saya import massagebox
import tkinter as tk
from tkinter import messagebox

# Alphabet
letters = 'abcdefghijklmnopqrstuvwxyz'

# Funct untuk encrypt teks
# sc: https://github.com/ashutosh17072004/Bhumitasks01
def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = (index + key) % 26
                ciphertext += letters[new_index]
        else:
            ciphertext += ' '
    return ciphertext


# Funct untuk decrypt teks
# sc: https://github.com/ashutosh17072004/Bhumitasks01
def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = (index - key) % 26
                plaintext += letters[new_index]
        else:
            plaintext += ' '
    return plaintext


"""
identifikasi kalo input key lebih dari 25
atau jika bukan angka (huruf) maka function
dibawah nampilin error massage dan stop 
program
"""
#sc: chatGPT (GAK BISA NJIR T_T)
"""def process_input(action):
    try:
        plaintext = entry1.get()
        key = int(entry_square.get())
        if key > 25:
            messagebox.showerror("Error", "ERROR! Key tidak boleh lebih dari 25") 
            #popup error
            root.destroy()#stop program
            return
        if action == "encrypt":
            result = encrypt(plaintext, key)
        elif action == "decrypt":
            result = decrypt(plaintext, key)
        update_entry2(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid Key!")  # popup error
        root.destroy() # stop porgram
"""


# ------- GUI --------

# placeholder
def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg='grey')

    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder_text)
            entry.config(fg='grey')

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


# Proses input dan refresh output
def process_input(action):
    try:
        plaintext = entry1.get()
        key = int(entry_square.get())
        if action == "encrypt":
            result = encrypt(plaintext, key)
        elif action == "decrypt":
            result = decrypt(plaintext, key)
        update_entry2(result)
    except ValueError:
        update_entry2("Invalid Key!")  # Jika key bukan angka/num_letter


# Memperbarui (entry2)
def update_entry2(text):
    entry2.config(state='normal')
    entry2.delete(0, tk.END)
    entry2.insert(0, text)
    entry2.config(state='readonly')
"""
note: Entry2 perlu di perbarui karena
input pada entry2/hasil dari encrypt
dan decrypt tidak dapat di hapus atau 
di rubah karena input bersifat READONLY.

"""

# Main window
root = tk.Tk()
root.title("Enc & Dec Caesar Cipher")

# Input plaintext (placeholder)
entry1 = tk.Entry(root, width=30)
entry1.grid(row=0, column=0, padx=10, pady=5)
# Row 0 | column 0 | padding x 10 | padding y 5
add_placeholder(entry1, "Masukkan plain text...")


# Output hasil(readonly)
#sc: chatGPT
entry2 = tk.Entry(root, width=30, state='readonly')
entry2.grid(row=1, column=0, padx=10, pady=5)
add_placeholder(entry2, "Hasil...")



# Input key (placeholder)
entry_square = tk.Entry(root, width=10)
entry_square.grid(row=2, column=0, padx=10, pady=5)
add_placeholder(entry_square, "Key...")



# Button encrypt
button1 = tk.Button(root, text="Encrypt", command=lambda: process_input("encrypt"))
# Row 3 | column 0 | padding x 10 | padding y 5
button1.grid(row=3, column=0, padx=10, pady=5)


# Button decrypt
button2 = tk.Button(root, text="Decrypt", command=lambda: process_input("decrypt"))
# Row 4 | column 0 | padding x 10 | padding y 5
button2.grid(row=4, column=0, padx=10, pady=5)

# Run program
root.mainloop()


# MIT License | Github DimazRizky
# https://github.com/DimazRizky/Caesar-chiper.py/blob/main/LICENSE