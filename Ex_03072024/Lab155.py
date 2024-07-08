# use of finally
#File IO
with open('snigdha','r') as file:
    print(file.read()) # we are able to see the text written in the file.
    file.close()
#with open automatically open the file,
# i need to close the file, else this file will be opened all time,so that the memory is saved
