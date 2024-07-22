# encryption.py

from cryptography.fernet import Fernet
import os

class Encryption:
    def __init__(self):
        self.key_file = 'secret.key'
        self.key = self._load_key()

    def _load_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
            return key

    def encrypt(self, message):
        fernet = Fernet(self.key)
        encrypted_message = fernet.encrypt(message.encode())
        return encrypted_message.decode()

    def decrypt(self, encrypted_message):
        fernet = Fernet(self.key)
        decrypted_message = fernet.decrypt(encrypted_message.encode())
        return decrypted_message.decode()