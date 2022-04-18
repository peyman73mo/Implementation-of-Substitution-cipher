import string

def get_plain_text():
    plain_text = ''.join(input().translate(str.maketrans('', '', string.punctuation+'\n\t')).upper().split())
    for i in plain_text:
        if i in '‘’”“!"#$%&\'()*+,-—./:;<=>?@[\\]^_`{|}~0123456789éÉ':
            plain_text = plain_text.replace(i,'')
    for i in plain_text:
        if not i in string.ascii_letters:
            plain_text = plain_text.replace(i,'')

    plain_text = list(plain_text) 
    return plain_text