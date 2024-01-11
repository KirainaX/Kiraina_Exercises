from itertools import combinations_with_replacement

def replacement_combinations(s, k):
    # Generate all possible combinations with replacements
    combinations = combinations_with_replacement(sorted(s), k)
    
    # Print the combinations
    for combo in combinations:
        print(''.join(combo))

# Sample Input
input_str, replacement_size = input(": ").split()
replacement_size = int(replacement_size)

# Call the function with the input
replacement_combinations(input_str, replacement_size)
