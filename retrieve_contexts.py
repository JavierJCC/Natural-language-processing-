# -*- coding: utf-8 -*-

from clean_tokens import get_text_string, get_raw_tokens
from clean_tokens import get_clean_tokens
from clean_tokens import delete_stopwords
from clean_tokens import get_vocabulary
from write import writeDict, writeList

def retrieve_contexts(text, vocabulary, windowSize):
   
    contextDict={}
    for w in vocabulary:
        context=[]
        for i in range(len(text)):
            if text[i]==w:
                for j in range(i-int(windowSize/2), i): #left context
                    if j >= 0:
                        context.append(text[j])
                try:
                    for j in range(i+1, i+(int(windowSize/2)+1)): #right context
                        context.append(text[j])
                except IndexError:
                    pass
        contextDict[w]=context 

    return contextDict

'''test if run as application'''
if __name__=='__main__':
    fname='e960401.htm'
    text_string=get_text_string(fname)
    #print text_string
    raw_tokens=get_raw_tokens(text_string)
    #print raw_tokens
    tokens=get_clean_tokens(raw_tokens) #tokens of letters, with stopwords
    print tokens
    tokens_without_stopwords=delete_stopwords('stopwords_es.txt', tokens)
    writeList(tokens_without_stopwords, 'e960401_tokens.txt')
    
    vocabulary=get_vocabulary(tokens_without_stopwords)   #vocabulary of unique tokens, with stopwords 
    writeList(vocabulary, 'e960401_vocabulary.txt')    
   
    contextDict=retrieve_contexts(tokens_without_stopwords, vocabulary, 8)
    writeDict(contextDict, 'e960401_contexts.txt')
     
    