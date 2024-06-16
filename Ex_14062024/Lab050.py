#Multiple condition
#switch
#if,elif,else
#match
number= int(input("enter the number\n"))
match number:
    case 1:
        print("you have entered 1")
    case 2:
            print("you have entered 2")
    case 3:
            print("you have entered 3")
    case 4:
            print("you have entered 4")
    case 5:
            print("you have entered 5")
    case 6:
            print("you have entered 6")
    case 7:
            print("you have entered 7")
    case _: #_is means default value
            print("no idea")