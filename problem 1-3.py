''' Michael Reece
    problem3.py
    2/11/2019
    177000762'''

essayfilename = input('Enter essay file name(including .txt): ')
def evaluate_essay(essayfilename):
    in_file = open(essayfilename, 'r')
    #opening the file that you want to read
    counter = 0
    long_words = []
    medium_words = []
    short_words = []
    #separating words
    for lines in in_file:
        for words in lines.split():
            if len(words) <= 3:
                short_words.append(words)
            elif len(words) <= 6:
                medium_words.append(words)
            else:
                long_words.append(words)
                counter += 1
    #Putting each word in the correct dictionary
    in_file.close()
    if (len(long_words) / counter) >= .5:
        print('This is a college level essay.')
    elif len(long_words) > len(medium_words) and len(long_words) > len(short_words):
        pritn('This is a high school level essay')
    elif len(medium_words) > len(long_words) and len(medium_words) > len(short_words):
        print('This is a middle school level essay')
    else:
        print('This is an elementary school level essay')
    #showing the user which level their essay is
  
