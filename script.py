import os
import subprocess


p = subprocess.Popen(["bash run_aloha.sh"], shell=True)
        

input = open("filename.csv","r")
output = open("newfilename.csv","w")

output.write(input.readline())
   
for line in input:
    if len(line) > 0 and line [0].isdigit():
            output.write(line)

input.close()
output.close()

       
