''' Michael Reece
    problem1.py
    2/11/2019
    177000762'''


print('\t\tPalindrome Generator')
print('-------------------------------------------------------\n')
def palindrome_generator():
    positive_int = input('Enter a positive interger:')
    if palindrome(positive_int):
        print(positive_int, 'is a palindrome.')
        again()
    else:
        print('\nGereratinga palindrome....')
        counter = 0
        positive_int = int(positive_int)
        #checks the reverse of the integer until it makes the palindrome
        while not palindrome(positive_int):
            positive_int += reverse_int(str(positive_int))
            counter += 1
            print(positive_int)
        print(counter, 'iterations were needed to get to a palindrome.')
        again()
            
def palindrome(N):
# Checks if the interger inputed is already a palindrome
    if str(N) == str(N)[::-1]:
        return True
    return False

def reverse_int(N):
    reverse_int = int(N[::-1])
    #makes the reverse of the integer
    return reverse_int

def again():
    x = input('\nWould you like to try again?(Y/N): ')
    if x == 'yes' or x == 'Yes' or x == 'Y' or x == 'y' or x == 'Yea' or x== 'Yeah':
        palindrome_generator()
    else:
        print('Goodbye!!')


