import os
import subprocess
import re


for filename in os.listdir(os.getcwd()):   
     #print (filename)
     if filename == "aloha-throughput.cc":
         f = open("SF.csv", "w+")
         
         p = subprocess.Popen(["bash run_aloha.sh",filename], shell=True,stdout=f)#stdout=subprocess.PIPE), stderr=subprocess.PIPE)
         stdout_results, stderr_results = p.communicate()
        
         #re.findall('^[0-9].*',f,re.MULTILINE)
"""with open("SF.csv","r+") as d:
         for line in d:
             if len(line) > 0 and line [0].isdigit():
                print(line)
                d.write(line)
def removetext():
"""
input = open("SF.csv","r")
output = open("SF_7.csv","w")

output.write(input.readline())
   
for line in input:
    if len(line) > 0 and line [0].isdigit():
            output.write(line)

input.close()
output.close()

       
