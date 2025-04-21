def binary_to_decimal(binary_str):
    if '.' in binary_str:
        integer_part, fractional_part = binary_str.split('.')
        decimal_integer = int(integer_part, 2)
        decimal_fraction = sum(int(bit) * (2 ** -i) for i, bit in enumerate(fractional_part, 1))
        return decimal_integer + decimal_fraction
    else:
        return int(binary_str, 2)
def octal_to_decimal(octal_str):
    if '.' in octal_str:
        integer_part, fractional_part = octal_str.split('.')
        decimal_integer = int(integer_part, 8)
        decimal_fraction = sum(int(digit) * (8 ** -i) for i, digit in enumerate(fractional_part, 1))
        return decimal_integer + decimal_fraction
    else:
        return int(octal_str, 8)

def hex_to_decimal(hex_str):
    if '.' in hex_str:
        integer_part, fractional_part = hex_str.split('.')
        decimal_integer = int(integer_part, 16)
        decimal_fraction = sum(int(digit, 16) * (16 ** -i) for i, digit in enumerate(fractional_part, 1))
        return decimal_integer + decimal_fraction
    else:
        return int(hex_str, 16)

def decimal_to_binary(decimal_num, min_integer_length=3, fractional_length=10):
    integer_part = int(decimal_num)
    fractional_part = decimal_num - integer_part

    # Convert integer part to binary and pad if necessary
    binary_integer = bin(integer_part)[2:]
    if len(binary_integer) < min_integer_length:
        binary_integer = binary_integer.zfill(min_integer_length)

    # Convert fractional part with adaptive precision until it's near zero or max length
    binary_fraction = []
    count = 0
    while fractional_part > 0 and count < fractional_length:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fraction.append(str(bit))
        fractional_part -= bit
        count += 1

    return binary_integer + '.' + ''.join(binary_fraction) if binary_fraction else binary_integer

def decimal_to_octal(decimal_num, input_length=None):
    integer_part = int(decimal_num)
    fractional_part = decimal_num - integer_part
    octal_integer = oct(integer_part)[2:]

    # Pad with leading zeros if needed
    if input_length:
        octal_integer = octal_integer.zfill(input_length)

    octal_fraction = []
    while fractional_part and len(octal_fraction) < 10:
        fractional_part *= 8
        digit = int(fractional_part)
        octal_fraction.append(str(digit))
        fractional_part -= digit

    return octal_integer + '.' + ''.join(octal_fraction) if octal_fraction else octal_integer

def decimal_to_hex(decimal_num, max_fraction_length=10):
    integer_part = int(decimal_num)
    fractional_part = decimal_num - integer_part
    hex_integer = hex(integer_part)[2:].upper()  
    
    hex_fraction = []
    while fractional_part and len(hex_fraction) < max_fraction_length:
        fractional_part *= 16
        digit = int(fractional_part)
        hex_fraction.append(hex(digit)[2:].upper())  
        fractional_part -= digit

    # Check if fractional part should be rounded
    if fractional_part > 0 and len(hex_fraction) == max_fraction_length:
        # Round last digit if needed
        last_digit = int(hex_fraction[-1], 16)
        if fractional_part * 16 >= 8:
            last_digit += 1
            if last_digit == 16:  # Handle overflow if last digit is F + 1
                last_digit = 0
                for i in range(len(hex_fraction) - 1, -1, -1):
                    if hex_fraction[i] == 'F':
                        hex_fraction[i] = '0'
                    else:
                        hex_fraction[i] = hex(int(hex_fraction[i], 16) + 1)[2:].upper()
                        break
                else:
                    hex_integer = hex(int(hex_integer, 16) + 1)[2:].upper()
            else:
                hex_fraction[-1] = hex(last_digit)[2:].upper()

    return hex_integer + '.' + ''.join(hex_fraction) if hex_fraction else hex_integer



# Modify the operation functions to pass input length for padding
def add_numbers(num1, num2, base):
    if base == 'binary':
        # Convert binary inputs to decimal, perform addition
        decimal_result = binary_to_decimal(num1) + binary_to_decimal(num2)
        integer_length = max(len(num1.split('.')[0]), len(num2.split('.')[0]))
        # Increase fractional length for more precision
        return decimal_to_binary(decimal_result, integer_length, fractional_length=5)
    elif base == 'octal':
        decimal_result = octal_to_decimal(num1) + octal_to_decimal(num2)
        integer_length = max(len(num1.split('.')[0]), len(num2.split('.')[0]))
        return decimal_to_octal(decimal_result, integer_length)
    elif base == 'decimal':
        return str(float(num1) + float(num2))
    elif base == 'hexadecimal':
        decimal_result = hex_to_decimal(num1) + hex_to_decimal(num2)
        return decimal_to_hex(decimal_result)

