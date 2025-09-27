from stats import num_words, num_characters, sorted_dict
import sys

def get_book_text(path):
    contents = ""
    with open(path) as f:
        contents += f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    all_text = get_book_text(sys.argv[1])

    total_words = num_words(all_text)
    total_ch = num_characters(all_text)
    sorted_items = sorted_dict(total_ch)
    
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_items:
        for key in item:
            if key.isalpha():
                print(f"{key}: {item[key]}")
    print("============= END ===============")


main()