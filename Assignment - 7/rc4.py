
# RC4 Algorithm

def rc4(data, key):
    # Step 1: Initialize the state array
    S = list(range(256))

    # Step 2: Key Scheduling Algorithm (KSA)
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Step 3: Pseudo Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    result = []

    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        t = (S[i] + S[j]) % 256
        k = S[t]

        result.append(char ^ k)

    return bytes(result)


# Get input from user
message = input("Enter the plaintext: ")
key = input("Enter the secret key: ")

if not key:
    print("Key cannot be empty!")
else:
    # Encryption
    encrypted = rc4(message.encode(), key.encode())
    print("Encrypted Text:", encrypted.hex())

    # Decryption
    decrypted = rc4(encrypted, key.encode())
    print("Decrypted Text:", decrypted.decode())