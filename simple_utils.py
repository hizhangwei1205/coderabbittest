# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverse the characters in the input string.
    
    Parameters:
        text (str): String whose characters will be reversed.
    
    Returns:
        str: The input string with characters in reverse order.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the words in a string by splitting on whitespace.
    
    Parameters:
        sentence (str): Input text to analyze.
    
    Returns:
        int: Number of words in `sentence`; words are delimited by any whitespace.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (float|int): Temperature in degrees Celsius.
    
    Returns:
        fahrenheit (float): Temperature converted to degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32