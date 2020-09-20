def get_indices(document, search_term):
    indices = []
    for index, token in enumerate(document.split()):
        if token == search_term:
            indices.append(index)
    return indices
          
def count_phrase_occurences(document, phrase):
    '''
    returns the number of occurrences of a phrase in a document

    param document: a document where a given phrase is searched
    type document: str
    
    param phrase: a phrase to be searched in the document
    type phrase: str
    
    returns: the number of occurrences of the phrase in the document
    rtype: int
    
    '''
    count= 0 
    
    phrase_tokens = phrase.split()

    indices = get_indices(document, phrase_tokens[0]) 
    
    for index in indices:
        #extract new phrase from document of length given phrase length
        extracted_phrase_tokens = document.split()[index:index+len(phrase_tokens)] 
        
        #combine tokens with space to get a phrase
        extracted_phrase = ' '.join(extracted_phrase_tokens) 
        
        #remove delimiters from the end of the extracted phrase
        delimiters = ['.', '?', ':', ';', '!', ',']
        for delimiter in delimiters:
            extracted_phrase = extracted_phrase.rstrip(delimiter)
        
        #compare new extracted phrase with the given phrase
        if extracted_phrase == phrase:
            count+=1
    return count
