import re

def fix_sentence_format(sentence):
    # Remove spaces around single quotes
    fixed_sentence = re.sub(r'\s*\'\s*', "'", sentence)
    
    # Remove spaces before periods, except when followed by an uppercase letter or there is no text after the period
    fixed_sentence = re.sub(r'\s*\.(?=[^a-z]|$)', '.', fixed_sentence)

    return fixed_sentence

# Example usage:
original_sentence = "I ' m afraid I can ' t do that . Leaving the cooker while frying is completely out of the question ."
fixed_sentence = fix_sentence_format(original_sentence)

print(fixed_sentence)
