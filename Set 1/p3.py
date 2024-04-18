import pprint

def all(string):
    string = bytes.fromhex(string)
    for i in range(256):
        comp = bytes([i])*len(string)
        text = bytes_xor()

        pprint.pprint(text.decode())


all("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")