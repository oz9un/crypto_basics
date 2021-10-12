hex_string = "1a"
scale = 16
num_of_bits = 8
result = bin(int(hex_string, scale))[2:].zfill(num_of_bits)

# example hex values:
hex_1 = "CAFEBABE"
hex_2 = "0A0A0A0A"

bin_1 = bin(int(hex_1, 16))[2:] # OUTPUT = "11001010111111101011101010111110"
bin_2 = bin(int(hex_2, 16))[2:] # OUTPUT = "1010000010100000101000001010"

# find out length of the longer binary:
desired_length = len(bin_1) if len(bin_1) > len(bin_2) else len(bin_2)

# use zfill() to make equal lengths:
bin_1 = bin_1.zfill(desired_length) # OUTPUT = "11001010111111101011101010111110"
bin_2 = bin_2.zfill(desired_length) # OUTPUT = "00001010000010100000101000001010"




bin_1 = "11001010111111101011101010111110"
bin_2 = "00001010000010100000101000001010"

result = [int(bit1) ^ int(bit2) for bit1,bit2 in zip(bin_1,bin_2)]


string_result = "".join([str(bits) for bits in result])

a = hex(int(string_result,2))[2:]


 # FINAL OUTPUT = c0f4b0b4


# CRYPTOPALS SET 1 CHALLENGE 2 : FIXED XOR

hex_value1 = "1c0111001f010100061a024b53535009181c"
hex_value2 = "686974207468652062756c6c277320657965"

#step 1-2
bin_value1 = bin(int(hex_value1, 16))[2:]
bin_value2 = bin(int(hex_value2, 16))[2:]

#step 3
desired_length = len(bin_value1) if len(bin_value1) > len(bin_value2) else len(bin_value2)

bin_value1 = bin_value1.zfill(desired_length)
bin_value2 = bin_value2.zfill(desired_length)

#step 4
result = [int(bit1) ^ int(bit2) for bit1,bit2 in zip(bin_value1,bin_value2)]
string_result = "".join([str(bits) for bits in result])

#step 5
final_output = hex(int(string_result, 2))[2:]

bin(0)  # OUTPUT = 0b0
bin(15) # OUTPUT = 0b1111
