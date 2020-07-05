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
KEY = 3

# Encryption function
def caeser_encrypt(plain_text):
    
    #the encrpted message
    cipher_text = ''
    # make the text case insensitive
    plain_text = plain_text.upper()
    
    #consider all the letters
    for c in plain_text:
        # find the index
        index = ALPHABET.find(c)
        # Add the Private key
        index = (index+KEY)%len(ALPHABET)
        # Append the cypher character by character
        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text
    
# Decryption function    
def caeser_decrypt(cipher_text):
    
    #the encrpted message
    plain_text = ''
        
    #consider all the letters
    for c in cipher_text:
        # find the index
        index = ALPHABET.find(c)
        # remove the key
        index = (index-KEY)%len(ALPHABET)
        # Append character by character
        plain_text = plain_text + ALPHABET[index]

    return plain_text
    
if __name__ == "__main__":
    encrypted = caeser_encrypt("Hello Arjun")
    print(encrypted)
    decrypted = caeser_decrypt(encrypted)
    print(decrypted)
    
    