from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
import EncryptionModule

# TODO:
# - ADD a way to manually select key file/path to create key file in.
# - FIX bug where the select file button crashed the whole program. (Might be OS X specific)

fernet = EncryptionModule.select_key_file('file-encrypter.key')

def select_file():
    filepath.delete(0, tk.END) # Clear text field.

    filepath_select = tk.filedialog.askopenfilename(initialdir=".", title="Select file", filetypes=(("all files", "*.*"), ("image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff;*.webp"), ("text files", "*.txt;*.docx;*.doc;*.pdf;*.rtf;*.odt;*.html;*.xml;*.csv;*.json;*.log;*.md;*.tex;*.yaml;*.yml;*.ini;*.cfg;*.conf;*.properties;*.env;*.sh;*.bat;*.cmd;*.ps1;*.psm1;*.psd1;*.ps1xml;*.pssc;*.psc1")))
    return filepath_select

def select_directory():
    filepath.delete(0, tk.END) # Clear text field.

    directory = tk.filedialog.askdirectory(initialdir=".", title="Select directory")
    return directory

# GUI
app = tk.Tk()
app.title("File Encrypter")
app.geometry("450x100")
app.resizable(False, False)

label_frame = tk.Frame(app)
label_frame.pack()

filepath_label = tk.Label(label_frame, text="Enter filepath:")
filepath_label.grid(row=0, column=0, pady=10)

filepath = tk.Entry(label_frame)
filepath.grid(row=0, column=1)

selection_frame = tk.Frame(label_frame)
selection_frame.grid(row=1, column=0, padx=5)

select_file_button = tk.Button(selection_frame, text="Select file", command=lambda: filepath.insert(0, select_file()))
select_file_button.grid(row=0, column=0)

select_directory_button = tk.Button(selection_frame, text="Select directory", command=lambda: filepath.insert(0, select_directory()))
select_directory_button.grid(row=0, column=1)

encrypt_decrypt_frame = tk.Frame(label_frame)
encrypt_decrypt_frame.grid(row=1, column=1, padx=5)

encrypt_button = tk.Button(encrypt_decrypt_frame, text="Encrypt", command=lambda: EncryptionModule.encrypt(filepath.get(), fernet))
encrypt_button.grid(row=1, column=0)

decrypt_button = tk.Button(encrypt_decrypt_frame, text="Decrypt", command=lambda: EncryptionModule.decrypt(filepath.get(), fernet))
decrypt_button.grid(row=1, column=1)

app.mainloop()