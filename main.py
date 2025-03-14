def main():
    bookPath = "books/frankenstein.txt"
    text = getBookText(bookPath)
    num_words = getNumWords(text)
    print(f"{num_words} words found in the document")


def getBookText(path):
    with open(path) as f:
        return f.read()


def getNumWords(text):
    words = text.split()
    return len(words)
main()