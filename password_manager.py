import os
import json
from encryption import Encryption
from utils import load_passwords, save_passwords

class PasswordManager:
    def __init__(self):
        self.encryption = Encryption()
        self.password_file = 'passwords.json'
        self.passwords = load_passwords(self.password_file)

    def add_password(self, service, password):
        encrypted_password = self.encryption.encrypt(password)
        self.passwords[service] = encrypted_password
        self._save()

    def retrieve_password(self, service):
        encrypted_password = self.passwords.get(service)
        if encrypted_password:
            return self.encryption.decrypt(encrypted_password)
        else:
            raise ValueError("Service not found")

    def delete_password(self, service):
        if service in self.passwords:
            del self.passwords[service]
            self._save()
        else:
            raise ValueError("Service not found")

    def update_password(self, service, new_password):
        if service in self.passwords:
            self.add_password(service, new_password)
        else:
            raise ValueError("Service not found")

    def _save(self):
        save_passwords(self.password_file, self.passwords)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Secure Password Manager")
    parser.add_argument('command', choices=['add', 'retrieve', 'delete', 'update'], help='Command to execute')
    parser.add_argument('--service', required=True, help='Service name')
    parser.add_argument('--password', help='Password for the service')

    args = parser.parse_args()
    pm = PasswordManager()

    if args.command == 'add':
        if not args.password:
            raise ValueError("Password is required for add command")
        pm.add_password(args.service, args.password)
        print(f"Password for {args.service} added successfully.")

    elif args.command == 'retrieve':
        print(f"Password for {args.service}: {pm.retrieve_password(args.service)}")

    elif args.command == 'delete':
        pm.delete_password(args.service)
        print(f"Password for {args.service} deleted successfully.")

    elif args.command == 'update':
        if not args.password:
            raise ValueError("Password is required for update command")
        pm.update_password(args.service, args.password)
        print(f"Password for {args.service} updated successfully.")