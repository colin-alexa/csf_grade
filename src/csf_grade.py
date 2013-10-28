#!/usr/bin/python

import re, subprocess

nfile = open("/home/robcol15/Documents/csf_2013/grading/csf-data/github-ssh-remotes.txt")
for ssh_url in nfile:
 name = ssh_url[15:ssh_url.find('/')]
 
 subprocess.call(["mkdir", name])
 subprocess.call(["git", "clone", ssh_url.strip('\n'), name])
