def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
    def word_count():
        wc = 0
        for word in words:
            wc += 1
        print(wc)
    word_count()
main()
