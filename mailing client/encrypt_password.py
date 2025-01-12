from cryptography.fernet import Fernet
'''
# Generate a key and write it to a file
key = Fernet.generate_key()
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Encrypt the password
password = 'enter your password here'.encode()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(password)

# Write the encrypted password to a file
with open('encrypted_password.bin', 'wb') as encrypted_file:
    encrypted_file.write(cipher_text)
    
    '''
print("Key and encrypted password files have been generated.")