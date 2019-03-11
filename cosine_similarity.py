# -*- coding: utf-8 -*-
import operator
import numpy as np
import math
from raw_freq_vectors import raw_freq_vectors
from write import writeList2
from clean_tokens import get_text_string, get_raw_tokens
  
def cosine_similarity(raw_freq_vectors_dict, word):
    similar_words_dict={}
    vector_to_compare=raw_freq_vectors_dict[word]
    v_to_compare=np.array(vector_to_compare)
    print 'El vector a comparar'
    print v_to_compare
    
    vc_squared=v_to_compare**2
    vc_sum=vc_squared.sum()
    vc_length=math.sqrt(vc_sum) 
    
    i=0
    for key in raw_freq_vectors_dict.keys():
        v=np.array(raw_freq_vectors_dict[key])
        
        v_squared=v**2
        v_sum=v_squared.sum()
        v_length=math.sqrt(v_sum) 
        lengths_product=vc_length*v_length
        
        similar_words_dict[key]=np.dot(v_to_compare, v)/lengths_product        
        i+=1
        print('cosine_similarity function ', str(i), str(similar_words_dict[key]))
    
    similar_words = sorted(similar_words_dict.items(), key=operator.itemgetter(1), reverse=True)
    return similar_words

def probability(raw_freq_vectors_dict, word, value):
    similar_words_dict={}
    vector_to_compare=raw_freq_vectors_dict[word]
    v_to_compare=np.array(vector_to_compare)
    print 'El vector a comparar'
    print v_to_compare
    
    vc_squared=v_to_compare**2
    vc_sum=vc_squared.sum()
    vc_length=math.sqrt(vc_sum) 
    
    i=0
    for key in raw_freq_vectors_dict.keys():
        v=np.array(raw_freq_vectors_dict[key])
        v=v/value
        v_squared=v**2
        v_sum=v_squared.sum()
        v_length=math.sqrt(v_sum) 
        lengths_product=vc_length*v_length
        
        similar_words_dict[key]=np.dot(v_to_compare, v)/lengths_product        
        i+=1
        print('cosine_similarity function ', str(i), str(similar_words_dict[key]))
    
    similar_words = sorted(similar_words_dict.items(), key=operator.itemgetter(1), reverse=True)
    return similar_words

def cal_frecuencia (word):
    fname='e960401.htm'
    frecuencia = get_text_string(fname)
    return frecuencia.count(word)
    
'''test if run as application'''
if __name__=='__main__':
    fname_vocabulary='e960401_vocabulary.txt'    
    fname_contexts='e960401_contexts.txt'
    word='empresa'
    value=2
    
    raw_freq_vectors_dict=raw_freq_vectors(fname_vocabulary, fname_contexts)
    print type(raw_freq_vectors_dict)
    print value
    similar_words=cosine_similarity(raw_freq_vectors_dict, word)
    #pb=probability(raw_freq_vectors_dict, word, value)
    writeList2(similar_words, word+'_similar_words_without_stopwords.txt')
    #writeList2(pb, word+'_similar_words_without_stopwords.txt')