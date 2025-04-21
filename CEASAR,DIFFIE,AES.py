import numpy as np
s_box = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0x9a, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]

# AES Mix Columns matrix
mix_columns_matrix = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

# Helper function to perform finite field multiplication
def g_mul(a, b):
    p = 0
    while b:
        if b & 1:
            p ^= a
        a = (a << 1) ^ (0x1b if a & 0x80 else 0)  # reduce modulo 0x1b if a >= 128
        b >>= 1
    return p


# Add Round Key
def add_round_key(state, key):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= key[i][j]
            if state[i][j] < 0 or state[i][j] > 255:
                raise ValueError(f"Byte value {state[i][j]} at state[{i}][{j}] is out of range after AddRoundKey.")



# Sub-Bytes using S-box
def sub_bytes(state):
    for i in range(4):
        for j in range(4):
            byte = state[i][j]
            if byte < 0 or byte > 255:
                raise ValueError(f"Byte value {byte} at state[{i}][{j}] is out of range.")
            state[i][j] = s_box[byte >> 4][byte & 0x0F]  # Row = high nibble, Column = low nibble

# Shift Rows
def shift_rows(state):
    state[1] = np.roll(state[1], -1)  # Row 2 (1 left shift)
    state[2] = np.roll(state[2], -2)  # Row 3 (2 left shifts)
    state[3] = np.roll(state[3], -3)  # Row 4 (3 left shifts)

# Mix Columns
def mix_columns(state):
    temp = np.zeros((4, 4), dtype=int)
    for c in range(4):
        for r in range(4):
            temp[r][c] = (
                g_mul(mix_columns_matrix[r][0], state[0][c]) ^
                g_mul(mix_columns_matrix[r][1], state[1][c]) ^
                g_mul(mix_columns_matrix[r][2], state[2][c]) ^
                g_mul(mix_columns_matrix[r][3], state[3][c])
            ) % 256  # Ensure result stays within byte range
    for i in range(4):
        for j in range(4):
            state[i][j] = temp[i][j]

# Function to print state matrix
def print_state(state):
    for i in range(4):
        for j in range(4):
            print(f"{state[i][j]:02x}", end=" ")
        print()


# Function to convert a 16-byte hex string into a 4x4 matrix
def hex_string_to_matrix(hex_str):
    if len(hex_str) != 32:
        raise ValueError("Hex string must be 32 characters long (16 bytes).")

    matrix = np.zeros((4, 4), dtype=int)
    for i in range(16):
        byte = int(hex_str[i * 2:i * 2 + 2], 16)
        if byte < 0 or byte > 255:
            raise ValueError(f"Byte value {byte} from hex string is out of range.")
        row = i % 4
        col = i // 4
        matrix[row][col] = byte
    return matrix

# Function to convert a 4x4 matrix back into a hex string
def matrix_to_hex_string(matrix):
    hex_str = ""
    for i in range(4):
        for j in range(4):
            hex_str += f"{matrix[i][j]:02x}"
    return hex_str


# AES encryption function
def aes_encrypt(plaintext_hex, key_hex):
    # Convert hex strings to state and key matrices
    state = hex_string_to_matrix(plaintext_hex)
    key = hex_string_to_matrix(key_hex)

    print("\n=== Initial State ===")
    print_state(state)

    # Initial AddRoundKey
    add_round_key(state, key)

    print("\n=== AddRoundKey ===")
    print_state(state)

    # 9 rounds of encryption
    for round in range(1):
        print(f"\nRound {round + 1}:")
        sub_bytes(state)
        print("\n=== SubBytes ===")
        print_state(state)

        shift_rows(state)
        print("\n=== ShiftRows ===")
        print_state(state)

        if round != 9:  # MixColumns is not performed in the last round
            mix_columns(state)
            print("\n=== MixColumns ===")
            print_state(state)

        # Key schedule for the next round key (for simplicity, using same key here)
        add_round_key(state, key)
        print("\nAfter AddRoundKey:")
        print_state(state)

    # Final round (no MixColumns)
    sub_bytes(state)
    print("\nAfter Final SubBytes:")
    print_state(state)
    
    shift_rows(state)
    print("\nAfter Final ShiftRows:")
    print_state(state)
    
    add_round_key(state, key)
    print("\nAfter Final AddRoundKey:")
    print_state(state)
    
    # Convert final state to hex string
    ciphertext_hex = matrix_to_hex_string(state)
    return ciphertext_hex

