
"""
Alert! 
Tolong baca atau pelajari link 
dokumentasi yang saya sisip kan di 
beberapa statement.

Pelajari ascii convert untuk penggunaan variabel di bawah
link belajar:  https://youtu.be/x71kJyNvB5o?si=xhRIl1WwzKetasyJ

Pelajari juga cara kerja function encrpt & decrypt: https://youtu.be/QYng_rXg5OQ?si=R3QxmMEJW0GmafT9

note: mulai dari line 27 - 117 adalah function
"""


import tkinter as tk #GUI import tkinter alias tk
from tkinter import messagebox #msgbox for popup



# Variabel global untukmenyimpan huruf alphabet
letters = 'abcdefghijklmnopqrstuvwxyz'


# Encrypt function 
# sc: https://github.com/ashutosh17072004/Bhumitasks01
def encrypt(plaintext, key):
    ciphertext = ' '
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


# Decrypt function
# sc: https://github.com/ashutosh17072004/Bhumitasks01
def decrypt(ciphertext, key):
    plaintext = ' '
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



# Processing input & output
# mengambil teks dari widget
def process_input(action):
    plaintext = text_input.get("1.0", tk.END).strip()
    # "1.0" membaca baris pertama
    # tk.END menandai pembacaan hingga akhir
    key_input = entry_key.get()
    


# Validasi key input 0-25
# sc: nyontek mas irgi hehe
    if not key_input.isdigit() or not (0 <= int(key_input) <= 25):
        messagebox.showerror("Error", "Jangan biarkan KEY anda kosong\ndan cek kembali apakah key berupa\nangka antara 0 sampai 25.")
        return
    
    key = int(key_input)
    result = ""
   


# Call function sesuai input dari user
    if action == "encrypt":
        result = encrypt(plaintext, key)
    elif action == "decrypt":
        result = decrypt(plaintext, key)
    
    update_output(result)



# Update tampilan text_output dari hasil enc/dec
def update_output(text):
    text_output.config(state='normal')
    text_output.delete("1.0", tk.END)#delete text
    text_output.insert(tk.END, text)#add hasil enc/dec
    text_output.config(state='normal')



# About 
def show_about():
    messagebox.showinfo("About", "Encrypt & Decrypt Application\nLatest Version 1.2.5\nCreated with Tkinter\n\nMIT License\nhttps://github.com/DimazRizky/Caesar-chiper.py/blob/main/LICENSE")

# Credit 
def credit():
    messagebox.showinfo("Credit","Code contributor\n\n-------------------------------\n• Dimaz Rizky\n• Adam Eswyn\n-------------------------------\n Ver 1.2.5\nCopyright© 2024 \n(All Rights Reserved As Above")
    
    
    
 # Copy to clipboard
def copy_text(text_widget):
    root.clipboard_clear()
    root.clipboard_append(text_widget.get("1.0", tk.END).strip())
    messagebox.showinfo("Info", "Teks berhasil disalin ke clipboard.")



# Paste from clipboard
def paste_text(text_widget):
    try:
        clipboard_content = root.clipboard_get() 
        text_widget.insert(tk.END, clipboard_content)
    except tk.TclError:
        messagebox.showwarning("Warning", "Clipboard kosong.")
 
 
 
# GUI Setup 
# sc: chatGpt
# sc:https://youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&si=DzCLr37AeRjWdz_3
root = tk.Tk()
root.title("Proyek Caesar Cipher")
root.geometry("550x550")
root.config(bg="white")



# Navigation Bar
nav_bar = tk.Frame(root, bg="#4682B4", height=50)
nav_bar.pack(fill='x')



# Call menu
popup_menu = tk.Menu(root, tearoff=0)
popup_menu.add_command(label="About", command=show_about)
popup_menu.add_command(label="Credit", command=credit)
popup_menu.add_command(label="Exit", command=root.quit)



# Menu button
def show_popup(event):
    popup_menu.post(event.x_root, event.y_root)

menu_button = tk.Button(nav_bar, text="≡", bg="#4682B4", fg="white", font=("Arial", 16, "bold"), relief="flat")
menu_button.pack(side='left', padx=5)
menu_button.bind("<Button-1>", show_popup)

# Nav bar & page title
title_label = tk.Label(nav_bar, text="Caesar Cipher Tool", bg="#4682B4", fg="white", font=("Arial", 14, "bold"))
title_label.pack(side='left', padx=20)




