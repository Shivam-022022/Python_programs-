# Caesar Cipher
# Encrypt and decrypt a message using the Caesar Cipher algorithm.

message = input("Enter message: ")
shift = int(input("Enter shift: "))
encrypted = ""

for ch in message:
    if ch.isupper():
        encrypted += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
    elif ch.islower():
        encrypted += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
    else:
        encrypted += ch

print("Encrypted:", encrypted)

decrypted = ""
for ch in encrypted:
    if ch.isupper():
        decrypted += chr((ord(ch) - ord("A") - shift) % 26 + ord("A"))
    elif ch.islower():
        decrypted += chr((ord(ch) - ord("a") - shift) % 26 + ord("a"))
    else:
        decrypted += ch

print("Decrypted:", decrypted)
