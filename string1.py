def replace_alphabet(input_str, n):
    result = ''
    
    for char in input_str:
        if char.isalpha():
            # Determine whether it's an uppercase or lowercase letter
            is_upper = char.isupper()
            # Convert the letter to its ASCII code
            char_code = ord(char.lower())
            # Calculate the new ASCII code with the offset
            new_char_code = (char_code - ord('a') + n) % 26 + ord('a')
            # Convert the new ASCII code back to a character and adjust the case
            new_char = chr(new_char_code).upper() if is_upper else chr(new_char_code)
            result += new_char
        else:
            # If the character is not an alphabet letter, keep it unchanged
            result += char

    return result

# Example usage
input_string = "Hello, World!"
shift_value = 3
output_string = replace_alphabet(input_string, shift_value)
print(output_string)
