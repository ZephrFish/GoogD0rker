#!/usr/bin/python3
# GoogD0rk3r 3.0
# Python 3 re-write of version 1.0

# Declare all the imports we need
import argparse
import sys
from googlesearch import search


# Define our arguments required, We'll need to specify our domain OR a file containing a list of domains
parser = argparse.ArgumentParser(description='GoogD0rker performs google dork queries to uncover information about a domain.')
parser.add_argument('-d', action='store', dest='domain', help='Supply a target domain i.e target.com')
#parser.add_argument('-i', action='store', dest='domainlist', help='Supply a file containing a list of domains i.e targets.txt')
parser.add_argument('-v','--verbose', action='store_true', help='Enable Verbose mode for debugging purposes')

# Execute the arguments defined
args = parser.parse_args()

def main():

    if args.domain == None:
        # Use sys.argv[0] here so we never have to update this line if we change the script name
        print("Please enter the domain you wish to target: "+ sys.argv[0] +" -d target.com")
        # -1 exit code error
        exit(-1)
    else:
        site = args.domain
    
    # This is where the results will be stored
    results_list = []

    # A keyed list of dorks
    dorks = {
        'site' : 'site:"'+site+'" inurl:"wp-" OR inurl:"plugin" OR inurl:"upload" OR inurl:"download"',
        'php' : 'inurl:"?id=" AND filetype:"php"',
        'loginPage': "loginpage.txt"
    }

    # Loop over the dict of dorks
    for dork in dorks:

        # Verbose output
        if args.verbose :
            print("Currently Running : " + dorks[dork])

        # Perform the google search
        search_results = search(dorks[dork], tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)
        
        # Loop over the search results and add them to the results_list variable
        for i in search_results:
            results_list.append(i)
    # Print the results_list
    print(results_list)

if __name__ == '__main__':
    main()
