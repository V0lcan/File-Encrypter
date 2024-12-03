from cryptography.fernet import Fernet
import os, filetype

# Used to select key file.
def select_key_file(keyfile):
    if os.path.exists(keyfile) == False: # If file-encrypter.key file does not exist, create it.
        with open(keyfile, 'wb') as filekey:
            key = Fernet.generate_key()
            filekey.write(key)
    
    with open(keyfile, 'rb') as filekey:
        key = filekey.read() # Read the key from file-encrypter.key file.
    
    return Fernet(key)

# Used to encrypt images.
def encrypt_image(img, fernet_key):
    with open(img, 'rb') as file:
        file_data = file.read()

    encrypted_data = fernet_key.encrypt(file_data)

    with open(img, 'wb') as file:
        file.write(encrypted_data)

# Used to encrypt files.
def encrypt_file(filename, fernet_key):
    kind = filetype.guess(filename)
    if kind and kind.mime.startswith('image/'): # If the file is an image, encrypt it as an image.
        encrypt_image(filename, fernet_key)
    
    else:
        with open(filename, 'r') as file: # Read file contents.
            file_data = file.read()

        encrypted_data = fernet_key.encrypt(file_data.encode()) # Encrypt file contents.

        with open(filename, 'w') as file: # Write encrypted data to file.
            file.write(encrypted_data.decode())

# Used to decrypt files.
def decrypt_file(filename, fernet_key):
    with open(filename, 'rb') as file: # Read file contents.
        file_data = file.read()

    decrypted_data = fernet_key.decrypt(file_data)

    with open(filename, 'wb') as file: # Write decrypted data to file.
        file.write(decrypted_data)

# Used to encrypt/decrypt files.
def encrypt_directory(directory, fernet_key):
    for root, dirs, files in os.walk(directory, topdown=True):
        print("Encrypting directory: " + root)
        for dir in dirs:
            print(dir + " is a subdirectory. Skipping...")
        for file in files:
            print("Encrypting file: " + file)
            file_to_encrypt = os.path.join(root, file)
            encrypt_file(file_to_encrypt, fernet_key)
            print("Done! \n---------------------------------")

def decrypt_directory(directory, fernet_key):
    for root, dirs, files in os.walk(directory, topdown=True):
        print("Decrypting directory: " + root)
        for dir in dirs:
            print(dir + " is a subdirectory. Skipping...")
        for file in files:
            print("Decrypting file: " + file)
            file_to_decrypt = os.path.join(root, file)
            decrypt_file(file_to_decrypt, fernet_key)
            print("Done! \n---------------------------------")

def encrypt(filepath, fernet_key):
    if os.path.isdir(filepath):
        encrypt_directory(filepath, fernet_key)
    else:
        encrypt_file(filepath, fernet_key)

def decrypt(filepath, fernet_key):
    if os.path.isdir(filepath):
        decrypt_directory(filepath, fernet_key)
    else:
        decrypt_file(filepath, fernet_key)