
def enc(plain_text,key):
    cipher_text=[]
    for i in plain_text:    
        cipher_text.append(chr(key[ord(i)-65]))
    return cipher_text,key