from stats import word_count, get_char, sorted_list

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	
	return file_contents

def main():
	file_path = "books/frankenstein.txt"
	file_text = get_book_text(file_path)
	wc = word_count(file_text)
	char_list = sorted_list(get_char(file_text))

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}...")
	print("----------- Word Count ----------")
	print(f"Found {wc} total words")
	print("--------- Character Count -------")
	for dict in char_list:
		print(f'{dict["char"]}: {dict["num"]}')
	print("============= END ===============")

main()