#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/devops-netology", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
#print(result_os)
#is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        test3 = os.getcwd()
        #test =  os.path.abspath('prepare_result')
        #test2 = os.getcwd('prepare_result')
        #print(test2)
        print(test3+'/'+prepare_result)
#        break
