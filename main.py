def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        letterdict = {}
        for i in range(len(words)):
            words[i] = words[i].lower()
            for char in words[i]:
                if char in letterdict:
                    letterdict[char] += 1
                else:
                    letterdict[char] = 1
        letterlist = []

        for letter in letterdict:
            if letter.isalpha():
                letterlist.append({"letter" : letter, "count" : letterdict[letter]})

        def sort_on(dict):
            return dict["count"]
        letterlist.sort(reverse = True, key = sort_on)

        for item in letterlist:
            letter = item["letter"]
            count = item["count"]
            print(f"The '{letter}' character was found {count} times")



main()