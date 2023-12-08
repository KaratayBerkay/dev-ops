### Inheritance

Inheritance is a concept from object-oriented databases. It opens up interesting new possibilities of database design.

Let's create two tables: A table cities and a table capitals. Naturally, capitals are also cities, 
so you want some way to show the capitals implicitly when you list all cities. If you're really clever you 
might invent some scheme like this:
```shell
CREATE TABLE capitals (
  name       text,
  population real,
  elevation  int,    -- (in ft)
  state      char(2)
);
 
```
```shell
CREATE TABLE non_capitals (
  name       text,
  population real,
  elevation  int     -- (in ft)
);
```
```shell
CREATE VIEW cities AS SELECT name, population, elevation FROM capitals
UNION
SELECT name, population, elevation FROM non_capitals;
```
This works OK as far as querying goes, but it gets ugly when you need to update several rows, for one thing.
A better solution is this:
```shell
CREATE TABLE cities (
  name       text,
  population real,
  elevation  int     -- (in ft)
);
```
```shell
CREATE TABLE capitals (
  state      char(2) UNIQUE NOT NULL
) INHERITS (cities);
```

```shell
SELECT name, elevation FROM cities WHERE elevation > 500;
```

```shell
   name    | elevation
-----------+-----------
 Las Vegas |      2174
 Mariposa  |      1953
(2 rows)
```
Here the ONLY before cities indicates that the query should be run over only the cities table, and not 
tables below cities in the inheritance hierarchy. Many of the commands that we have already discussed 
— SELECT, UPDATE, and DELETE — support this ONLY notation.

