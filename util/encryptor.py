import base64

def encrypt_password(password):
    passwordBytes = password.encode('ascii')
    base64Bytes = base64.b64encode(passwordBytes)
    return base64Bytes.decode('ascii')

def decrypt_password(encryptedPassword):
    base64Bytes = encryptedPassword.encode('ascii')
    passwordBytes = base64.b64decode(base64Bytes)
    return passwordBytes.decode('ascii')

if __name__ == '__main__':
    encryptedPassword = encrypt_password("DJChampion")
    print(encryptedPassword)
    password = decrypt_password(encryptedPassword)
    print(password)