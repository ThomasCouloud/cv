from cryptography.fernet import Fernet

#crypter
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

if __name__ == "__main__":
    data_to_encrypt = "EMAIL_USER=thomas.couloud.cfailda@gmail.com\nEMAIL_PASS=fghq fjwn tnmj fzvr"
    key = generate_key()
    encrypted_data = encrypt_data(data_to_encrypt, key)
    
    with open("encrypted_credentials.dat", "wb") as file:
        file.write(encrypted_data)

#décripter
def load_key():
    return open("secret.key", "rb").read()

def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data

if __name__ == "__main__":
    key = load_key()
    with open("encrypted_credentials.dat", "rb") as file:
        encrypted_data = file.read()

    decrypted_data = decrypt_data(encrypted_data, key)
    print(decrypted_data)
