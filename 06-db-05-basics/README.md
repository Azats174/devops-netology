### Домашнее задание к занятию "6.5. Elasticsearch"

### Задача 1

Docker file:
```
FROM centos:7                                                                                                                                          
LABEL ElasticSearch Lab 7.11 \                                                                                                                         
    (c)Safiullin Azat \
name="elasticsearch_7.11" 

ENV PATH=/usr/lib:/usr/lib/jvm/jre-11/bin:$PATH

RUN yum install java-11-openjdk -y 
RUN yum install wget -y 

RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.11.1-linux-x86_64.tar.gz \
    && wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.11.1-linux-x86_64.tar.gz.sha512 
RUN yum install perl-Digest-SHA -y 
RUN shasum -a 512 -c elasticsearch-7.11.1-linux-x86_64.tar.gz.sha512 \ 
    && tar -xzf elasticsearch-7.11.1-linux-x86_64.tar.gz \
    && yum upgrade -y
    
ADD elasticsearch.yml /elasticsearch-7.11.1/config/
ENV JAVA_HOME=/elasticsearch-7.11.1/jdk/
ENV ES_HOME=/elasticsearch-7.11.1
RUN groupadd elasticsearch \
    && useradd -g elasticsearch elasticsearch
    
RUN mkdir /var/lib/logs \
    && chown elasticsearch:elasticsearch /var/lib/logs \
    && mkdir /var/lib/data \
    && chown elasticsearch:elasticsearch /var/lib/data \
    && chown -R elasticsearch:elasticsearch /elasticsearch-7.11.1/
RUN mkdir /elasticsearch-7.11.1/snapshots &&\
    chown elasticsearch:elasticsearch /elasticsearch-7.11.1/snapshots
    
USER elasticsearch
CMD ["/usr/sbin/init"]
CMD ["/elasticsearch-7.11.1/bin/elasticsearch"]
```
образ на dockerhub 
```
docker image pull  azath174/netology:elactic
```



elasticsearch.yml:
```
cluster.name: netology_test
discovery.type: single-node
path.data: /var/lib/data
#
path.logs: /var/lib/logs
path.repo: /elasticsearch-7.11.1/snapshots
network.host: 0.0.0.0
discovery.seed_hosts: ["127.0.0.1", "[::1]"]
```
запуск  контэйнера
```
docker run -d -e ES_JAVA_POTS="-Xms256m -Xmx256m" -e"discovery.type=single-node" -p 9200:9200 -p 9300:9300 azath174/netology:elactic 
```
ответ elactic
```
azat@nout2:~/netology/06-db-05$ curl localhost:9200
{
  "name" : "6da9271d094b",
  "cluster_name" : "netology_test",
  "cluster_uuid" : "fCWKpHyEQIOuhmYYgWgh4w",
  "version" : {
    "number" : "7.11.1",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "ff17057114c2199c9c1bbecc727003a907c0db7a",
    "build_date" : "2021-02-15T13:44:09.394032Z",
    "build_snapshot" : false,
    "lucene_version" : "8.7.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

### Задача 2

Рботаем с  этим контайнером

Создал индексы:
```
curl -X PUT localhost:9200/ind-1 -H 'Content-Type: application/json' -d'{ "settings": { "number_of_shards": 1,  "number_of_replicas": 0 }}'
curl -X PUT localhost:9200/ind-2 -H 'Content-Type: application/json' -d'{ "settings": { "number_of_shards": 2,  "number_of_replicas": 1 }}'
curl -X PUT localhost:9200/ind-3 -H 'Content-Type: application/json' -d'{ "settings": { "number_of_shards": 4,  "number_of_replicas": 2 }}'    
```
Список индексов:
```
$ curl -X GET 'http://localhost:9200/_cat/indices?v' 
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   ind-1 GsWVsEodQeq71Eehb6Txfg   1   0          0            0       208b           208b
yellow open   ind-3 kyfE2lpYR4KpIPzvmIEj6A   4   2          0            0       832b           832b
yellow open   ind-2 w7d7vBSISeCdEfYQu0Thfg   2   1          0            0       416b           416b

``` 
Статус индексов:
```
$ curl -X GET 'http://localhost:9200/_cluster/health/ind-1?pretty' 
{
  "cluster_name" : "netology_test",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 1,
  "active_shards" : 1,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 0,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 100.0
}

$ curl -X GET 'http://localhost:9200/_cluster/health/ind-2?pretty' 
{
  "cluster_name" : "netology_test",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 2,
  "active_shards" : 2,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 2,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 41.17647058823529
}

