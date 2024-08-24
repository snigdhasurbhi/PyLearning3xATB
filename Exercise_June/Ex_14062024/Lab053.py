browser=str(input("enter the browser to be tested \n"))
match browser:
    case "chrome":
        print("test for chrome browser")
    case "edge":
        print("test for edge browser")
    case "firefox":
        print("test for firefox browser")
    case "mozilla":
        print("test for mozilar browser")
    case "safari":
        print("test for safari browser")
    case "opera":
        print("test for opera browser")
    case _:
        print("invalid browser")