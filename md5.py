import hashlib

flag = 0

pass_hash = input("Enter md5 hash: ")

with open("md5.txt","r") as file:

    for word in file:

        enc_word = word.strip().encode('utf-8')

        digest = hashlib.md5(enc_word).hexdigest

        if digest == pass_hash:
            print("Password has been found!")
            print(f"The decrypted password for {pass_hash} is: {word.strip()}")
            flag = 1
            break

if flag == 0:
    print ("The password is not found.")


