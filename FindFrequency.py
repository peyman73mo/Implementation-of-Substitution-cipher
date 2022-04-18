import numpy as np
import itertools
import string

def find_frequency(text):
    text = ''.join(text)
    freq =[]
    
    ch = [''.join(i) for i in itertools.product(string.ascii_uppercase,repeat=2)]
    for i in ch:
        freq.append(text.count(i))
        
    freq = np.array(freq)
    freq = freq.reshape(26*26)/freq.reshape(26*26).sum()
    freq = freq.reshape(26,26)
    return freq