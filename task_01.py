def caeser_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

def caeser_decrypt(ciphertext, shift):
    return caeser_encrypt(ciphertext, -shift)

def main():
    plaintext = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = caeser_encrypt(plaintext, shift)
    print("Encrypted text:", encrypted_text)
    decrypted_text = caeser_decrypt(encrypted_text, shift)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
