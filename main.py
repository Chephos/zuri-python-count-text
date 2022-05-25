# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import pprint, string

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename,'r') as f:
        file_read = f.read()
        return (file_read)

    
def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    nu_text = text.translate(str.maketrans('','',string.punctuation))
    words = {}
    list_of_words = nu_text.split()
    
    for word in list_of_words:
        words.setdefault(word.lower(),0)
        words[word.lower()] += 1

    return pprint.pprint(words)



count_words()