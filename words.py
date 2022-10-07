def print_upper_words(words):
    """This prints each word uppercased on a seperate line"""
    
    for word in words:
        print(word.upper())
        
def print_upper_words_v2(words):
    """This prints words with the letter e in them uppercased on a seperate line"""
    
    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper())


def print_upper_words_v3(words, must_start_with):
    """Prints words that start with the chosen letter of the user"""
    
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
            
        