# https://www.educative.io/courses/grokking-coding-interview-patterns-python/valid-word-abbreviation 
def valid_word_abbreviation(word, abbr):

    # Replace the following return statement with your code
    index_w = 0
    index_a = 0
    w_len = len(word)
    a_len = len(abbr)
    while index_w < w_len or index_a < a_len:
      print("Before ", index_w, index_a)
      if index_w >= w_len or index_a >= a_len:
        return False
      abbr_c = abbr[index_a]
      word_c = word[index_w]
      if abbr_c == "0":
        return False
      elif abbr_c.isdigit():
        index_a += 1
        if index_a < a_len:
          next_c = abbr[index_a]
          if next_c.isdigit():
            abbr_c = str(abbr_c) + str(next_c)
            index_a += 1
        print(abbr_c)
        index_w += int(abbr_c)
      print("After ", index_w, index_a)
      if index_w == w_len and index_a == a_len:
        return True
      elif index_w > w_len or index_a > a_len:
        return False
      elif abbr[index_a] != word[index_w]:
        return False
      index_w += 1
      index_a += 1
    else: # Unnecessary
      return True