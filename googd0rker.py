#!/usr/bin/python3
# GoogD0rker 2.0
# Full python 3 re-write to correct issues
# Added in Sleep inbetween requests and pause inbetween queries to correct the too many requests error
# App will only search for first 50 pages, if you want more change line 42 to none and line 43 to 5.0
# Note the too many requests error still happens some times 

from googlesearch import search
import os
import argparse
from random import randint
from time import sleep
import time


# Add in argument options
parser = argparse.ArgumentParser(description='GoogD0rker performs google dork queries to uncover information about a domain.')
parser.add_argument('-d', action='store', dest='domain', help='type in the domain to target i.e target.com')

results = parser.parse_args()

if results.domain == None:
	print("Please enter the domain you wish to target: googd0rker.py -d target.com")
	exit()
else:
	site = results.domain

def clear_cookie():
	fo = open(".google-cookie", "w")
	fo.close()



def d0rkit (site,dork,filename):
	clear_cookie()
	out=open(filename,"a")
	for title in search(
		dork, 
		tld = 'com',  # The top level domain
        lang = 'en',  # The language
        num = 10,     # Number of results per page
        start = 0,    # First result to retrieve
        stop = 50,  # Last result to retrieve
        pause = 2.0,  # This is required to bypass google's limiting unfortunately
		):
            	print(title)
            	out.write(title)
            	out.write("\n")
	out.close()
	

def main():

	print("Finding Login Pages for "+site+"\n")
	d0rkit (site,"site:"+site+" inurl:wp- OR inurl:plugin OR inurl:upload OR inurl:download","loginpage.txt")
	sleep(randint(10,100))

	print("Finding Backdoors for "+site+"\n")
	d0rkit (site,"site:"+site+" inurl:shell OR inurl:backdoor OR inurl:wso OR inurl:cmd OR shadow OR passwd OR boot.ini OR inurl:backdoor","backdoor.txt")
	sleep(randint(10,100))

	print("Finding Install / Setup files for "+site+"\n")
	d0rkit (site,"site:"+site+" inurl:readme OR inurl:license OR inurl:install OR inurl:setup OR inurl:config","setup_files.txt")
	sleep(randint(10,100))

	print("Finding WORDPRESS PLUGINS/UPLOADS/DOWNLOADS for "+site+"\n")
	d0rkit (site,"site:"+site+" inurl:wp- OR inurl:plugin OR inurl:upload OR inurl:download","wordpress.txt")
	sleep(randint(10,100))

	print("Finding OPEN REDIRECTS for "+site+"\n")
	d0rkit (site,"site:"+site+" inurl:redir OR inurl:url OR inurl:redirect OR inurl:return OR inurl:src=http OR inurl:r=http" ,"openredirect.txt")
	sleep(randint(10,100))

	print("Finding FILES BY EXTENSION for "+site+"\n")
	d0rkit (site,"site:"+site+" ext:cgi OR ext:php OR ext:asp OR ext:aspx OR ext:jsp OR ext:jspx OR ext:swf OR ext:fla OR ext:xml" ,"extentions.txt")
	sleep(randint(10,100))

	print("Finding FIND DOCUMENTS BY EXTENSION for "+site+"\n")
	d0rkit (site,"site:"+site+" ext:doc OR ext:docx OR ext:csv OR ext:pdf OR ext:txt OR ext:log OR ext:bak" ,"documents.txt")
	sleep(randint(10,100))

	print("Finding FIND APACHE STRUTS RCE for "+site+"\n")
	d0rkit (site,"site:"+site+" ext:action OR ext:struts OR ext:do" ,"struts.txt")
	sleep(randint(10,100))

	print("Finding PASTEBIN POSTS FOR DOMAIN for "+site+"\n")
	d0rkit (site,"site:pastebin.com "+site+"" ,"pastebin.txt")
	sleep(randint(10,100))

	print("Finding EMPLOYEES ON LINKEDIN for "+site+"\n")
	d0rkit (site,"site:linkedin.com employees "+site+"" ,"linkedin.txt")
	sleep(randint(10,100))

	print("Finding Subdomains for "+site+"\n")
	d0rkit (site,"site:*."+site+"" ,"subdomains.txt")
	sleep(randint(10,100))

	print("Finding Sub-subdomains for "+site+"\n")
	d0rkit (site,"site:*.*."+site+"" ,"sub-subdomains.txt")
	sleep(randint(10,100))

	print("Finding PHPINFO Files for "+site+"\n")
	d0rkit (site,"inurl:'/phpinfo.php' "+site+"" ,"phpinfo.txt")
	sleep(randint(10,100))

	print("Finding Files containing passwords for"+site+"\n")
	d0rkit (site,"intext:'connectionString' AND inurl:'web' AND ext:'config'", "passwords.txt")
	sleep(randint(10,100))

	print("Finding .htaccess & sensitive fiels for "+site+"\n")
	d0rkit (site,"inurl:'/phpinfo.php' OR inurl:'.htaccess' OR inurl:'/.git' "+site+" -github" ,"sensitive.txt")
	sleep(randint(10,100))

	time.sleep(5)

if __name__ == '__main__':
    main()