# DES functions
def permute(input_str, permutation):
    return ''.join(input_str[i - 1] for i in permutation)

def left_shift(input_str, shifts):
    # Split the input string into two halves
    left_half = input_str[:5]
    right_half = input_str[5:]
    # Left shift both halves
    left_half_shifted = left_half[shifts:] + left_half[:shifts]
    right_half_shifted = right_half[shifts:] + right_half[:shifts]
    # Return the concatenated result
    return left_half_shifted + right_half_shifted

def xor_strings(a, b):
    return ''.join('1' if a[i] != b[i] else '0' for i in range(len(a)))

def s_box_lookup(input_str, s_box):
    row = (int(input_str[0]) * 2) + int(input_str[3])
    col = (int(input_str[1]) * 2) + int(input_str[2])
    return bin(s_box[row][col])[2:].zfill(2)

def to_hex(binary_str):
    decimal = int(binary_str, 2)
    return hex(decimal)[2:].upper()

# Constants for DES
P10 = [5, 3, 8, 9, 10, 1, 2, 4, 7, 6]
P8 = [4, 5, 2, 1, 6, 7, 8, 3]
EP = [4, 3, 2, 1, 4, 2, 1, 3]
IP = [2, 3, 5, 6, 7, 1, 4, 8]
P4 = [2, 3, 1, 1]

# S-Boxes
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [2, 1, 3, 0]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

# Caesar cipher functions
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, 26 - shift)

# Modular exponentiation function
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Extended Euclidean algorithm for modular inverse
def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Function to find the modular inverse
def mod_inverse(a, m):
    gcd, x, _ = gcd_extended(a, m)
    if gcd != 1:
        print("\nInverse doesn't exist")
        return None
    return x % m

def des_encryption():
    key = input("\nEnter a 10-bit key (10 bits): ")
    plaintext = input("Enter an 8-bit plaintext (8 bits): ")

    # Step 1: Print the given K
    print("\nGiven K:", key)

    # Step 2: Permute the key with P10
    permuted_key = permute(key, P10)
    print("P10:", permuted_key)

    # Step 3: Left shift the permuted key once
    ls1 = left_shift(permuted_key, 1)
    print("LS1 (Left Shift 1):", ls1)

    # Step 4: Generate Key 1
    key1 = permute(ls1, P8)
    print("Key 1 (P8):", key1)

    # Step 5: Left shift the permuted key twice for Key 2
    ls2 = left_shift(ls1, 2)
    print("LS2 (Left Shift 2):", ls2)

    # Step 6: Generate Key 2
    key2 = permute(ls2, P8)
    print("Key 2 (P8):", key2)

    # Step 7: Print the given PT
    print("\nGiven PT:", plaintext)

    # Step 8: Permute the plaintext with IP
    ip = permute(plaintext, IP)
    print("IP:", ip)
    left = ip[:4]
    right = ip[4:]

    # Round 1
    ep = permute(right, EP)
    print("EP:", ep)

    xor1 = xor_strings(ep, key1)
    print("XOR (EP and Key 1):", xor1)

    # Divide into two parts for S-Box lookup
    s0_input = xor1[:4]
    s1_input = xor1[4:]
    s0_output = s_box_lookup(s0_input, S0)
    s1_output = s_box_lookup(s1_input, S1)

    # Step 5: Print S0 and S1 values
    print("S0:", s0_input, "->", s0_output)
    print("S1:", s1_input, "->", s1_output)

    # Step 6: Combine S0 and S1 and permute with P4
    s0s1 = s0_output + s1_output
    print("S0S1:", s0s1)

    p4 = permute(s0s1, P4)
    print("P4:", p4)

    # Step 9: XOR with left part of IP
    xor2 = xor_strings(p4, left)
    print("XOR (P4 - s0s1 - left(IP)):", xor2)

    # Step 10: Combine results
    new_right = xor2 + right
    print("XOR + Right of IP: ", xor2 + right)

    # Step 11: Swap halves
    new_ip = new_right[4:] + new_right[:4]
    print("Swapped Result:", new_ip)

    # Convert final output to hex
    ciphertext = to_hex(new_ip)
    print("Ciphertext in hexadecimal:", ciphertext)

