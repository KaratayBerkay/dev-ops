## config commands

Calculate conf of postgres
https://pgtune.leopard.in.ua/

```markdown
# DB Version: 16 | OS Type: linux | DB Type: web | Total Memory (RAM): 16 GB | CPUs num: 4
# Connections num: 100 | Data Storage: ssd

max_connections = 100
shared_buffers = 4GB
effective_cache_size = 12GB
maintenance_work_mem = 1GB
checkpoint_completion_target = 0.9
wal_buffers = 16MB
default_statistics_target = 100
random_page_cost = 1.1
effective_io_concurrency = 200
work_mem = 20971kB
huge_pages = off
min_wal_size = 1GB
max_wal_size = 4GB
max_worker_processes = 4
max_parallel_workers_per_gather = 2
max_parallel_workers = 4
max_parallel_maintenance_workers = 2
```


```shell
show config_file;
```
```shell
                 config_file                  
----------------------------------------------
 /opt/bitnami/postgresql/conf/postgresql.conf
(1 row)
```

```shell
show max_connections;
```

```shell
 max_connections 
-----------------
 100
(1 row)
```

```shell
show work_mem;
```

```shell
 work_mem 
----------
 4MB
(1 row)
```

```shell
show shared_buffers;
```

```shell
 shared_buffers 
----------------
 128MB
(1 row)
```

```shell
show shared_memory_size;
```

```shell
 shared_memory_size 
--------------------
 143MB
(1 row)
```

```shell
select * from pg_stat_user_tables;
```

```shell
SELECT pg_size_pretty(pg_database_size('postgres'));
```

```shell
explain analyze select * from user_service_user;
```

```shell
                                                   QUERY PLAN                                                   
----------------------------------------------------------------------------------------------------------------
 Seq Scan on user_service_user  (cost=0.00..10.40 rows=40 width=1996) (actual time=0.019..0.020 rows=2 loops=1)
 Planning Time: 0.399 ms
 Execution Time: 0.038 ms
(3 rows)
```

Extensions
1. pg_stat_statements
2. PostGIS
3. ElasticSearch
4. Postgres_fdw
5. TimescaleDB
6. PostPic
7. IntArray
8. Pgsphere
9. pg_cron



