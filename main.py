# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as file:  #open file in read-only
        fileStory = file.readlines()   #read lines from

    print(fileStory)    #print content of file
    return fileStory    


def count_words():
    text = read_file_content("Reading-Text-Files\story.txt")  #assigning content in file to variable text
    # [assignment] Add your code here
    d = {}    #creating empty dictionary

    for line in text:    #Iterate through content from file
        
        line = line.strip("?")     #to remove question marks in the text
        line = line.replace(",", "")    #removing the commas
        line = line.replace(".", "")    #removing the full stops
        line = line.strip()         #remove leading spaces and newline character
        
        #convert to lower case to avoid case mismatch
        line = line.lower()

        #split into words wherever there is a white space
        words = line.split(" ")

        
        for word in words:    #iterate through the words
            if word in d:     #check if word is in the dictionary 
                d[word] = d[word] + 1 #if word is in dictionary add count by 1
            else: 
                d[word] = 1 #if not in dictionary add word with first count
    
    for key in list(d.keys()):      #iterate through dictionary 
        print(key, ":", d[key])     #print words with their count


    #return {"as": 10, "would": 20}

read_file_content("Reading-Text-Files\story.txt")
count_words()