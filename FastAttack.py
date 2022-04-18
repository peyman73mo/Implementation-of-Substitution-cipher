import numpy as np

def d_score(a,b):
    return np.abs(a - b).sum()
# =========================================================================           
def swap_dimensions(x,i,j):
    x[:,[i,j]] = x[:,[j,i]]
    x[[i,j],:] = x[[j,i],:]
    return x
# =========================================================================
def fast_attack(s,guess,key):  
    score = d_score(s,guess)
    for _ in range(10):
        for i in range(1,26):
            for j in range(0,26-i):
                temp = swap_dimensions(np.copy(guess),j,j+i)
                if d_score(s,temp) < score:
                    guess = temp
                    score = d_score(s,temp)
                    key[j],key[j+i] = key[j+i],key[j]
    return key