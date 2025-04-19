from stats import word_count

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	
	return file_contents

def main():
	print(f"{word_count(get_book_text("books/frankenstein.txt"))} words found in the document")

main()