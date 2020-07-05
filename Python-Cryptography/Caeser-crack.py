# 
#   A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
#   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
#
#   Private Key =3 i.e n in the formulae
#   Plain text = THIS IS AN EXAMPLE
#   CIPHER TEXT = WKLV LV DQ HADPS
#   En(X) = (X+n) MOD 26
#


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caeser_crack(cipher_text):

    for key in range(len(ALPHABET)):
    
        plain_text = ''
        
        for c in cipher_text:        
            # find the index
            index = ALPHABET.find(c)
            # Add the Private key
            index = (index-key)%len(ALPHABET)
            # Append the cypher character by character
            plain_text = plain_text + ALPHABET[index]        
           
        print('With key %s, the result is: %s'%(key,plain_text))
           
if __name__ == "__main__":
    encrypted = 'KHOORCDUMXQ'    
    caeser_crack(encrypted)
    