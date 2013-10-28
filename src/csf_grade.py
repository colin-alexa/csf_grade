#!/usr/bin/python

## The intent of this program is to automate grading of
##  specific programming assignments based on expected output.
## When complete, the program will:
## - update the student git repos
## - find the correct homework program
## - run the program
## - redirect the output to a file
## - perform some basically intelligent comparison
##    between that file and an answer key
## Obviously, this approach can only work for assignments which
##  require minimal user input. This particular program requires
##  there to be absolutely none, but it wouldn't be very difficult
##  to modify it for some slight automated interaction. 
##  (An exercise for the reader ^_^)

### TODO:
### - glob.glob search for supplied filename

import re, subprocess, glob
from sys import argv, exit


path_to_grading = "/home/robcol15/Documents/csf_2013/grading/"
assignment = raw_input("name of file to grade: ")
path_to_key = "/home/robcol15/Documents/csf_2013/grading/keys/hw" \
                + assignment + ".key"

subprocess.call(["git", "clone", "git@github.com:ppham/csf-data.git", path_to_grading + "csf-data"])
ssh_remotes = "/home/robcol15/Documents/csf_2013/grading/csf-data/github-ssh-remotes.txt"


nfile = open(ssh_remotes)
def overclone():
 subprocess.call(["rm","-rf",path_to_grading+"*"])
 for ssh_url in nfile:
  name = ssh_url[15:ssh_url.find('/')]
  path_to_repo = path_to_grading + name
  subprocess.call(["mkdir", path_to_repo])
  subprocess.call(["git", "clone", ssh_url.strip('\n'), path_to_repo])
 
  hwx = glob.glob(path_to_repo + 'hw' + assignment)
  ## run assignment program >> tmp.o
  ## Read answer key
  ## find relevant answers in tmp.o (^_^)
  ## compare them
  ## generate grade


##Implement this
def update():
 print "not supported yet!"

def bad_exit(e="uknown error"):
 exit("Error: e")
 
fdict = {'o': overclone, 'u': update}

def main():
 if len(argv) > 1:
  options = argv[0].split()[1:]
  for opt in options:
   fdict.get(opt, bad_exit)()
 elif len(argv) == 1:
  overclone()
 else:
  bad_exit()

main()
