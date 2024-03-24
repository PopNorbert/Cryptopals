def convert64(string):
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
        'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
    }
    bin = ""
    for ch in string:
        bin+=hex_to_bin[ch]
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    b64 = ""
    
    while len(bin)%6!=0:
        x = ""
        x+="00"
        x+=bin
        bin=x

    for i in range(0, len(bin), 6):
        chunk = bin[i:i+6]
        b = 0
        x = 5
        for c in chunk:
            if c=='1':
                b+=2**x
            x-=1
        b64+=base64_chars[b]
    return b64

print(convert64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))