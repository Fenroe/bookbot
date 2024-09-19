def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def print_text(text):
    print(text)

def count_words(text):
    try:
        word_count = len(text.split())
        return word_count
    except Exception as e:
        print("Error in the count_words function. See below")
        print(e)

def count_characters(text):
    character_count = {}
    lower_text = text.lower()
    for t in lower_text:
        try:
            if t in character_count:
                character_count[t] += 1
            else:
                character_count[t] = 1
        except Exception as e:
            print("Error in loop. See below")
            print(e)
    return character_count

def sort_on(dict):
    return dict["count"]

def sort_character_occurrences(character_dict):
    character_list = []
    for k in character_dict:
        if k.isalpha():
            dict = {
                "name": k,
                "count": character_dict[k]
            }
            character_list.append(dict)
    character_list.sort(reverse=True, key=sort_on)
    return character_list


def generate_report(path):
    print(f"--- Begin report of {path} ---")
    text = get_text(path)
    word_count = count_words(text)
    print(f"{word_count} words found in the document")
    character_count_dict = count_characters(text)
    sorted_list = sort_character_occurrences(character_count_dict)
    for s in sorted_list:
        name = s["name"]
        count = s["count"]
        print(f"The '{name}' character was found {count} times")
    

def main():
    generate_report("./books/frankenstein.txt")

main()