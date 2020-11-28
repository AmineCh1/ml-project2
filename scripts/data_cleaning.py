import re
import itertools
from helpers import *

CONTRACTION_DIC = {
    "ain't":"is not",
    "aint":"is not",
    "amn't":"am not",
    "amn't":"am not",
    "amnt":"am not",
    "aren't":"are not",
    "arent":"are not",
    "can't":"cannot",
    "cant":"cannot",
    "'cause":"because",
    "couldn't":"could not",
    "couldnt":"could not",
    "couldn't've":"could not have",
    "couldnt've":"could not have",
    "could've":"could have",
    "couldve":"could have",
    "daren't":"dare not",
    "darent":"dare not",
    "daresn't":"dare not",
    "daresnt":"dare not",
    "dasn't":"dare not",
    "dasnt":"dare not",
    "didn't":"did not",
    "didnt":"did not",
    "doesn't":"does not",
    "doesnt":"does not",
    "don't":"do not",
    "dont":"do not",
    "e'er":"ever",
    "eer":"ever",
    "em":"them",
    "everyone's":"everyone is",
    "finna":"fixing to",
    "gimme":"give me",
    "gonna":"going to",
    "gon't":"go not",
    "gont":"go not",
    "gotta":"got to",
    "hadn't":"had not",
    "hadnt":"had not",
    "hasn't":"has not",
    "hasnt":"has not",
    "haven't":"have not",
    "havent":"have not",
    "he'd":"he would",
    "hed":"he would",
    "he'll":"he will",
    "he's":"he is",
    "hes":"he is",
    "he've":"he have",
    "heve":"he have",
    "how'd":"how would",
    "howd":"how would",
    "how'll":"how will",
    "how're":"how are",
    "howre":"how are",
    "how's":"how is",
    "hows":"how is",
    "i'd":"i would",
    "i'll":"i will",
    "i'm":"i am",
    "im":"i am",
    "i'm'a":"i am about to",
    "ima":"i am about to",
    "i'm'o":"i am going to",
    "imo":"i am going to",
    "isn't":"is not",
    "isnt":"is not",
    "it'd":"it would",
    "itd":"it would",
    "it'll":"it will",
    "itll":"it will",
    "it's":"it is",
    "its":"it is",
    "i've":"i have",
    "ive":"i have",
    "kinda":"kind of",
    "let's":"let us",
    "lets":"let us",
    "mayn't":"may not",
    "maynt":"may not",
    "may've":"may have",
    "mayve":"may have",
    "mightn't":"might not",
    "mightnt":"might not",
    "might've":"might have",
    "mightve":"might have",
    "mustn't":"must not",
    "mustnt":"must not",
    "mustn't've":"must not have",
    "mustnt've":"must not have",
    "must've":"must have",
    "mustve":"must have",
    "needn't":"need not",
    "neednt":"need not",
    "ne'er":"never",
    "o'":"of",
    "o'er":"over",
    "ol'":"old",
    "oughtn't":"ought not",
    "oughtnt":"ought not",
    "shalln't":"shall not",
    "shallnt":"shall not",
    "shan't":"shall not",
    "shant":"shall not",
    "she'd":"she would",
    "shed":"she would",
    "she'll":"she will",
    "shell":"she will",
    "she's":"she is",
    "shes":"she is",
    "shouldn't":"should not",
    "shouldnt":"should not",
    "shouldn't've":"should not have",
    "shouldnt've":"should not have",
    "should've":"should have",
    "shouldve":"should have",
    "somebody's":"somebody is",
    "someone's":"someone is",
    "something's":"something is",
    "that'd":"that would",
    "thatd":"that would",
    "that'll":"that will",
    "thatll":"that will",
    "that're":"that are",
    "thatre":"that are",
    "that's":"that is",
    "thats":"that is",
    "there'd":"there would",
    "thered":"there would",
    "there'll":"there will",
    "therell":"there will",
    "there're":"there are",
    "therere":"there are",
    "there's":"there is",
    "theres":"there is",
    "these're":"these are",
    "thesere":"these are",
    "they'd":"they would",
    "theyd":"they would",
    "they'll":"they will",
    "theyll":"they will",
    "they're":"they are",
    "theyre":"they are",
    "they've":"they have",
    "theyve":"they have",
    "this's":"this is",
    "thiss":"this is",
    "those're":"those are",
    "thosere":"those are",
    "'tis":"it is",
    "'twas":"it was",
    "wanna":"want to",
    "wasn't":"was not",
    "wasnt":"was not",
    "we'd":"we would",
    "we'd've":"we would have",
    "we'll":"we will",
    "we're":"we are",
    "weren't":"were not",
    "werent":"were not",
    "we've":"we have",
    "weve":"we have",
    "what'd":"what did",
    "whatd":"what did",
    "what'll":"what will",
    "whatll":"what will",
    "what're":"what are",
    "whatre":"what are",
    "what's":"what is",
    "whats":"what is",
    "what've":"what have",
    "whatve":"what have",
    "when's":"when is",
    "whens":"when is",
    "where'd":"where did",
    "whered":"where did",
    "where're":"where are",
    "wherere":"where are",
    "where's":"where is",
    "wheres":"where is",
    "where've":"where have",
    "whereve":"where have",
    "which's":"which is",
    "whichs":"which is",
    "who'd":"who would",
    "whod":"who would",
    "who'd've":"who would have",
    "whod've":"who would have",
    "who'll":"who will",
    "wholl":"who will",
    "who're":"who are",
    "who's":"who is",
    "who've":"who have",
    "whove":"who have",
    "why'd":"why did",
    "whyd":"why did",
    "why're":"why are",
    "whyre":"why are",
    "why's":"why is",
    "won't":"will not",
    "wont":"will not",
    "wouldn't":"would not",
    "wouldnt":"would not",
    "would've":"would have",
    "wouldve":"would have",
    "y'all":"you all",
    "yall":"you all",
    "you'd":"you would",
    "youd": "you would",
    "you'll":"you will",
    "youll":"you will",
    "you're":"you are",
    "youre":"you are",
    "you've":"you have",
    "youve":"you have",
    "whatcha":"What are you",
    "whut":"what",
    "luv":"love",
    "ya":"you",
    "sux":"sucks",
    "k":"ok"
}

