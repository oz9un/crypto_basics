from Crypto.Cipher import AES 

def padding_check(plaintext, blocksize):
    if type(plaintext) == bytes:
        plaintext = plaintext.decode()
    count = 0
    if ord(plaintext[len(plaintext)-1]) <= blocksize:
        pad_byte = ord(plaintext[len(plaintext)-1])
    else:
        return False

    if (len(plaintext) % blocksize) == 0:
        for i in range(len(plaintext)-1, -1, -1):
            count += 1
            if ord(plaintext[i]) != pad_byte and count < pad_byte:
                raise Exception('Wrong padding: Different padding bytes')
            elif ord(plaintext[i]) != pad_byte and count >= pad_byte:
                count -= 1
                break
        
        if count == pad_byte:
            return True
        else:
            raise Exception('Wrong padding: Wrong padding byte!')
    
    else:
        raise Exception('Wrong padding: Unsufficient bytes')



def control(plaintext, blocksize):
    #padding_check('YELLOW SUBMARINE\x04\x04\x04\x04',20)
    #padding_check("ICE ICE BABY\x01\x02\x03\x04",16)
    try:
        check = padding_check(plaintext, blocksize)
        if check == True:
            return True
        elif check == False:
            return False
    except:
        return False

#print(control('\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10',16))
#print(control('yellow submarine\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10',16))
#print(control('000002Quick to the point, to the point, no fakin',16))
#print(control('000002Quick to the point, to the point, no faking\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f',16))