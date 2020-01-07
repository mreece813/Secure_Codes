''' Michael Reece 
    problem2.py
    2/11/2019
    177000762 '''

print('\t---------------------------')
print('\t Ubbi Dubbi Translator')
print('\t---------------------------')
vowel = ['a', 'e', 'i', 'o', 'u', 'y', 'uba', 'ube', 'ubi','ubo','ubu','uby']
def ubbidubbi_word(eword):
# These if and elif statements deal with adding 'ub' in front of the vowels and if the ending letter is an E
    eword = list(eword)
    if eword[0].lower() in vowel:
        eword[0] = 'ub' + eword[0]
    if eword[-1] == 'e':
        for letter in range(1, len(eword) - 1):
            if eword[letter] in vowel:
                if eword[letter-1] not in vowel:
                    eword[letter] = 'ub' + eword[letter]
    elif eword[-1].isalpha and eword[-2] == 'e':
        for letter in range(1, len(eword[letter] - 2)):
            if eword[letter] in vowel:
                if eword[letter-1] not in vowel:
                    eword[letter] = 'ub' + eword[letter]
                
    elif eword[-1] != 'e':
        for letter in range(1, len(eword)):
            if eword[letter]in vowel:
                if eword[letter-1] not in vowel:
                    eword[letter] = 'ub' + eword[letter]

    return eword

def ubbidubbi_sentence(esentence):
# Where the sentence will be broken into a list of words and translated into Ubbi Dubbi 
    esentence = esentence.split(" ")
    esentence = [''.join(ubbidubbi_word(words)) for words in esentence]
    return (' '.join(esentence))

def ubbidubbi_translator():
# This is where the user will input a sentence and get the translation
    esentence = input('Enter an English sentence: ')
    print('Translation: ', ubbidubbi_sentence(esentence))
    again()

def again():
# Ask the User if they would like to try another sentence
    x = input('\nWould you like to do another?(Y/N): ')
    if x == 'yes' or x == 'Yes' or x == 'Y' or x == 'y' or x == 'Yea' or x== 'Yeah':
        ubbidubbi_translator()
    else:
        print('gubo ubin pubeace! guboodbubye!')
