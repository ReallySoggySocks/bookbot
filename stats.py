def word_count(text):
	words = text.split()

	wc = 0

	for word in words:
		wc += 1
	
	return wc