def bitwise_and(binary_str1, binary_str2):
    """Perform a bitwise AND operation on two binary strings, including the fractional part."""
    # Split the binary strings into whole and fractional parts
    if '.' in binary_str1:
        whole_part1, frac_part1 = binary_str1.split('.')
    else:
        whole_part1, frac_part1 = binary_str1, ''

    if '.' in binary_str2:
        whole_part2, frac_part2 = binary_str2.split('.')
    else:
        whole_part2, frac_part2 = binary_str2, ''

    # Ensure both whole parts have the same length by padding with leading zeros
    max_whole_length = max(len(whole_part1), len(whole_part2))
    whole_part1 = whole_part1.zfill(max_whole_length)
    whole_part2 = whole_part2.zfill(max_whole_length)

    # Perform bitwise AND on the whole part
    and_whole = ''.join('1' if bit1 == '1' and bit2 == '1' else '0'
                        for bit1, bit2 in zip(whole_part1, whole_part2))

    # Perform bitwise AND on the fractional part, padding to the same length
    max_frac_length = max(len(frac_part1), len(frac_part2))
    frac_part1 = frac_part1.ljust(max_frac_length, '0')
    frac_part2 = frac_part2.ljust(max_frac_length, '0')
    and_frac = ''.join('1' if bit1 == '1' and bit2 == '1' else '0'
                       for bit1, bit2 in zip(frac_part1, frac_part2))

    # Combine the whole and fractional parts
    return and_whole + ('.' + and_frac if and_frac else '')

def bitwise_or(binary_str1, binary_str2):
    """Perform a bitwise OR operation on two binary strings, including the fractional part."""
    # Split the binary strings into whole and fractional parts
    if '.' in binary_str1:
        whole_part1, frac_part1 = binary_str1.split('.')
    else:
        whole_part1, frac_part1 = binary_str1, ''

    if '.' in binary_str2:
        whole_part2, frac_part2 = binary_str2.split('.')
    else:
        whole_part2, frac_part2 = binary_str2, ''

    # Ensure both whole parts have the same length by padding with leading zeros
    max_whole_length = max(len(whole_part1), len(whole_part2))
    whole_part1 = whole_part1.zfill(max_whole_length)
    whole_part2 = whole_part2.zfill(max_whole_length)

    # Perform bitwise OR on the whole part
    or_whole = ''.join('1' if bit1 == '1' or bit2 == '1' else '0'
                       for bit1, bit2 in zip(whole_part1, whole_part2))

    # Perform bitwise OR on the fractional part, padding to the same length
    max_frac_length = max(len(frac_part1), len(frac_part2))
    frac_part1 = frac_part1.ljust(max_frac_length, '0')
    frac_part2 = frac_part2.ljust(max_frac_length, '0')
    or_frac = ''.join('1' if bit1 == '1' or bit2 == '1' else '0'
                      for bit1, bit2 in zip(frac_part1, frac_part2))

    # Combine the whole and fractional parts
    return or_whole + ('.' + or_frac if or_frac else '')

def bitwise_xor(binary_str1, binary_str2):
    """Perform a bitwise XOR operation on two binary strings, including the fractional part."""
    # Split the binary strings into whole and fractional parts
    if '.' in binary_str1:
        whole_part1, frac_part1 = binary_str1.split('.')
    else:
        whole_part1, frac_part1 = binary_str1, ''

    if '.' in binary_str2:
        whole_part2, frac_part2 = binary_str2.split('.')
    else:
        whole_part2, frac_part2 = binary_str2, ''

    # Ensure both whole parts have the same length by padding with leading zeros
    max_whole_length = max(len(whole_part1), len(whole_part2))
    whole_part1 = whole_part1.zfill(max_whole_length)
    whole_part2 = whole_part2.zfill(max_whole_length)

    # Perform bitwise XOR on the whole part
    xor_whole = ''.join('1' if bit1 != bit2 else '0'
                        for bit1, bit2 in zip(whole_part1, whole_part2))

    # Perform bitwise XOR on the fractional part, padding to the same length
    max_frac_length = max(len(frac_part1), len(frac_part2))
    frac_part1 = frac_part1.ljust(max_frac_length, '0')
    frac_part2 = frac_part2.ljust(max_frac_length, '0')
    xor_frac = ''.join('1' if bit1 != bit2 else '0'
                       for bit1, bit2 in zip(frac_part1, frac_part2))

    # Combine the whole and fractional parts
    return xor_whole + ('.' + xor_frac if xor_frac else '')

def bitwise_not(binary_str):
    """Perform a bitwise NOT operation on a binary string, flipping 1s to 0s and 0s to 1s."""
    # Split into whole and fractional parts if necessary
    if '.' in binary_str:
        whole_part, frac_part = binary_str.split('.')
    else:
        whole_part, frac_part = binary_str, ''

    # Flip each bit in the whole part
    flipped_whole = ''.join('1' if bit == '0' else '0' for bit in whole_part)
    
    # Flip each bit in the fractional part
    flipped_frac = ''.join('1' if bit == '0' else '0' for bit in frac_part)

    # Combine the flipped whole and fractional parts
    return flipped_whole + ('.' + flipped_frac if flipped_frac else '')

def bitwise_calculator(a, b=None, operation="AND"):
    if operation != "NOT" and b is None:
        return "Second operand is required for AND, OR, and XOR operations."

    # Perform the bitwise operation
    if operation == "AND":
        return bitwise_and(a, b)
    elif operation == "OR":
        return bitwise_or(a, b)
    elif operation == "XOR":
        return bitwise_xor(a, b)
    elif operation == "NOT":
        return bitwise_not(a)
    else:
        return "Invalid operation"

# Example usage
a = input("Enter the first binary number (e.g., 101.101): ")
operation = input("Enter the operation (AND, OR, XOR, NOT): ").strip().upper()
b = None
if operation != "NOT":
    b = input("Enter the second binary number (ex: 011.001): ")

# Display the result in binary format
print("Result:", bitwise_calculator(a, b, operation))
