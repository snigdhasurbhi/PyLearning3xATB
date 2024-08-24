# Walk me in directory
import os
for root, dir,files in os.walk("/Ex_01072024"):
    print(f'current dir {root}')
    print(f'sub dir dir {dir}')
    print(f"files dir dir {files}")
    print(len(files))# it will give the length of the files