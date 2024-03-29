ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
base64_alphabet = ascii_uppercase + ascii_lowercase + digits + '+/'

to_encode  = input('Enter the Hex string : ')
hex_string= to_encode.encode('utf-8').hex()
bit_string = (((6 - len(bin(int(hex_string[0])))) * '0') + bin(int(hex_string,16))[2:])
 
#This math operation to provide its length be multiple of 4 .
bits6_rep = [bit_string[bits:bits+6] for bits in range(0,len(bit_string),6)]

if len(bits6_rep[len(bits6_rep)-1]) != 6:
    bits6_rep[len(bits6_rep)-1] = bits6_rep[len(bits6_rep)-1] + ((6 - len(bits6_rep[len(bits6_rep)-1])) * '0')

encoded = ''.join([base64_alphabet[int(bits,2)] for bits in bits6_rep])

print(encoded)

''' Easy way, with imports using base64 library.
import base64
hex2string = bytes.fromhex(hex_string)
encoded_string = base64.b64encode(hex2string)
print(encoded_string.decode('utf8'))

Easy way, with imports using codec library.
import codecs
encoded_string = codecs.encode(codecs.decode(hex_string, 'hex'), 'base64')
print(encoded_string.decode('utf8'))

'''
