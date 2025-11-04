#turns a books contents into a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#takes get_book_text and prints out contents of book
#def main():
#   text = get_book_text("books/frankenstein.txt")
#   print(text)

#main()

#takes get_book_text and gets work count
def word_count():
    text = get_book_text("books/frankenstein.txt")
    word_list = text.split()
    print(f"Found {len(word_list)} total words")

word_count()