from collections import Counter

def character_frequency(input_string):
    # Using Counter to count frequency of each character
    freq = Counter(input_string)
    
    # Printing the frequency of each character
    for char, count in freq.items():
        print(f"Character: {char} -> Frequency: {count}")

# Example usage
input_string = input("Enter a string: ")
character_frequency(input_string)