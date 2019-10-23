# 1/20: Format Reverse

def format_reverse(input_string):
    output_string = "{}" * len(input_string)
    for i in range(len(input_string)):
        remaining_chars = ["{}" for j in range(
                            len(input_string) - i-1)]
        output_string = output_string.format(*remaining_chars, 
                                             input_string[i])
#         print(output_string) # UNCOMMENT FOR A FUN TIME!
    return output_string

print(format_reverse("a bad idea"))