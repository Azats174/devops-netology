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
