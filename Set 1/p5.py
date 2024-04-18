def repeating_key_xor(text, key):
    encrypted = bytearray()
    for i in range(len(text)):
        encrypted.append(text[i] ^ key[i % len(key)])
    return encrypted

plaintext = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"

plaintext_bytes = bytearray(plaintext, 'utf-8')
key_bytes = bytearray(key, 'utf-8')

encrypted_bytes = repeating_key_xor(plaintext_bytes, key_bytes)

encrypted_hex = ''.join(format(byte, '02X') for byte in encrypted_bytes)


print(encrypted_hex)
print("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f".upper())
print(encrypted_hex == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f".upper())