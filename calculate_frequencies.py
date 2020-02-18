!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    file_contents = file_contents.lower()   #Convert all strings in text file to lower case.
    separate_words = file_contents.split()  #Separate words from text file into a list.
    results = {} #The dictionary that will contain the final set of words and their frequencies.
    for word in separate_words: #Iterate every word in the list.
        no_punc_word = ""
        for char in word: #Iterate every character in the word and remove punctuation.
            if char not in punctuations:
                no_punc_word += char
        
        if no_punc_word not in uninteresting_words and no_punc_word.isalpha(): #Check if word is uninteresting and consists of alpha only.
            if no_punc_word not in results: #Add the word as key and frequency as value in the Dictionary.
                results[no_punc_word] = 1
            else:
                results[no_punc_word] += 1
        
     
            
            
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(results)
    return cloud.to_array()