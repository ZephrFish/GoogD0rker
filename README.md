# GoogD0rker

## About
GoogD0rker is a tool for firing off google dorks against a target domain, it is purely for OSINT against a specific target domain. This will output all the google results for each of the tasks so you can hopefully find a vunerability. A 503 error means you need a new IP as google knows you're up to something!  This will output the results to files and then you can browse and see what you have found.

### Setup
Install the pre-reqs which are the google library for python, also install python if you haven't already.
`pip install -r rerquirements`

### Usage

*This will work on any unix machine*

`GoogD0rker.py -d example.com`

### Coming Soon 

- Able to add custom d0rks
- Prettier error handling
