# file = open("TestData2.txt")# this file is not present in the same folder,
# FileNotFoundError: [Errno 2] No such file or directory: 'TestData2.txt'
# we have to copy and absoulte path of the file
file = open('C:/Users/snigd/PycharmProjects/PyLearning 3xATB/Ex_01072024/textdata2','r' )
content = file.read()
print(content)
file.close()