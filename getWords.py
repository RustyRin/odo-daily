import requests
import random
import pytumblr

def getAll():
    print("Downloading dictionary")
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    words = response.content.splitlines()
    print(words)
    with open("dictionary.txt", "w") as dictionary:
        for line in words:
            print(line.decode("utf-8"))
            dictionary.write(line.decode("utf-8") + "\n")
    print("\nWords added to file")
    dictionary.close()

def getIngWords():
    print("Sorting words")
    ingWords = open("ingWords.txt", "w")
    with open("dictionary.txt", "r") as dictionary:
        for line in dictionary:
            if "ing" in line:
                ingWords.write(line.lower())
    ingWords.close()

def getRandomWord():
    return random.choice(open("ingWords.txt").readlines())

def read_secrets(filename):
    try:
        text = open(filename, 'r')
        lines = []
        for line in text:
            line = line.replace('\n', '')
            lines.append(line)
        text.close()
        return lines
    except:
        print('!!! Cannot find ' + filename + ' or it has been deleted !!!')

def post():
    client = pytumblr.TumblrRestClient(read_secrets('secrets_tumblr')[0],  # TUMBLR secrets. don't share
                                       read_secrets('secrets_tumblr')[1],
                                       read_secrets('secrets_tumblr')[2],
                                       read_secrets('secrets_tumblr')[3])
    blogName = "constable-odo-daily"

    client.create_text(blogName, state="queue",  title="No " + getRandomWord() + "on the Promenade!", tags=["star trek", "deep space nine", "odo", "daily", "startrek", "ds9"])
def main():
    #getAll()
    #getIngWords()
    for x in range(0, 200):
        post()

if __name__ == '__main__':
    main()