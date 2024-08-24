# standard libarary in python which can help

#listfiles
import os
all_dir=os.listdir("/Ex_01072024")
print(all_dir)

#enivorment variable
#jdk

#Set an env
os.environ["My_var"]= 'Promode'
print(os.getenv('My_var'))