#!/usr/bin/env python3

import socket as s
import time as t
import datetime as dt
import json
import yaml


# set variables
i = 1
wait = 2 #  check interval
srv = {'drive.google.com':'0.0.0.0', 'mail.google.com':'0.0.0.0', 'google.com':'0.0.0.0'}
init = 0
fpath = "/home/azat/netology/devops-netology/04-script-03-yaml/" # path  to  config 
flog = "/tmp/error.log" # path logs

# start script workflow
print('*** start script ***')
print(srv)
print('********************')

while 1 == 1 : #  for unlimited loop , else  set  i >= count  iterations
  for host in srv:
    is_error = False
    ip = s.gethostbyname(host)
    if ip != srv[host]:
      if i==1 and init !=1: 
        is_error=True
        #   error different files
        with open(flog,'a') as fl:
          print(str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +' [ERROR] ' + str(host) +' IP mistmatch: '+srv[host]+' '+ip,file=fl)

        # json
        with open(fpath+host+".json",'w') as jsf:
          json_data= json.dumps({host:ip})
          jsf.write(json_data)
        # yaml
        with open(fpath+host+".yaml",'w') as ymf:
          yaml_data= yaml.dump([{host : ip}],explicit_start=True,explicit_end=True)
          ymf.write(yaml_data)
    #  error one files
    if is_error:
      data = []
      for host in srv:
        data.append({host:ip})
      with open(fpath+"services_conf.json",'w') as jsf:
        json_data= json.dumps(data)
        jsf.write(json_data)
      with open(fpath+"services_conf.yaml",'w') as ymf:
        yaml_data= yaml.dump(data,explicit_start=True,explicit_end=True)
        ymf.write(yaml_data)
      srv[host]=ip
  #print(i) #  debug step iterations 
  i+=1 # set comment for unlimit loop
  if i >=20 : # count iteration for debug 
    break
  t.sleep(wait) 
