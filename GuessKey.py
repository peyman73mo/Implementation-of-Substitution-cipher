from collections import Counter

def guess_key(alphabet,cipher_text,frequency):
    guess_key=[]
    ciphertxt_frequency = dict(Counter(cipher_text))
    d = sorted(ciphertxt_frequency.items(), key=lambda item: item[1])
    for i in d:
        guess_key.append(ord(i[0])) 
    guess_key = guess_key[::-1]
    
    
    for i in alphabet:
        if not i in guess_key:
            guess_key.append(i)
    gk = []        
    for i in range(26):
        for j in range(26):
            if alphabet[i] == frequency[j]:
                gk.append(guess_key[j])
    return gk