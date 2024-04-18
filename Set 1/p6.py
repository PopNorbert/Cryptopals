def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for char1, char2 in zip(str1, str2):
        distance += bin(ord(char1) ^ ord(char2)).count('1')
    
    return distance

string1 = "this is a test"
string2 = "wokka wokka!!!"

distance = hamming_distance(string1, string2)
print("Hamming distance:", distance)