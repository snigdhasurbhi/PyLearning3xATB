import os
fd= os.open("testdata.txt", os.O_RDWR)
os.write(fd,b"hello i writing for api test")# in the testdata the text we have written it will appear there
os.close(fd)