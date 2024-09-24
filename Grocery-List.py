list = []
while True:
    print("Choose an Option: ")
    print('[1] Add an Item')
    print('[2] View the List')
    print('[3] Remove an Item')
    print('[4] Exit')
    choice = int(input("Enter your Choice: "))

    match choice:
        case 1: 
            add = input("What do you want to add?: ")
            list.append(add)
        case 2:
            print(list)
        case 3:
            removal = input('Choose an item to Remove: ')
            if removal not in list:
                print('error')
            else:
                list.remove(removal)
        case 4:
            break
