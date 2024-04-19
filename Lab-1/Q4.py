#Q.4 of Assignment-1
import random
class TextGenerator:
    def __init__(self):
        self.prefix_dict={} # the prefix dictionary 
        
    def assimilateText(self,file):
        self.file=file
        my_file = open(self.file,"r+",encoding="mbcs") # for encoding (in window)
        content=my_file.read()  
        split_words = content.split() # split() function splits the text of word file into list of words
        #creating with each two tuples as keys and intially the corresponding values is taken empty
        self.prefix_dict={(split_words[i-1],split_words[i]):[] for i in range(1,len(split_words)) }
        
        # The values are poulated in the dictionary according to the keys
        for i in range(1, len(split_words) - 1):
            self.prefix_dict[(split_words[i - 1], split_words[i])].append(split_words[i + 1])
        my_file.close()
        return self
    def generateText(self,number_words,word=None):
        self.number_words=number_words
        self.word= word 
        generating_word=[] # list to short the word of output texts
        dummy=[] # A dummy list of two entries to act as key for the dictionary
        #checking given word is string or not, if not then taking random list from dictionary
        if isinstance(word,str)==False:
          generating_word=list(random.choice(list(self.prefix_dict.keys())))    
        # next part throws exception if the given word is not found in the text file
        elif self.word not in [key[0] for key in self.prefix_dict.keys()]:
                try:
                  raise Exception('Unable to produce text with the specified start word')
                except Exception as l:
                     print(type(l))
                     print(l) 
                exit()
        else:
               for key in self.prefix_dict.keys(): #iterating over the prefix dictionary to check if our given
                  if (key[0]==self.word):          #word is present in dictionary as a first element of key 
                    generating_word.append(key)                  #tuples or not
               generating_word=list(random.choice(dummy))
        #generating text in next parts
        if len(self.prefix_dict[tuple(generating_word)]) >0:
          dummy=generating_word
        while len(generating_word) <=self.number_words:
          dummy=[generating_word[len(generating_word)-2],generating_word[len(generating_word)-1]]
          if (len(self.prefix_dict[tuple(dummy)]))==0:
            break
          generating_word.append(random.choice(self.prefix_dict[tuple(dummy)]))
          dummy.clear()
        print(" ".join(generating_word))
t=TextGenerator()
t.assimilateText(r"C:\Users\ZAHIR\OneDrive\Desktop\sherlock.txt") #"r" produces raw text
t.generateText(20,'the')