def subtract_numbers(num1, num2, base):
    if base == 'binary':
        decimal_result = binary_to_decimal(num1) - binary_to_decimal(num2)
        integer_length = max(len(num1.split('.')[0]), len(num2.split('.')[0]))
        return decimal_to_binary(decimal_result, integer_length)
    elif base == 'octal':
        decimal_result = octal_to_decimal(num1) - octal_to_decimal(num2)
        integer_length = max(len(num1.split('.')[0]), len(num2.split('.')[0]))
        return decimal_to_octal(decimal_result, integer_length)
    elif base == 'decimal':
        return str(float(num1) - float(num2))
    elif base == 'hexadecimal':
        decimal_result = hex_to_decimal(num1) - hex_to_decimal(num2)
        return decimal_to_hex(decimal_result)
def multiply_numbers(num1, num2, base):
    if base == 'binary':
        # Convert binary inputs to decimal, perform multiplication
        decimal_result = binary_to_decimal(num1) * binary_to_decimal(num2)
        # Use a larger fractional length for more precision
        return decimal_to_binary(decimal_result, fractional_length=16)
    elif base == 'octal':
        decimal_result = octal_to_decimal(num1) * octal_to_decimal(num2)
        return decimal_to_octal(decimal_result)
    elif base == 'decimal':
        return str(float(num1) * float(num2))
    elif base == 'hexadecimal':
        decimal_result = hex_to_decimal(num1) * hex_to_decimal(num2)
        return decimal_to_hex(decimal_result)

def divide_numbers(num1, num2, base):
    if base == 'binary':
        decimal_result = binary_to_decimal(num1) / binary_to_decimal(num2)
        min_integer_length = max(3, len(bin(int(decimal_result))[2:]))
        return decimal_to_binary(decimal_result, min_integer_length=min_integer_length, fractional_length=4)
    elif base == 'octal':
        decimal_result = octal_to_decimal(num1) / octal_to_decimal(num2)
        return decimal_to_octal(decimal_result)
    elif base == 'decimal':
        return str(float(num1) / float(num2))
    elif base == 'hexadecimal':
        # Convert hexadecimal inputs to decimal and perform division
        try:
            decimal_result = hex_to_decimal(num1) / hex_to_decimal(num2)
            return decimal_to_hex(decimal_result)  # Convert back to hexadecimal
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None
def align_decimal_point(num_str):
    if num_str is None:
        return '', ''  # Return empty strings if num_str is None to avoid errors
    if '.' in num_str:
        integer_part, fractional_part = num_str.split('.')
    else:
        integer_part, fractional_part = num_str, ''
    return integer_part, fractional_part

def format_result(num_str):
    integer_part, fractional_part = align_decimal_point(num_str)
    return f"{integer_part}.{fractional_part}" if fractional_part else integer_part

def main():
    print("Choose the number system (binary, octal, decimal, hexadecimal): ")
    base = input().strip().lower()
    if base not in ['binary', 'octal', 'decimal', 'hexadecimal']:
        print("Invalid base. Please choose binary, octal, decimal, or hexadecimal.")
        return

    print(f"Enter the first number in {base}: ")
    num1 = input().strip()
    print(f"Enter the second number in {base}: ")
    num2 = input().strip()

    print("Choose the operation (add, subtract, multiply, divide): ")
    operation = input().strip().lower()

    if operation == 'add':
        result = add_numbers(num1, num2, base)
    elif operation == 'subtract':
        result = subtract_numbers(num1, num2, base)
    elif operation == 'multiply':
        result = multiply_numbers(num1, num2, base)
    elif operation == 'divide':
        if num2 == '0' or num2 == '0.0':
            print("Error: Division by zero is not allowed.")
            return
        result = divide_numbers(num1, num2, base)
    else:
        print("Invalid operation. Please choose add, subtract, multiply, or divide.")
        return

    # Format and align the result based on the decimal point
    formatted_result = format_result(result)
    print(f"The result of {operation} in {base} is: {formatted_result}")

if __name__ == "__main__":
    main()
