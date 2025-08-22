def count_characters(input_string):
    uppercase_count = 0
    lowercase_count = 0
    special_count = 0
    
    
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif not char.isalnum():  
            special_count += 1
    
    
    print(f"Uppercase characters: {uppercase_count}")
    print(f"Lowercase characters: {lowercase_count}")
    print(f"Special characters: {special_count}")


input_string = input("Enter a string: ")
count_characters(input_string)
