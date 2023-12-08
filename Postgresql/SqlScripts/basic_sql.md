# Sql Commands

Create Tables
```shell
CREATE TABLE weather (
        city      varchar(80) references cities(name),
        temp_lo   int,
        temp_hi   int,
        prcp      real,
        date      date
);
```

```shell
CREATE TABLE cities (
        name     varchar(80) primary key,
        location point
);
```
Insert > Tables
```shell
INSERT INTO weather VALUES ('Berkeley', 45, 53, 0.0, '1994-11-28');
```

```shell
ERROR:  insert or update on table "weather" violates foreign key constraint "weather_city_fkey"
DETAIL:  Key (city)=(Berkeley) is not present in table "cities".
```


Views 
```shell
CREATE VIEW myview AS 
SELECT name, temp_lo, temp_hi, prcp, date, location
FROM weather, cities WHERE city = name;
SELECT * FROM myview;
```

