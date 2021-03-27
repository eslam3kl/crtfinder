#!/usr/bin/env python 

'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
						 written by eslam akl - @eslam3kl 
								happy hacking bro <3 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[+] tool to find subdomains from crt.sh 
[+] extract triple subdomains, doubles subdoamins and single subdomains 
[+] extract the domain .com .net .org .etc 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
import requests 
from termcolor import colored 
import re 
import optparse 
import sys 
'''
print(colored("			   ___     _     ___ _           _ 								", "red", attrs=['bold']))          
print(colored("			  / __\ __| |_  / __(_)_ __   __| | ___ _ __ 					", "red", attrs=['bold']))	
print(colored("			 / / | '__| __|/ _\ | | '_ \ / _` |/ _ \ '__|					", "red", attrs=['bold']))
print(colored("			/ /__| |  | |_/ /   | | | | | (_| |  __/ |  					", "red", attrs=['bold'])) 
print(colored("			\____/_|   \__\/    |_|_| |_|\__,_|\___|_|						", "red", attrs=['bold']))   
print(" ")
print(colored("				     Coded by Eslam Akl 						   		   	", 'yellow', attrs=['bold']))
print(colored("			     Blog: https://medium.com/@eslam3kl 					       ", 'yellow'))
print(colored("			     GitHub: https://github.com/eslam3kl 						   ", 'yellow'))                                                                     
'''


#get the user input form the command option -u


def get_user_input():
	parser = optparse.OptionParser()
	parser.add_option("-u", "--target_url", dest="target_url", help="\tTarget URL (google.com, microsoft.com)")
	(options, arguments) = parser.parse_args()
	if not options.target_url:
		print(colored("\n[-] ", 'red') + colored("Target url doesn't exist, see --help for more info", 'cyan'))
		print(colored("[+] ", 'red') + colored("Usage: python ctrfinder.py -u target.com", 'cyan'))
		print(" ")
		raise SystemExit 
	else: 
		target_word = options.target_url.split(".")[0]
		#print(colored("[+] ", 'red') + colored("Getting the results from crt.sh with this keywords:", 'cyan', attrs=['bold']) + colored(" *." + target_word + ".com / " + target_word + ".*", "white"))
		#print(colored("[+] ", 'red') + colored("Start collecting info for: ", "cyan", attrs=["bold"]) + colored( target_word + "\n" , 'white' , attrs=[]))
		return options.target_url


#function to send request
def send_request(url): 
	request = requests.get(url) 
	return request

#function to filter the output of the conetnt 
def filter_crt(content_array): 
	subdomains = []
	for line in content_array: 
		if "<" in line: 
			line = re.findall('(?:)(.*?)<', line)[0]
			if line not in subdomains: 
				if word in line:
					if " " not in line: 
						if '@' not in line: 
							subdomains.append(line) 
		else: 
			if line not in subdomains: 
				if word in line:
					if " " not in line:
						if '@' not in line:
							subdomains.append(line)
	return subdomains


#function to extract the data from crt.sh 
def get_data(first_url, second_url): 
	first_response = send_request(first_url)
	second_response = send_request(second_url)
	first_content = first_response.text
	second_content = second_response.text
	first_subdomain_first_filter = re.findall('(?:<TD>)(.*?)</TD>', first_content) 
	second_subdomain_first_filter = re.findall('(?:<TD>)(.*?)</TD>', second_content)
	first_subdomain_second_filter = re.findall('(?:BR>)(.*?)<', first_content)
	second_subdomain_second_filter = re.findall('(?:BR>)(.*?)<', second_content)

	#calling filter function 
	first_output_first_filter = filter_crt(first_subdomain_first_filter)
	second_output_first_filter = filter_crt(second_subdomain_first_filter)
	first_output_second_filter = filter_crt(first_subdomain_second_filter)
	second_output_second_filter = filter_crt(second_subdomain_second_filter)
	#return the output 
	return first_output_first_filter, second_output_first_filter, first_output_second_filter, second_output_second_filter


#=======================[ Start from here ]=======================#

#get target domain from user input 
#input = sys.argv 
user_input = get_user_input()  # yahoo.com
domain = user_input # yahoo.com
if not domain: 
	print("Please enter the domain")
	raise SystemExit 
word = domain.split(".com")[0] #yahoo

first_url = 'https://crt.sh/?q=%25.' + domain # %.domain.com 
second_url = 'https://crt.sh/?q=' + word + '.%25' # domain.% 

#calling data function 
subdomains = get_data(first_url, second_url)
all_subdomains = []
for line in subdomains[0]: 
	if line not in all_subdomains: 
		all_subdomains.append(line)
for line in subdomains[1]: 
	if line not in all_subdomains: 
		all_subdomains.append(line)
for line in subdomains[2]: 
	if line not in all_subdomains: 
		all_subdomains.append(line) 
for line in subdomains[3]: 
	if line not in all_subdomains: 
		all_subdomains.append(line)

#loop to show the result at the terminal 
for line in all_subdomains: 
	try:
		if "*" in line: 
			line = line.split("*.")[1]
			print line 
		else: 
			print line 
	except: 
		pass
