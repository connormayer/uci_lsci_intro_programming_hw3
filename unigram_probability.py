# Your job in this file is to implement two functions that will let us
# - train a unigram probability model
# - calculate the unigram probabilities of new words
#
# For details on unigram models, see Friday's lecture. In both cases your 
# code should be insensitive to case (so "dog" and "Dog") are the same word.

# Here's a sample training and test pair you can play around with, but you
# should write your code so it works for any input. I've removed
# all punctuation except for in contractions
training_data = [
    'You', 'know', 'this', 'is', 'excuse', 'me', 'a', 'damn', 'fine', 'cup',
    'of', 'coffee', "I've", 'had', 'I', "can't", 'tell', 'you', 'how', 'many', 
    'cups', 'of', 'coffee', 'in', 'my', 'life', 'and', 'this', 'this', 'is', 'one', 
    'of', 'the', 'best'
]

test_data = ['Coffee', 'is', 'my', 'life']

###################################################################################
# 1: Implement a function called "train_unigram_model". This should take as       #
#    input a list of strings and return a dictionary mapping words to their       #
#    unigram probabilties.                                                        #
#                                                                                 #
#    For example, if the input is ['dog', 'cat', 'cat', 'cat'], the output should #
#    be the dictionary {'dog': 0.25, cat: '0.75'}.                                #
###################################################################################




#####################################################################################
# 2: Implement another function called "score_sentence". This should take as input  #
#    two arguments: a dictionary defining a unigram model in the format described   #
#    above, and a list of strings representing a sentence. The function should      #
#    return a float representing the unigram probability of the sentence according  #
#    to the unigram model.                                                          #
#                                                                                   #
#    For example, if the input model is {'dog': 0.25, cat: '0.75'} and the input    #
#    sentence is ["dog", "cat", "dog"], the return value should be 0.046875.        #
#####################################################################################




# DO NOT MODIFY THE FOLLOWING LINE
if __name__ == "__main__":
    # You can add code here to test your functions
    pass