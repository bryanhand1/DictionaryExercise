### This is exercise 1 from the Dictionary Exercise Assignment
###Using the text.txt file we need to state how many times a word is ued

# Need to take txt file and strip punct, return as string and split string into words
# Define strip punct function.
undesired_punc = ["'", '"', ",", ".", "!", ":", ";", "#", "@", "?"]


def strip_punct(string, undesired_punc):

    # Next create a loop to check for punctation and remove it
    for x in undesired_punc:
        if x in string:
            string = string.replace(x, "")
    # Now I'll make all letters lowercase
    string = string.lower()
    # This prints the new string
    print(string)
    # Returns the string to the code that called it
    return string


# Read file and make it a string

text_file = open("text.txt", "r")

text_str = ""

for i in text_file:
    text_str += i

### Strip punct from string and make it lower case

text_str = strip_punct(string=text_str, undesired_punc=undesired_punc)


# Start dictionary and word count
# Everything below is from pg 218 of Intro To Python for computer science and data science
word_counts = {}

for word in text_str.split():
    if word in word_counts:
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # creates new key-value pair

print(f'{"WORD": <12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f"{word:<12}{count}")

print("\nNumber of unique words: ", len(word_counts))
