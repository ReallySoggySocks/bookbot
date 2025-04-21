from stats import word_count, get_char

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	
	return file_contents

def main():
	file_text = get_book_text("books/frankenstein.txt")
	print(f"{word_count(file_text)} words found in the document")
	print(get_char(file_text))

main()