def word_count(text):
	words = text.split()

	wc = 0

	for word in words:
		wc += 1
	
	return wc

def get_char(text):
	chars = {}
	words = text.split()

	for word in words:
		for char in word:
			c = char.lower()
			if c not in chars:
				chars[c] = 1
			else:
				chars[c] += 1
	return chars

def sorted_list(dictionary):
	def sort_on(dict):
		return dict["num"]

	sort = []

	for key in dictionary:
		if key.isalpha():
			sort.append({"char": key , "num" : dictionary[key]})
	
	sort.sort(reverse=True, key=sort_on)
	
	return sort