def replace_numbers(t):
    '''
    Replace number in the tweet by the string "<number>"
    So we can make the difference with the word "number"
    
    '''
    tweet = ''
    words = t.split()
    
    for w in words:
        if w.isdigit():
            tweet += '<number> '
        else: 
            tweet += w + ' '

    return tweet.strip()

def reduce_chars(t):
    '''
    Reduce the occurence of a same character in a word to a maximum of 2

    '''
    tweet = ''

    for _, s in itertools.groupby(t):
        tweet += ''.join(''.join(s)[:2]) #for _, s in itertools.groupby(t))
        
    return tweet

def delete_user_and_url(t):
    '''
    Delete words "<user>" and "<url>" from the tweet
    
    '''
    tweet = ''
    words = t.split()
    
    for w in words:
        if w == "<user>" or w == "<url>":
            tweet += ''
        else:
            tweet += w + ' '
            
    return tweet.strip()


def delete_punctuation(t):
    '''
    Delete punctuation characters from the tweet
    
    '''
    punctuation = "[\.\,\:\;\?\!\<\>\(\)\/\#\=\n]"
    
    return ''.join(re.sub(punctuation, "", t)).strip()


def decontracted(t, dic):
    # specific
    t = re.sub(r"won\'t", "will not", t)
    t = re.sub(r"can\'t", "can not", t)

    # general
    t = re.sub(r"n\'t", " not", t)
    t = re.sub(r"\'re", " are", t)
    t = re.sub(r"\'s", " is", t)
    t = re.sub(r"\'d", " would", t)
    t = re.sub(r"\'ll", " will", t)
    t = re.sub(r"\'t", " not", t)
    t = re.sub(r"\'ve", " have", t)
    t = re.sub(r"\'m", " am", t)

    #
    # USE REGEX? OR ONLY MANUALLY CREATED DICTIONARY?
    #
    
    tweet = ''
    t = t.replace("’","'")
    words = t.split()
    
    for w in words:
        tweet += (dic[w] if w in dic else w) + ' '
    
    return tweet.strip()


def remove_stopwords(tweet):
    stop_words=['the', 'a', 'and', 'is', 'be', 'will']
    tweet = ' '.join([word for word in tweet.split() if word not in stop_words])
    return tweet


def preprocess_tweet(tweet):
    #Replacing numbers
    tw = replace_numbers(tweet)
    #Replacing url and user
    tw_url = delete_user_and_url(tw)
    #Remove repetitions
    tw_reduced = reduce_chars(tw_url)
    #Remove contraction 
    tw_wo_cont = decontracted(tw_reduced, CONTRACTION_DIC)
    # Remove stopwords
    tw_stop = remove_stopwords(tw_wo_cont)
    #Remove punctuation
    tw_punct = delete_punctuation(tw_stop)
    
    return tw_punct
    



