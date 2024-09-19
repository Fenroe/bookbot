def get_frankenstein_text():
    with open("./books/frankenstein.txt") as f:
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

def main():
    # Frankenstein
    frankenstein_text = get_frankenstein_text()
    print_text(frankenstein_text)
    # newline
    print("")
    print(f"Total words in Frankenstein: {count_words(frankenstein_text)}")

main()