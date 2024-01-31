list1 = input("Enter the first list in the format [element1,element2,...,elementn]: ")
list2 = input("Enter the second list in the format [element1,element2,...,elementn]: ")

try:
    list1 = list1.strip("[]").split(',')
    list2 = list2.strip("[]").split(',')

    if len(list1) != len(list2):
        print("Error: The lengths of these two lists are not equal.")

    MergedList = [None]*(len(list1)+len(list2))
    MergedList[::2] = list1
    MergedList[1::2] = list2

    print(MergedList)

except Exception as error:
    print(error)
