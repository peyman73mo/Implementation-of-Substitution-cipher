
def dec(key,cipher_text):
    dec_p=[]
    for i in [ord(_) for _ in cipher_text]:
        for j in range(26):
            if i == key[j]:
                dec_p.append(j+65)
    return [chr(_) for _ in dec_p]