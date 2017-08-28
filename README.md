# GoogD0rker

## About
GoogD0rker is a tool for firing off google dorks against a target domain, it is purely for OSINT against a specific target domain. 
It is split into two versions, a bash script designed for OSX and a python script designed to be cross platform.

`GoogD0rker-OSX.sh` is designed for OSX, if you want to tweak it for Linux simply use sed: `sed 's/open/newbrowser/g' googd0rker > googd0rker-newbrowser`. It is modified from goohak by [crowdshield](https://github.com/1N3/Goohak).

### GoogD0rker-TXT

GoogD0rker-TXT was written by [txt3rob](https://github.com/txt3rob/bugbountydork) has been merged into this repo to keep continuity, changes will be added to this over time to account for extra D0rks and features.

### GoogD0rker-TXT - Setup
Install the pre-reqs which are the google library for python, also install python if you haven't already.
`pip install google`

### GoogD0rker-TXT - Info
This will output all the google results for each of the tasks so you can hopefully find a vunerability. A 503 error means you need a new IP as google knows you're up to something!  This will output the results to files and then you can browse and see what you have found.

### GoogD0rker-TXT - Usage

*This will work on any unix machine*

`googD0rker-txt.py -d example.com`

## GoogD0rker Shell Script

*Note this will only work on OSX, as it was written as a quick PoC tool*

`/googd0rker.sh domain.com`

