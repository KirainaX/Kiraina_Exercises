from itertools import groupby

def compress_string(s):
    compressed = [(len(list(group)), int(key)) for key, group in groupby(s)]
    result = ' '.join(f'({count}, {char})' for count, char in compressed)
    return result

# Sample Input
input_str = input()

# Call the function with the input
output_str = compress_string(input_str)

# Print the result
print(output_str)
