def read_file():
    fp = open("quotes.txt", "r", encoding = "ISO-8859-1")
    text = []
    for line in fp:
        text.append(line)
    return text

def main():
    print(read_file())

main()