# Fungsi untuk menambahkan placeholder pada Text widget
#SC GPT
def set_text_placeholder(text_widget, placeholder_text):
    text_widget.insert("1.0", placeholder_text)
    text_widget.config(fg="grey")

    def on_focus_in(event):
        if text_widget.get("1.0", "end-1c") == placeholder_text:
            text_widget.delete("1.0", "end")
            text_widget.config(fg="black")

    def on_focus_out(event):
        if text_widget.get("1.0", "end-1c") == "":
            text_widget.insert("1.0", placeholder_text)
            text_widget.config(fg="grey")

    text_widget.bind("<FocusIn>", on_focus_in)
    text_widget.bind("<FocusOut>", on_focus_out)

# Input plaintext (multi-line) dan scrollbar
input_frame = tk.Frame(root, bg="white")
input_frame.pack(pady=1, anchor='w', fill='x')
# fill x; menyelaraskan frame ke kiri dari window
# anchor w: memperluas frame horizontal



tk.Label(input_frame,  bg="white", font=("Arial", 12)).pack(anchor='w', padx=5, pady=5)
text_input_scrollbar = tk.Scrollbar(input_frame)
text_input_scrollbar.pack(side="right", fill="y")
# bg color: white
# font: Arial
# fontsize: 12


text_input = tk.Text(input_frame, height=5, width=60, font=("Arial", 12), bd=2, relief="groove", yscrollcommand=text_input_scrollbar.set)
text_input.pack(side="left", fill="x", expand=True)
"""

# height=5: Tinggi widget adalah 5 baris teks
# width=60: Lebar widget adalah 60 karakter
# font=("Arial", 12): font Arial ukuran 12.
# bd=2: Border widget ketebalan 2 piksel.
# relief="groove": Tipe border diatur menjadi groove.

# yscrollcommand=text_input_scrollbar.set: Menghubungkan scrollbar vertikal (text_input_scrollbar) dengan widget teks.


.pack(side="left", fill="x", expand=True):

side="left": Menempatkan widget teks di sisi kiri frame.

fill="x": Memperluas widget secara horizontal mengikuti lebar frame.

expand=True: Mengizinkan widget menyesuaikan ukurannya dengan frame.
"""



text_input_scrollbar.config(command=text_input.yview)

# Tambahkan placeholder ke Text widget
set_text_placeholder(text_input, "Masukkan teks Anda di sini...")



#Tombol Paste 
tk.Button(root, bg="#4682B4", font=("Arial", 5),fg="white", text="Paste", command=lambda: paste_text(text_input)).pack(padx=10, pady=1, ipadx=50)


# Fungsi untuk menampilkan placeholder
def set_placeholder(entry, placeholder_text):
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


# Input key
key_frame = tk.Frame(root, bg="white", pady=1)
key_frame.pack(ipady=5, anchor='center', padx=300)
tk.Label(key_frame, bg="white", font=("Arial", 12)).pack(padx=(0, 5))
entry_key = tk.Entry(key_frame, width=3, font=("Arial", 12), bd=2, relief="groove")
entry_key.pack(side='left')

# Tambahkan placeholder
set_placeholder(entry_key, "Key") 


# Fungsi untuk menambahkan placeholder pada Text widget (Output)
#SC GPT
def set_output_placeholder(text_widget, placeholder_text):
    text_widget.config(state='normal')  # Mengaktifkan Text widget sementara
    text_widget.insert("1.0", placeholder_text)
    text_widget.config(fg="grey", state='disabled')  # Kembali ke mode read-only


# Output (multi-line) dengan scrollbar
output_frame = tk.Frame(root, bg="white")
output_frame.pack(pady=1, anchor='w', fill='x')

tk.Label(output_frame, bg="white", font=("Arial", 12)).pack(anchor='w', pady=1)
text_output_scrollbar = tk.Scrollbar(output_frame)
text_output_scrollbar.pack(side="right", fill="y")

text_output = tk.Text(output_frame, height=5, width=60, font=("Arial", 12), bd=2, relief="groove", state='normal', yscrollcommand=text_output_scrollbar.set)
text_output.pack(side="left", fill="x", expand=True)

text_output_scrollbar.config(command=text_output.yview)



# Tambahkan placeholder ke Text widget (Output)
set_output_placeholder(text_output, "Hasil akan ditampilkan di sini...")


# Tombol Copy di bawah hasil teks
tk.Button(root, bg="#4682B4", font=("Arial", 5),fg="white", text="Copy", command=lambda: copy_text(text_output)).pack(padx=10, pady=1, ipadx=50)


# Buttons encrypt decrypt
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=20)

button_encrypt = tk.Button(button_frame, text="Encrypt", command=lambda: process_input("encrypt"), font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=10)
button_encrypt.pack(side='left', padx=10, pady=50)

button_decrypt = tk.Button(button_frame, text="Decrypt", command=lambda: process_input("decrypt"), font=("Arial", 12, "bold"), bg="#2196F3", fg="white", width=12)
button_decrypt.pack(side='left', padx=10)



# Run app
root.mainloop()
                
