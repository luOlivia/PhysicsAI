#takes in physics problems from problems.txt and processes them
#for now, we aren't taking in txt file and just working with 1 problem
#import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag

def find_subject(last_sen):
    tokenme = word_tokenize(last_sen)
    re = ""
    pos = pos_tag(tokenme)
    for p in pos:
        if p[1]=="NN":
            re = p[0]
            #print("subject: ",re)
            return re

def lp(problem):
    findnoun_arr = problem.split(". ")
    last_sen = findnoun_arr[-1]
    subject = find_subject(last_sen)
    #print(last_sen)
    lmtzr = WordNetLemmatizer()
    tokenize = word_tokenize(problem)
    no_stop = []
    varry = []
    for i in range(len(tokenize)):
        w = tokenize[i]
        if (w not in stopWords and w not in punct) or w == "s":#keep s, which was flagged as a stopword
            addme = lmtzr.lemmatize(w)
            if addme[0].isalpha() == False:
                unit = tokenize[i+1]
                #print("number: ", addme," unit: ",unit)
                varry.append((addme,unit))
            no_stop.append(addme)
    return(subject,varry)
    #print(no_stop) #full sentence
    #returns (what to solve for, list of known variables with units)

stopWords = set(stopwords.words('english'))
punct = [".",","]
problem = "An airplane accelerates down a runway at 3.20 m/s2 for 32.8 s until it finally lifts off the ground. Determine the distance traveled before takeoff."
print(lp(problem))
