# 17/20: Bitwise shift

def bit_reverse(input_word):
    current_output = 0
    
    for i in range(len(input_word)):
        char = input_word[i]
        shift = 8 * i        
        current_output = current_output | (int(bin(ord(char)), 2) << shift)
#         print("{:<42}{}".format("Current char:", char))
#         print("{:<42}{}".format("Current char's binary representation:", bin(ord(char))))
#         print("{:<42}{}".format("Current output as binary representation:", bin(current_output)))
#         print("---")
    
#     print("\n##### AND NOW, BACKWARDS #####\n")
    
    loop_start_index = len(bin(ord(char)))
    out_word = char
    for i in range(loop_start_index, len(bin(current_output)), 8):
        out_word += chr(int(bin(current_output)[i:i+8], 2))
#         print("{:<50}{}".format("Current char's binary representation:", bin(current_output)[i:i+8]))
#         print("{:<50}{}".format("Current char's integer (base 10) representation:", int(bin(current_output)[i:i+8], 2)))
#         print("{:<50}'{}'".format("Current char as character:", chr(int(bin(current_output)[i:i+8], 2))))
#         print("---")
    return out_word

# ATTN please don't reverse any strings containing >8-bit chars :(
print(bit_reverse("¿hola, cómo estás?"))
