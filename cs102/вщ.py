def encrypt_vigenere(plaintext, keyword):
    """
    »> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    »> encrypt_vigenere("python", "a")
    'python'
    »> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    key = keyword.lower()
    ciphertext = ""
    alph = "abcdefghijklmnopqrstuvwxyz"
    abc = 26
    for m in range(len(plaintext)):
        wordcode = ord(plaintext[m])
        keycode = alph.find(key[m % len(key)])
        if (97 <= wordcode <= 122):
            if (97 <= wordcode + keycode <= 122):
                ciphertext += chr(wordcode + keycode)
            else:
                ciphertext += chr(wordcode + keycode - abc)
        elif (65 <= wordcode <= 90):
            if (65 <= wordcode + keycode <= 90):
                ciphertext += chr(wordcode + keycode)
            else:
                ciphertext += chr(wordcode + keycode - abc)
        else:
            ciphertext += plaintext[m]
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.

    »> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    »> decrypt_vigenere("python", "a")
    'python'
    »> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    key = str(keyword).lower()
    plaintext = ""
    alph = "abcdefghijklmnopqrstuvwxyz"
    abc = 26
    for m in range(len(str(ciphertext))):
        wordcode = ord(str(ciphertext)[m])
        keycode = alph.find(key[m % len(key)])
        if (97 <= wordcode <= 122):
            if (97 <= wordcode - keycode <= 122):
                plaintext += chr(wordcode - keycode)
            else:
                plaintext += chr(wordcode - keycode + abc)

        elif (65 <= wordcode <= 90):
            if (65 <= wordcode - keycode <= 90):
                plaintext += chr(wordcode - keycode)
            else:
                plaintext += chr(wordcode - keycode + abc)
        else:
            plaintext += str(ciphertext[m])
    return plaintext