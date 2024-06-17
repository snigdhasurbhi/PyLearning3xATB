#
name1 = str(input("enter the name \n")) #in api testing it will using
match name1:
    case "amit":
        print("you have entered amit")
    case "deep":
            print("you have entered deep")
    case "seema":
            print("you have entered seema")
    case "ram":
            print("you have entered ram")
    case "sham":
            print("you have entered sham")
    case "ritu":
            print("you have entered ritu")
    case "rani":
            print("you have entered rani")
    case _: #_is means default value
            print("no idea")
