import os.path
try:
    file= open('example.txt','r')
    print(file.read()) # we are able to see the text written in the file.
    file.close()

except FileNotFoundError as fnfe:
  print("i am not able to find the file")

finally:
    print("closing the file")

    try:
         file.close()  # close has to be excuted
    except NameError as ne:
         print("ne")