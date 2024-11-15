# String Manipulation Task:
# Write a Python function that takes a sentence as input and returns the most frequently occurring word.
# If there is a tie, return the word that appears first in the sentence.
# Ignore punctuation and case while counting word frequency.


import re
from collections import Counter

def most_frequent_word(sentence):
    """
    Find the most frequently occurring word in a sentence.
    
    :param sentence: Input sentence as a string.
    :return: The most frequently occurring word.
    """
    words = re.findall(r'\b\w+\b', sentence.lower())  # Extract words, ignore case
    word_counts = Counter(words)
    return max(word_counts, key=lambda word: (word_counts[word], -words.index(word)))

# Example usage:
sentence = "This is a test. This test is only a test."
print(most_frequent_word(sentence))  # Output: 'test'

