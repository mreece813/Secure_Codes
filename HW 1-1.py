def main():
    original_Num = int(input("Enter a positive interger: "))
    check(original_Num)
    gen_Pal(original_Num)
    again()

def check(original_Num):
        if original_Num == int(str(original_Num)[::-1]):
            print(original_Num, "is a palindrome.")
            x = again()
        else:
            print(original_Num, "is not a palindrome.")
            print('\nGenerating palindrome...')
            

def gen_Pal(original_Num):
    counter = 0
    reverse_Num = int(str(original_Num)[::-1])
    counter = counter + 1
    new_Num = original_Num + reverse_Num
    original_Num = new_Num
    if original_Num == int(str(original_Num)[::-1]):
        print(original_Num)
        print('\n')
        print(counter, "iteration were needed to get to a palindrome.")
    else:
        print(new_Num)
        counter +=1
        reverse_Num = gen_Pal(original_Num)
    
    
def again():
    x = input('\nWould you like to try again?(Y/N): ')
    if x == 'yes' or x == 'Yes' or x == 'Y' or x == 'y' or x == 'Yea' or x== 'Yeah':
        main()
    else:
        print('Goodbye!!')


main()
