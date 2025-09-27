def num_words(text):
    total_words = 0
    text_list = text.split()
    for word in text_list:
        total_words += 1
    return total_words

def num_characters(text):
    char_dict = {}
    text_list = text.split()
    for word in text_list:
        for char in word:
            ch = char.lower()
            if ch not in char_dict:
                char_dict[ch] = 1
            else:
                char_dict[ch] += 1
    return char_dict

def sorted_dict(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    list_of_dicts = [{key: value} for key, value in sorted_items]
    return list_of_dicts