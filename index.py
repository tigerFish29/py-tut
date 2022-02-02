from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
# loop through the url 
for line in story:
    line_words = line.decode('utf8').split() # decoding the bytes 
    for word in line_words:
        story_words.append(word)

story.close()

print(story_words)