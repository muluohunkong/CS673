while True:
    string = input("Enter a string (Enter 'q' to quit): ")
    if string == 'q':
        break
    if string == string[::-1]:
        print("The string",string,"is a palindrome.")
    else:
        print("The string",string,"is not a palindrome.")

