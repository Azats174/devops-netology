### Как сдавать задания

Вы уже изучили блок «Системы управления версиями», и начиная с этого занятия все ваши работы будут приниматься ссылками на .md-файлы, размещённые в вашем публичном репозитории.

Скопируйте в свой .md-файл содержимое этого файла; исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-03-yaml/README.md). Заполните недостающие части документа решением задач (заменяйте `???`, ОСТАЛЬНОЕ В ШАБЛОНЕ НЕ ТРОГАЙТЕ чтобы не сломать форматирование текста, подсветку синтаксиса и прочее, иначе можно отправиться на доработку) и отправляйте на проверку. Вместо логов можно вставить скриншоты по желани.

# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис
Недлстаточно ковычек в  9 строке.
"ip" : 71.78.22.43


## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python

azat@nout2:~/netology/devops-netology/04-script-03-yaml$ cat  script_4_3_2.py 
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

### Вывод скрипта при запуске при тестировании:
```
azat@nout2:~/netology/devops-netology/04-script-03-yaml$ ./script_4_3_2.py 
*** start script ***
{'drive.google.com': '0.0.0.0', 'mail.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}
********************
```

### json-файл(ы), который(е) записал ваш скрипт:
```json

azat@nout2:~/netology/devops-netology/04-script-03-yaml$ more services_conf.json 
[{"drive.google.com": "142.250.74.142"}, {"mail.google.com": "142.250.74.142"}, {"google.com": "142.250.74.142"}]
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
azat@nout2:~/netology/devops-netology/04-script-03-yaml$ more services_conf.yaml 
---
- {drive.google.com: 142.250.74.142}
- {mail.google.com: 142.250.74.142}
- {google.com: 142.250.74.142}
...

```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

### Ваш скрипт:
```python
???
```

### Пример работы скрипта:
???

