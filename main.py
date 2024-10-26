def main():     
    with open("books/frankenstein.txt") as f:

        file_contents = f.read()

        words = file_contents.split()
        wc = len(words)

        lowered = file_contents.lower()

        char = {}
        cc = [
            {"letter": 'a', "num": 7}
        ]

        for chars in lowered:
            if chars.isalpha():
                if chars in char:
                    char[chars] += 1
                else:
                    char[chars] = 1
            else:
                pass

        print(
            "--- Begin report of books/frankenstein.txt --- \n", 
            f"{wc} words found in the document \n\n",
            )
        
        for letter in char:
            print(f"The '{letter}' character was found {char[letter]} number of times")

        print("--- End Report --- \n")

        return

main()