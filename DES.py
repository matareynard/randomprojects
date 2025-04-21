def permute(input_bits, permutation_table):
    zero_based_table = [i - 1 for i in permutation_table]
    max_index = len(input_bits) - 1
    for i in zero_based_table:
        if i < 0 or i > max_index:
            raise ValueError(f"Index {i + 1} in permutation table is out of range for input length {len(input_bits)}.")
    
    return ''.join(input_bits[i] for i in zero_based_table)

def left_shift(bits, shifts):
    return bits[shifts:] + bits[:shifts]

def xor(bits1, bits2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

def sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)  # Row from first and last bits
    col = int(bits[1] + bits[2], 2)  # Column from second and third bits
    return format(sbox[row][col], '02b')

def generate_keys(key, P10, P8):
    if len(key) != 10:
        raise ValueError("The key must be 10 bits long.")
    
    key = permute(key, P10)
    print("Key after P10:", key)
    
    left, right = key[:5], key[5:]
    left, right = left_shift(left, 1), left_shift(right, 1)
    round_key1 = permute(left + right, P8)
    print("Round Key 1 (K1) after P8:", round_key1)
    
    left, right = left_shift(left, 2), left_shift(right, 2)
    round_key2 = permute(left + right, P8)
    print("Round Key 2 (K2) after P8:", round_key2)
    
    return round_key1, round_key2

def fk(bits, subkey, EP, P4, S0, S1):
    left, right = bits[:4], bits[4:]
    right_expanded = permute(right, EP)
    print("Right half after EP:", right_expanded)
    
    xor_result = xor(right_expanded, subkey)
    print("XOR result with subkey:", xor_result)
    
    left_sbox = sbox(xor_result[:4], S0)
    right_sbox = sbox(xor_result[4:], S1)
    print("S-box outputs: Left S-box:", left_sbox, "Right S-box:", right_sbox)
    
    # Combine S-box outputs to form 4 bits
    combined_sbox_output = left_sbox + right_sbox
    print("Combined S-box output (4 bits):", combined_sbox_output)
    
    sbox_output = permute(combined_sbox_output, P4)  # Apply P4
    print("S-box output after P4:", sbox_output)
    
    result = xor(left, sbox_output)
    resultXOR = xor(result,combined_sbox_output)
    print("Result after XOR with left half:", resultXOR)
    
    return resultXOR + right  # Combine the left and right parts

def sdes_encrypt(plaintext, key, IP, P10, P8, EP, P4, S0, S1):
    round_key1, round_key2 = generate_keys(key, P10, P8)
    
    plaintext = permute(plaintext, IP)
    print("After Initial Permutation (IP):", plaintext)
    
    temp = fk(plaintext, round_key1, EP, P4, S0, S1)
    print("After Round 1 (fk with round_key1):", temp)
    
    temp = temp[4:] + temp[:4]
    print("After Switch (ROUND 1 RESULT):", temp)
    

    
    return temp

def input_permutation_table(name):
    return list(map(int, input(f"Enter {name} (e.g., 3,0,2,4,...): ").split(',')))

# Get user input for tables
P10 = input_permutation_table("P10")
P8 = input_permutation_table("P8")
IP = input_permutation_table("IP")
EP = input_permutation_table("EP")
P4 = input_permutation_table("P4")

# Define S-boxes with the correct indexing
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

# Get user input for key and plaintext
key = input("Enter a 10-bit key (e.g., 1010000010): ")
plaintext = input("Enter an 8-bit plaintext (e.g., 11010111): ")

# Ensure the key and plaintext are of correct length
if len(key) != 10 or len(plaintext) != 8:
    print("Invalid input lengths. Key must be 10 bits and plaintext must be 8 bits.")
else:
    # Encrypt plaintext
    ciphertext = sdes_encrypt(plaintext, key, IP, P10, P8, EP, P4, S0, S1)
    print("ROUND 1 RESULT: ", ciphertext)