def main():
    while True:
        print("\nChoose an operation:")
        print("1. Caesar Cipher")
        print("2. Diffie-Hellman Key Exchange")
        print("3. RSA Encryption/Decryption")
        print("4. AES Encryption\n")
        main_choice = input("> ")

        if main_choice == '1':
            # Caesar Cipher
            choice = input("\nDo you want to (e)enc4rypt or (d)decrypt? ").lower()
            text = input("\nEnter text: ")
            shift = int(input("\nEnter shift value: "))

            if choice == 'e':
                encrypted_text = encrypt(text, shift)
                print("\nEncrypted text:", encrypted_text)
            elif choice == 'd':
                decrypted_text = decrypt(text, shift)
                print("\nDecrypted text:", decrypted_text)
            else:
                print("\nInvalid choice!")

        elif main_choice == '2':
            # Diffie-Hellman Key Exchange
            q = int(input("\nEnter a prime number (q): "))
            g = int(input("Enter a primitive root (g): "))
            a = int(input("Enter Secret key (a): "))
            b = int(input("Enter Secret key (b): "))

            # Calculate public keys
            a_public = mod_exp(g, a, q)
            b_public = mod_exp(g, b, q)

            print("\nPublic key (A):", a_public)
            print("Public key (B):", b_public)

            # Calculate shared secret using the other party's public key
            shared_secret_a = mod_exp(b_public, a, q)  # b_public^a mod q
            shared_secret_b = mod_exp(a_public, b, q)  # a_public^b mod q

            print("Shared secret computed by (A):", shared_secret_a)
            print("Shared secret computed by (B):", shared_secret_b)

            # Check if the shared secrets match
            if shared_secret_a == shared_secret_b:
                print("\nThe shared secrets match:", shared_secret_a)
            else:
                print("\nThe shared secrets do not match!")

        elif main_choice == '3': # RSA Encryption/Decryption
            p = int(input("\nEnter the first prime number (P): "))

            q = int(input("Enter the second prime number (Q): "))

            e = int(input("Enter public key (E): "))

            m = int(input("Enter plaintext (M): "))

            # Calculate n and phi(n)
            n = p * q
            phi_n = (p - 1) * (q - 1)

            print("\nCalculating n and phi(n):")

            print("n = P * Q =", n)

            print("phi(n) = (P - 1) * (Q - 1) =", phi_n)

            # Encrypt the plaintext
            c = mod_exp(m, e, n)
            print("\nCiphertext (C):", c)

            # Decrypt the ciphertext
            d = mod_inverse(e, phi_n)
            if d is not None:
                print("\nModular Inverse (d):", d)

                decrypted_m = mod_exp(c, d, n)

                print("Decrypted Plaintext (M):", decrypted_m)

        elif main_choice == '5':
            des_encryption()

        elif main_choice == '4':
            plaintext = input("\nEnter plaintext (16 bytes in hex): ")
            key = input("Enter key (16 bytes in hex): ")
            ciphertext = aes_encrypt(plaintext, key)
            print(f"\nCiphertext: {ciphertext}")

        else:
            print("\nInvalid choice!")

        continue_choice = input("\nDo you want to continue (y/n)? ").lower()
        if continue_choice != 'y':
            break

if __name__ == "__main__":
    main()