# GoogD0rker 0.3 
# Merging changes into the main repo
# Follow RandomRobbie on the twitters, https://twitter.com/Random_Robbie
# Added in Sleep inbetween requests

from googlesearch import search
import os
import argparse
from random import randint
from time import sleep


# Add in argument options
parser = argparse.ArgumentParser(description='Which Domain to target')
parser.add_argument('-d', action='store', dest='domain',
                    help='type in the domain to target i.e target.com')

results = parser.parse_args()

# 
if results.domain == None:
	print ("Please enter the domain you wish to target: main.py -d target.com")
	exit()
else:
	site = results.domain

def clear_cookie():
	fo = open(".google-cookie", "w")
	fo.close()



def google_it (site,dork,filename):
	clear_cookie()
	out=open(filename,"a")
	for title in search(dork, stop=50):
            	print(title)
            	out.write(title)
            	out.write("\n")
	out.close()
	

	
	
	
	

print ("Finding Login Pages for "+site+"\n")
google_it (site,"site:"+site+" inurl:wp- OR inurl:plugin OR inurl:upload OR inurl:download","loginpage.txt")
sleep(randint(10,100))
print ("Finding Backdoors for "+site+"\n")
google_it (site,"site:"+site+" inurl:shell OR inurl:backdoor OR inurl:wso OR inurl:cmd OR shadow OR passwd OR boot.ini OR inurl:backdoor","backdoor.txt")
sleep(randint(10,100))
print ("Finding Install / Setup files for "+site+"\n")
google_it (site,"site:"+site+" inurl:readme OR inurl:license OR inurl:install OR inurl:setup OR inurl:config","setup_files.txt")
sleep(randint(10,100))
print ("Finding WORDPRESS PLUGINS/UPLOADS/DOWNLOADS for "+site+"\n")
google_it (site,"site:"+site+" inurl:wp- OR inurl:plugin OR inurl:upload OR inurl:download","wordpress.txt")
sleep(randint(10,100))
print ("Finding OPEN REDIRECTS for "+site+"\n")
google_it (site,"site:"+site+" inurl:redir OR inurl:url OR inurl:redirect OR inurl:return OR inurl:src=http OR inurl:r=http" ,"openredirect.txt")
sleep(randint(10,100))
print ("Finding FILES BY EXTENSION for "+site+"\n")
google_it (site,"site:"+site+" ext:cgi OR ext:php OR ext:asp OR ext:aspx OR ext:jsp OR ext:jspx OR ext:swf OR ext:fla OR ext:xml" ,"extentions.txt")
sleep(randint(10,100))
print ("Finding FIND DOCUMENTS BY EXTENSION for "+site+"\n")
google_it (site,"site:"+site+" ext:doc OR ext:docx OR ext:csv OR ext:pdf OR ext:txt OR ext:log OR ext:bak" ,"documents.txt")
sleep(randint(10,100))
print ("Finding FIND APACHE STRUTS RCE for "+site+"\n")
google_it (site,"site:"+site+" ext:action OR ext:struts OR ext:do" ,"struts.txt")
sleep(randint(10,100))
print ("Finding PASTEBIN POSTS FOR DOMAIN for "+site+"\n")
google_it (site,"site:pastebin.com "+site+"" ,"pastebin.txt")
sleep(randint(10,100))
print ("Finding EMPLOYEES ON LINKEDIN for "+site+"\n")
google_it (site,"site:linkedin.com employees "+site+"" ,"linkedin.txt")
sleep(randint(10,100))
print ("Finding Subdomains for "+site+"\n")
google_it (site,"site:*."+site+"" ,"subdomains.txt")
sleep(randint(10,100))
print ("Finding Sub-subdomains for "+site+"\n")
google_it (site,"site:*.*."+site+"" ,"sub-subdomains.txt")
sleep(randint(10,100))
print ("Finding PHPINFO Files for "+site+"\n")
google_it (site,"inurl:'/phpinfo.php' "+site+"" ,"phpinfo.txt")
sleep(randint(10,100))
print ("Finding Files containing passwords for"+site+"\n")
google_it (site,"intext:'connectionString' AND inurl:'web' AND ext:'config'")
sleep(randint(10,100))
print ("Finding .htaccess & sensitive fiels for "+site+"\n")
google_it (site,"inurl:'/phpinfo.php' OR inurl:'.htaccess' OR inurl:'/.git' "+site+" -github" ,"sensitive.txt")
sleep(randint(10,100))
google_it(site, "site:"+site, "inurl:callback")
time.sleep(5)
