> Postgres sql terminal commands

Run service Docker .yml
```yml
services:

  postgres-db:
    image: 'bitnami/postgresql:latest'
    ports:
      - 5432:5432
    restart: always
    container_name: postgres-db
    environment:
      - POSTGRESQL_USERNAME=evyosdatauser
      - POSTGRESQL_PASSWORD=KIIVCo2S5Z1AfxlruFsUonsKg1FABd5he9w7DTuF26K0qnXE5xXDzfUzlNDlj1H9
      - POSTGRESQL_DATABASE=evyosdatastore
    volumes:
      - postgresql_master_data:/bitnami/postgresql

volumes:
  postgresql_master_data:
```

Get into postgres api with user and database name
```bash
psql -U <$POSTGRESQL_USERNAME> <$POSTGRESQL_DATABASE>
```
On Terminal Enter password
```shell
Password for user evyosdatauser: <POSTGRESQL_PASSWORD>
```

Get list of database @db
```
\l
```
Output:
```shell
List of databases
      Name      |     Owner     | Encoding | Locale Provider |   Collate   |    Ctype    | ICU Locale | ICU Rules |        Access privileges        
----------------+---------------+----------+-----------------+-------------+-------------+------------+-----------+---------------------------------
 POSTGRESQL_DATABASE | POSTGRESQL_USERNAME | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | =Tc/POSTGRESQL_USERNAME              +
                     |                     |          |                 |             |             |            |           | POSTGRESQL_USERNAME=CTc/POSTGRESQL_USERNAME
 postgres            | postgres            | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | 
 template0           | postgres            | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | =c/postgres                    +
                     |                     |          |                 |             |             |            |           | postgres=CTc/postgres
 template1           | postgres            | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | =c/postgres                    +
                     |                     |          |                 |             |             |            |           | postgres=CTc/postgres
(4 rows)
```
Check connection info
```
\conninfo
```
Output:
```shell
You are connected to database "evyosdatastore" as user "evyosdatauser" via socket in "/tmp" at port "5432".
```
List Users with \dn
```
\dn
```
Output:
```shell
List of schemas
  Name  |     Owner     
--------+---------------
 public | evyosdatauser
(1 row)
```

List database info and relations
```
\dt+
```
Output:
```shell
Schema |      Name       | Type  |     Owner     | Persistence | Access method |    Size    | Description 
--------+-----------------+-------+---------------+-------------+---------------+------------+-------------
 public | alembic_version | table | evyosdatauser | permanent   | heap          | 0 bytes    | 
 public | cars            | table | evyosdatauser | permanent   | heap          | 8192 bytes | 
(2 rows)
```




