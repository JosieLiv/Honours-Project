encrypted = 'pbbxvrqbhtu'
# shift for each character in the alphabet
for i in range(1, 26):
    password = ''
    for character in encrypted:
        if character.isalpha():
            shifted = ord(character) - i
            # if character is a, shift it back to z
            if shifted < ord('a'):
                shifted += 26
            password += chr(shifted)
        else:
            password += character
    print(f'The decrypted password is {password}')
