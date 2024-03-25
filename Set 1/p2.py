def fixed_xor(s1, s2):
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
        'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
    }
    bin_to_hex = {}
    for key,value in hex_to_bin.items():
        bin_to_hex[value] = key
    res = ''
    for i in range(len(s1)):
        b1=hex_to_bin[s1[i]]
        b2=hex_to_bin[s2[i]]
        r = ''
        for j in range(4):
            if b1[j]!=b2[j]:
                r+='1'
            else:
                r+='0'
        res+=bin_to_hex[r]
    return res
                


print(fixed_xor("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965"))
