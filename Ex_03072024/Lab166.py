# File Handling
# How to Read a Text and Write into it using Python code


# Function-
# Pre built function open("file_name", "mode")


# Mode-
# 'r' for reading(default)
# 'w' for writing (creates a new file or truncates an existing one)
# 'a' for appending
# 'b' for binary mode
# '+' for updating (reading and writing)


# Read and Write content
# Read a File
# Reading entire content : Content = file_object.read()
# line = file_object.readline() for single line
# lines = file_object.readlines() for all lines in a list.
# # Close the file


file = open("TestData.txt")
content = file.read()
print(content)
file.close()