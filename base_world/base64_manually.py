ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
base64_alphabet = ascii_uppercase + ascii_lowercase + digits + '+/'

to_encode = input("base64 encoder ->  ")

chunks_8bit = ''.join([format(bits,'08b') for bits in to_encode.encode('utf8')])

chunks_6bit = [chunks_8bit[bits:bits+6] for bits in range(0,len(chunks_8bit),6)]
padding_amount = ( 6 - len(chunks_6bit[len(chunks_6bit)-1]) )
chunks_6bit[len(chunks_6bit)-1] += padding_amount * '0'


encoded = ''.join([base64_alphabet[int(bits,2)] for bits in chunks_6bit])
encoded += int(padding_amount/2) * '='
print('Base64 encoded version of {to_encode} is: {result}'.format(to_encode = to_encode, result = encoded))