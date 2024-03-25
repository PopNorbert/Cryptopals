import binascii


def all(string):
    string = bytes.fromhex(string)
    for i in range(256):
        comp = bytes([i])*len(string)
        text = bytes([a ^ b for a, b in zip(string, comp)])

        print(text.decode())


print(all("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")) 