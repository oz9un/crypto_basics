def padding (plaintext, block_length):
    lack_bytes = (block_length - (len(plaintext)) % block_length)
    if lack_bytes == 0:
        lack_bytes = block_length
    padding = (chr(lack_bytes) * lack_bytes).encode()
    return plaintext + padding

def main():
    plaintext = b'YELLOW SUBMARINE'
    new_plaintext = padding(plaintext, 16)
    print(new_plaintext)
    print(len(new_plaintext))

