def get_num_words(content):
    text = content.split()
    num_words = len(text)
    return num_words

def get_char_stats(text):
    stats = {}
    char = list(text)
    for character in text:
        lower_char = character.lower()
        if not lower_char in stats:
            stats[lower_char] = 1
        else:
            stats[lower_char] += 1
    return stats


def sort_on(items):
    return items["num"]

def sorted(dict):
    sorted = dict.sort(reverse=True, key=sort_on)
    return sorted


def sort_dict(dict):
    sorted_dict = []
    temp_dict = {}

    for item in dict:
        temp_dict = {}
        #print(f"item: {item}")
        #print(f"value:{dict[item]}")
        temp_dict["char"] = item
        temp_dict["num"] = dict[item]
        sorted_dict.append(temp_dict)
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict
    
