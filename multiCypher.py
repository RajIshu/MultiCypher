from Crypto.Cipher import AES

# Set the encryption key and initialization vector (IV)
key = b'mysecretpassword'
iv = b'1234567890123456'

# Set the input and output file paths
input_file = 'plaintext.txt'
output_file = 'ciphertext.txt'

# Encrypt the input file and write the ciphertext to the output file
with open(input_file, 'rb') as infile:
    with open(output_file, 'wb') as outfile:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        while True:
            plaintext = infile.read(1024)
            if len(plaintext) == 0:
                break
            elif len(plaintext) % 16 != 0:
                plaintext += b' ' * (16 - len(plaintext) % 16)
            ciphertext = cipher.encrypt(plaintext)
            outfile.write(ciphertext)

# Decrypt the ciphertext and write the plaintext to the output file
with open(output_file, 'rb') as infile:
    with open('decrypted.txt', 'wb') as outfile:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        while True:
            ciphertext = infile.read(1024)
            if len(ciphertext) == 0:
                break
            plaintext = cipher.decrypt(ciphertext)
            outfile.write(plaintext.rstrip())
