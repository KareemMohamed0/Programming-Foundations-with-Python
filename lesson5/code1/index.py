import urllib


def read_text():
    quotes = open("quotes.txt")
    file_content = quotes.read()
    print(file_content)
    check_profanity(file_content)
    quotes.close()


def check_profanity(text_to_check):
    connection = urllib.request.urlopen("linkhere?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("word here")
    elif "false" in output:
        print("word not here")
    else:
        print("couldn't scan the doc")


read_text()
