def  print_upper_words(words, must_start_with) :
    """For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!"""
    for word in words :
        for letter in must_start_with :
            if ( word[0] == letter ) :
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {'h', 'y'})