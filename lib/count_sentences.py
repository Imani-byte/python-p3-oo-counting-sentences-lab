#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    if not isinstance(value, str):
      print("The value must be a string.")
    self.value = value

  def is_sentence(self):
    return self.value.endswith('.')

  def is_question(self):
    return self.value.endswith('?')

  def is_exclamation(self):
    return self.value.endswith('!')

  def count_sentences(self):
    # Replace common sentence-ending punctuation with a period
    normalized_string = self.value.replace('?', '.').replace('!', '.')
        
    # Split the string into sentences using '.' as the separator
    sentences = normalized_string.split('.')
        
    # Count the number of non-empty sentences
    count = sum(1 for sentence in sentences if sentence.strip())
    return count
