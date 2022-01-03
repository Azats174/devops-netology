#!/usr/bin/env python3

import os
import sys

pwd = os.getcwd()

if len(sys.argv)>=2:
    cmd = sys.argv[1]

bash_command = ["cd "+pwd, "git status 2>&1"]

result_os = os.popen(' && '.join(bash_command)).read()
#is_change = False
for result in result_os.split('\n'):
    if result.find('fatal') != -1:
        print('This directory'+pwd+' is  not git directory')    
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified: ', '')
        prepare_result = prepare_result.replace(' ', '') 
        print(pwd+'/'+prepare_result)
