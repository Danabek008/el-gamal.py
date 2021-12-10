import binascii


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


msg = input("Введите слово: ")
k1 = 1
k2 = 2


left = msg[0:len(msg)//2]
right = msg[len(msg)//2
            if len(msg)%2 == 0
            else ((len(msg)//2)+1):]

left_binary = text_to_bits(left)[2:]
right_binary = text_to_bits(right)[2:]

print("Left Binary: ",left_binary)
print("Right Binary: ",right_binary)

sdvig1 = left_binary[k1:] + left_binary[:k1]

print("f={l,k}: ",sdvig1)

text = ""
itera = 0

for i in range(len(right_binary)):
    temp = int(right_binary[i]) ^ int(sdvig1[itera])
    text += str(temp)
    itera += 1
    if itera >= len(sdvig1):
        itera = 0
print("first XOR: ", text)

sdvig2 = right_binary[k2:] + right_binary[:k2]
print("Sdvig2: ",sdvig2)

textencr = ""
bitr = 0

for i in range(len(sdvig2)):
    temp = int(sdvig2[i]) ^ int(text[bitr])
    textencr += str(temp)
    bitr += 1
    if bitr >= len(text):
        bitr = 0
print("second XOR: ", textencr)

alltext_bin = str(text) + str(textencr)
print(alltext_bin)