$ curl -X GET 'http://localhost:9200/_cluster/health/ind-3?pretty' 
{
  "cluster_name" : "netology_test",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 4,
  "active_shards" : 4,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 8,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 41.17647058823529
}
```
Статус кластера:
```
$ curl -XGET localhost:9200/_cluster/health/?pretty=true
{
  "cluster_name" : "netology_test",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 7,
  "active_shards" : 7,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 10,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 41.17647058823529
}
```
Удалил индексы:
```
$ curl -X DELETE 'http://localhost:9200/ind-1?pretty' 
{
  "acknowledged" : true
}
$ curl -X DELETE 'http://localhost:9200/ind-2?pretty' 
{
  "acknowledged" : true
}
$ curl -X DELETE 'http://localhost:9200/ind-3?pretty' 
{
  "acknowledged" : true
}
```
Список  индексов
```
$ curl -X GET 'http://localhost:9200/_cat/indices?v'
health status index uuid pri rep docs.count docs.deleted store.size pri.store.size
```
индексы в статусе Yellow потому что у них указано число реплик, а по факту нет других серверов, соответсвено реплицировать некуда.



### Задание 3

Путь для снапшота мы  уже   указали в  кнфиге  при создании докера
Зарегестрировал  путь до каталога с снапшотами

```
curl -XPOST localhost:9200/_snapshot/netology_backup?pretty -H 'Content-Type: application/json' -d'{"type": "fs", "settings": { "location":"/elasticsearch-7.11.1/snapshots" }}'
{
  "acknowledged" : true
}
```
вывод снапшотов
```
curl http://localhost:9200/_snapshot/netology_backup?pretty 
{
  "netology_backup" : {
    "type" : "fs",
    "settings" : {
      "location" : "/elasticsearch-7.11.1/snapshots"
    }
  }
}

```
Создал индекс test с 0 реплик и 1 шардом
```
curl -X PUT localhost:9200/test -H 'Content-Type: application/json' -d'{ "settings": { "number_of_shards": 1,  "number_of_replicas": 0 }}'
```
```
curl  http://localhost:9200/test?pretty 
{
  "test" : {
    "aliases" : { },
    "mappings" : { },
    "settings" : {
      "index" : {
        "routing" : {
          "allocation" : {
            "include" : {
              "_tier_preference" : "data_content"
            }
          }
        },
        "number_of_shards" : "1",
        "provided_name" : "test",
        "creation_date" : "1647671443016",
        "number_of_replicas" : "0",
        "uuid" : "keSaKfMaRFKcNJ-9Pfbw1Q",
        "version" : {
          "created" : "7110199"
        }
      }
    }
  }
}
```
Создал snapshot состояния кластера elasticsearch
```
curl -X PUT localhost:9200/_snapshot/netology_backup/elasticsearch?wait_for_completion=true
{"snapshot":{"snapshot":"elasticsearch","uuid":"W18zCbOQQxOCCrR2aJJiOQ","version_id":7110199,"version":"7.11.1","indices":["test"],"data_streams":[],"include_global_state":true,"state":"SUCCESS","start_time":"2022-03-19T06:37:29.664Z","start_time_in_millis":1647671849664,"end_time":"2022-03-19T06:37:29.664Z","end_time_in_millis":1647671849664,"duration_in_millis":0,"failures":[],"shards":{"total":1,"failed":0,"successful":1}}}
```
Листинг файлов
```
docker exec fd5ea667ee07  ls  /elasticsearch-7.11.1/snapshots
index-0
index.latest
indices
meta-W18zCbOQQxOCCrR2aJJiOQ.dat
snap-W18zCbOQQxOCCrR2aJJiOQ.dat
```
Список  индексев
```
curl -X GET 'http://localhost:9200/_cat/indices?v' 
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test  keSaKfMaRFKcNJ-9Pfbw1Q   1   0          0            0       208b           208b
```
Удалил индекс тест
```
curl -X DELETE 'http://localhost:9200/test?pretty'
{
  "acknowledged" : true
}
```
Создал индекс тест-2
```
curl -X PUT localhost:9200/test-2?pretty -H 'Content-Type: application/json' -d'{ "settings": { "number_of_shards": 1,  "number_of_replicas": 0 }}'
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "test-2"
}
```
Список индексев
```
 curl -X GET 'http://localhost:9200/_cat/indices?v' 
health status index  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test-2 7LmrEBYZR8Wz-ha28UDM5g   1   0          0            0       208b           208b
```
Востановил индекс
```
curl -X POST localhost:9200/_snapshot/netology_backup/elasticsearch/_restore?pretty -H 'Content-Type: application/json' -d'{"include_global_state":true}'
{
  "accepted" : true
}
```
Список  индексев
```
curl -X GET 'http://localhost:9200/_cat/indices?v' 
health status index  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test-2 7LmrEBYZR8Wz-ha28UDM5g   1   0          0            0       208b           208b
green  open   test   Og8bHVp8Rnu0mmom8dAZoQ   1   0          0            0       208b           208b
```




