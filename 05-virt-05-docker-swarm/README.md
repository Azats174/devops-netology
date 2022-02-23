Задача 1

Дайте письменые ответы на следующие вопросы:

  В чём отличие режимов работы сервисов в Docker Swarm кластере: replication и global?
        
    Replication режим это значит  запуск идентичных задач. Несколько задач может исполняться на  одной ноде. 
    Например, я запустил сервис HTTP с тремя репликами, 
    каждая из которых обслуживает один и тот же контент. И нужно указать число реплик.
    
    Global режим это  когда  запускается одна задача  на  одной ноде.  
    Глобальный сервис — это сервис, который запускает одну задачу на каждой ноде.
    Предварительно заданного количества задач нет. Каждый раз, когда вы добавляете ноду в swarm, 
    оркестратор создает задачу, а планировщик назначает задачу новой ноде. Например это может быть  
    агенты мониторинга.
    
   Какой алгоритм выбора лидера используется в Docker Swarm кластере?
    
    Для выбора лидера используеться алгоритм Raft. Raft – алгоритм, использующийся для решения задач нахождения консенсуса
    в сети ненадёжных вычислений.
    
   Что такое Overlay Network?
    
    Overlay-сеть  это сеть, которую могут использовать контейнеры в разных физических хостах swarm-кластера.
  
Задание 2

>root@node01 ~]# docker node ls
>ID                            HOSTNAME             STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
>p9xm33dao0trspqbnqdupvua7 *   node01.netology.yc   Ready     Active         Leader           20.10.12
>pbzornfdvemypke8mi0ksz22     node02.netology.yc   Ready     Active         Reachable        20.10.12
>gir43n60bxl8jjafaafn2jhrt     node03.netology.yc   Ready     Active         Reachable        20.10.12
>m70str5ksimr4mlglodusl9mb     node04.netology.yc   Ready     Active                          20.10.12
>khtys3r1tls9y7nb58q8g80t2     node05.netology.yc   Ready     Active                          20.10.12
>strxb8pl1ljooargqu7vxk19b     node06.netology.yc   Ready     Active                          20.10.12

Задание 3

[root@node01 ~]# docker service ls
ID             NAME                                MODE         REPLICAS   IMAGE                                          PORTS
yyg2lt1wzptm   swarm_monitoring_alertmanager       replicated   1/1        stefanprodan/swarmprom-alertmanager:v0.14.0    
zltk4274azk1   swarm_monitoring_caddy              replicated   1/1        stefanprodan/caddy:latest                      *:3000->3000/tcp, *:9090->9090/tcp, *:9093-9094->9093-9094/tcp
i7tfezrb86tc   swarm_monitoring_cadvisor           global       6/6        google/cadvisor:latest                         
q299gdzks67j   swarm_monitoring_dockerd-exporter   global       6/6        stefanprodan/caddy:latest                      
g1pddm7pbmoq   swarm_monitoring_grafana            replicated   1/1        stefanprodan/swarmprom-grafana:5.3.4           
jcmww9xdg3hw   swarm_monitoring_node-exporter      global       6/6        stefanprodan/swarmprom-node-exporter:v0.16.0   
k9eqvq6go7u3   swarm_monitoring_prometheus         replicated   1/1        stefanprodan/swarmprom-prometheus:v2.5.0       
qcxk8a53a9t0   swarm_monitoring_unsee              replicated   1/1        cloudflare/unsee:v0.8.0  
