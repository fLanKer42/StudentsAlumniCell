def palindrome_test(string):
    for i in range(0,len(string)//2):
        if string[i] != string[(-1)*(i+1)]:
            return "This string is not a palindrome"
    return "This string is a palindrome"

if __name__ == '__main__':
    string = input()
    print(palindrome_test(string))