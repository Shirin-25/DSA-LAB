def find_largest_word(input_string):
    
    words = input_string.split()

    
    largest_word = max(words, key=len)

    return largest_word


input_string = "Find the largest word in this string"
largest_word = find_largest_word(input_string)
print("Largest word:", largest_word)
