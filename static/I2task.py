import hashlib

target = '482c811da5d5b4bc6d497ffa98491e38'

with open('file/path/to/passwords.txt', 'r') as file:
    for password in file:
        password = password.strip()
        hashedPass = hashlib.md5(password.encode()).hexdigest()
        if hashedPass == target:
            print(f'Found the password: {password}')
            break

    
