import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def XOR(bits1,bits2):
	xor_result = ""
	for index in range(len(bits1)):
		if bits1[index] == bits2[index]:
			xor_result += '0'
		else:
			xor_result += '1'
	return xor_result

def apply_PC1(pc1_table,keys_64bits):
 """ возвращает 56-битный ключ """
 keys_56bits = ""
 for index in pc1_table:
  keys_56bits += keys_64bits[index-1]
# Python list index start with 0
# so index -1 will cover the difference between the index
 return keys_56bits


PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
keys_64bits = "0001001100110100010101110111100110011011101111001101111111110001"
keys_56bits = apply_PC1(PC1,keys_64bits)
#Output: 11110000110011001010101011110101010101100110011110001111

def split_in_half(keys_56bits):
 """ Разделение 56-битного ключа на две равные половины """
 left_keys, right_keys = keys_56bits[:28],keys_56bits[28:]
 return left_keys, right_keys
left56 , right56 = split_in_half(keys_56bits)

def circular_left_shift(bits,numberofbits):
 """Этот метод будет циклически сдвигать заданную битовую строку в соответствии с количеством битов"""
 shiftedbits = bits[numberofbits:] + bits[:numberofbits]
 return shiftedbits

#Сжатие
def apply_PC2(pc2_table,keys_56bits):
 """ Это возьмет таблицу сжатия и объединит обе половины в качестве ввода и вернет 48-битную строку в качестве вывода"""
 keys_48bits = ""
 for index in pc2_table:
  keys_48bits += keys_56bits[index-1]
 return keys_48bits
PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2, 41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
subkey = apply_PC2(PC2,left56 + right56)

def generate_keys(key_64bits):
 round_keys = list()
 pc1_out = apply_PC1(PC1,key_64bits)
 L0,R0 = split_in_half(pc1_out)
 for roundnumber in range(16):
  newL = circular_left_shift(L0,round_shifts[roundnumber])
  newR = circular_left_shift(R0,round_shifts[roundnumber])
  roundkey = apply_PC2(PC2,newL+newR)
  round_keys.append(roundkey)
  L0 = newL
  R0 = newR
 return round_keys
round_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
key_64bits = "0001001100110100010101110111100110011011101111001101111111110001"
subkeys = generate_keys(key_64bits)

print(subkeys)



msg = input("Введите слово: ")

msg_binary = text_to_bits(msg)[1:]
print("Message in binary: ",msg_binary)
zeroinend = msg_binary.ljust(64, '0')
print("Расширение: ",zeroinend)


INITIAL_PERMUTATION_TABLE = ['58 ', '50 ', '42 ', '34 ', '26 ', '18 ', '10 ', '2',
							 '60 ', '52 ', '44 ', '36 ', '28 ', '20 ', '12 ', '4',
							 '62 ', '54 ', '46 ', '38 ', '30 ', '22 ', '14 ', '6',
							 '64 ', '56 ', '48 ', '40 ', '32 ', '24 ', '16 ', '8',
							 '57 ', '49 ', '41 ', '33 ', '25 ', '17 ', '9 ', '1',
							 '59 ', '51 ', '43 ', '35 ', '27 ', '19 ', '11 ', '3',
							 '61 ', '53 ', '45 ', '37 ', '29 ', '21 ', '13 ', '5',
							 '63 ', '55 ', '47 ', '39 ', '31 ', '23 ', '15 ', '7']

def apply_initial_p(P_TABLE, PLAINTEXT):
	permutated = ""
	for index in P_TABLE:
		permutated += PLAINTEXT[int(index)-1]
	return permutated

plaintext = zeroinend
## initial permutation
p_plaintext = apply_initial_p(INITIAL_PERMUTATION_TABLE,plaintext)
print("Initial Permutation: ", p_plaintext)

def Half(binarybits):
	return binarybits[:32],binarybits[32:]
####### Разделение на 32 : 32
L0,R0 = Half(p_plaintext)
print("Left:  ", L0)
print("Right: ",R0)

# Генерация раундовых ключей

roundkeys = generate_keys(key_64bits)

########################################## DES steps ##########################################

######## Rounds




