def is_palindrome(input_string):
    
    input_string = input_string.replace(" ", "").lower()


    return input_string == input_string[::-1]


input_string = "bob"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')


