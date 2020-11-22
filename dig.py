#!/usr/bin/env python 
# coded by Eslam Akl - @eslam3kl 


import re 
import sys 
import subprocess 
import threading 
import time 
from termcolor import colored

print("----------------------------------------")
print(colored("[*] ","red") + colored("Start collecting more subdomains", "white"))
print(colored("[*] ", "red") + colored("It may take more time, please wait", "white"))
print("----------------------------------------\n")
file_name = sys.argv[1] #dell.txt
word = file_name.split(".txt")[0] #dell
keywords = []
with open(file_name, "r") as domains: 
	for domain in domains: # uat.develop.dell.com
		if word + "." in domain:
			first_part = domain.split("." + word)[0] # uat.develop     .dell.com
			second_part = domain.split(first_part)[1]
			if second_part: 
				line = first_part.split(".") #uat(0)   develop(1)
				length = len(line) #2
				line2 = line[length-1] + second_part #1 develop
				if line2 not in keywords:
					keywords.append(line2)

for line in keywords: 
	line = line.strip()
	#print line 
arr_length = len(keywords)

for line in keywords: 
	subprocess.call("python repeat_crt.py -u " + line, shell=True)

#[==========[ Use Multithread only if your PC resources enough ]============] 

'''
i = 0 
j = 1 


while i < arr_length:
	try: 
		t1 = threading.Thread(target=get_subdomains, args=(keywords[i],)) # 0, 2,    
		t1.start() 
		t2 = threading.Thread(target=get_subdomains, args=(keywords[i+1],)) # 1, 3, 
		t2.start()
	except: 
		pass 
	i = i + 2   


#start_time = time.time()
#main()
#print("--- %s seconds ---" % (time.time() - start_time))
'''