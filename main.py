def main():     
    with open("books/frankenstein.txt") as f:

        file_contents = f.read()

        words = file_contents.split()
        wc = len(words)

        lowered = file_contents.lower()

        char = {}
        cc = []

        for chars in lowered:
            if chars.isalpha():
                if chars in char:
                    char[chars] += 1
                else:
                    char[chars] = 1
            else:
                pass


        for key in char:
            num = char[key]
            cc.append({'char': key, 'num': num})
        
        cc.sort(reverse=True, key=sort_on)

        print(
            "--- Begin report of books/frankenstein.txt --- \n", 
            f"{wc} words found in the document \n\n",
            )
        
        for letter in cc:
            print(f"The {letter} character was found {0} times")

        print("--- End Report --- \n")

        return

def sort_on(dict):
    return dict['num']

main()