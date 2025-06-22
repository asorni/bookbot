def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars_stats = {}
    for c in text:
        if c.lower() in chars_stats:
            chars_stats[c.lower()] = chars_stats[c.lower()] + 1
        else:
            chars_stats[c.lower()] = 1
    return chars_stats

def get_num(item):
    return item["num"]

def to_sorted_list(chars_count):
    result = []
    for c in chars_count:
        new_item = {}
        new_item["char"] = c
        new_item["num"] = chars_count[c]
        result.append(new_item)
    result.sort(key=get_num, reverse=True)
    return result