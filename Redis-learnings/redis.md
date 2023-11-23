> Redis works with key pair values. It is a key-value store. It is an in-memory data structure store, used as a database, cache and message broker. 
> It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, 
> hyperloglogs, geospatial indexes with radius queries and streams. 
Store value with set <key> <value>
```bash
set name "John"
set lname "Doe"
```
Retrieve value with get <key>
```bash
get name
> "John"
```
Delete key with del <key>
```bash
del name lname
> 2  # number of keys deleted
```
Check if key exists with exists <key>
```bash
exists name
> 1  # 1 if key exists, 0 if key does not exist
```
Set key with expiration with expire <key> <time in seconds>
```bash
set name "John" ex 10  # time in seconds
set lname "Doe" px 10000  # time in milliseconds
```
Rename key with rename <oldkey> <newkey>
```bash
rename user:1 user:1:name
```
Type of key with type <key>
```bash
type name
> string
```
Check time to live with ttl <key>
```bash
ttl name
> 10  # time in seconds
pttl name # time in milliseconds
or
> -2  # if key does not exist
```
Persist key with persist <key>
```bash
persist name
> 1  # 1 if key exists, 0 if key does not exist
```
Select all keys with keys *
```bash
keys *
> 1) "name"
> 2) "lname"
```
Flush database with flushdb
```bash
flushdb
> OK
```
Key naming conventions
```bash
set user:1 "John"
set user:1:grouplist "admin,editor"
set user:2:grouplist "editor"
set user:3:grouplist "admin"
```
Keys pattern matching
```bash
user:??? # matches user:123, user:abc, user:xyz
user:*:grouplist # matches user:1:grouplist, user:2:grouplist, user:3:grouplist
h[ae]llo # matches hello and hallo, but not hillo 
h[^e]llo # matches hallo, hbllo, ... but not hello
h[a-b]llo # matches hallo and hbllo
```
shut down redis server
```bash
shutdown SAVE # save data to disk
shutdown NOSAVE # do not save data to disk
```

increment key with incr <key>
```bash
set counter 100
incr counter
> 101
```
increment key by value with incrby <key> <value>
same with incrbyfloat <key> <value>
```bash
set counter 100
incrby counter 10
> 110
incrbyfloat counter 10.5
> 110.5
```

decrement key with decr <key>
```bash
set counter 100
decr counter
> 99
```
decrement key by value with decrby <key> <value>
same with decrbyfloat <key> <value>
```bash
set counter 100
decrby counter 10
> 90
decrbyfloat counter 10.5
> 89.5
```

Append value to key with append <key> <value>
```bash
set name "John"
append name " Doe"
> 9  # length of string
get name
> "John Doe"
```

Set Range of string with setrange/replace <key> <offset> <value>
```bash
set name "John"
setrange name 3 "athan"
> 9  # length of string
get name
> "Jonathan"
```

Create json object
```bash
set user:1 "{\"name\":\"John\", \"age\":30}"
get user:1
> "{\"name\":\"John\", \"age\":30}"
```

Push list with lpush <key> <value>
```bash
lpush users "John"
lpush users "Jane"
lpush users "Jack"
get users
> 1) "Jack"
> 2) "Jane"
> 3) "John"
```
Push list with rpush <key> <value>
```bash
rpush users "John"
rpush users "Jane"
rpush users "Jack"
get users
> 1) "John"
> 2) "Jane"
> 3) "Jack"
```
List a range of values with lrange <key> <start> <stop>
```bash
lrange users 0 1 # list first two values
> 1) "John"
> 2) "Jane"
lrange users 0 -1 # list all values
> 1) "John"
> 2) "Jane"
> 3) "Jack"
```

List length with llen <key>
```bash
llen users
> 3
```

Pop item from list with lpop <key> and rpop <key>
```bash
lpop users # pop first item
> "John"
rpop users # pop last item
> "Jack"
```

Get all values of a key with getall <key>
```bash
getall users
> 1) "John"
> 2) "Jane"
> 3) "Jack"
```

Set value with hset <key> <field> <value>
```bash
hset user:1 name "John"
hset user:1 age 30
> 0  # 0 if field is new, 1 if field is updated
hset user:1 "email"
get user:1
> 1) "name"
> 2) "John"
> 3) "age"
> 4) "30"
> 5) "email"
```

Get value with hget <key> <field>
```bash
hgset user:1 name "John"
hget user:1 name
> "John"
```

Get value with key with hmget <key> <field1> <field2>
```bash
hset user:1 name "John"
hset user:1 age 30
hmget user:1 name age
> 1) "John"
> 2) "30"
```

Delete field with hdel <key> <field>
```bash
hset user:1 name "John"
hset user:1 age 30
hdel user:1 age name
> 2  # number of fields deleted
```

Check if field exists with hexists <key> <field>
```bash
hexists user:1 age name
> 1  # 1 if field exists, 0 if field does not exist
```

Get keys with hkeys <key>
```bash
hkeys user:1
> 1) "name"
> 2) "age"
```

Get values with hvals <key>
```bash
hvals user:1
> 1) "John"
> 2) "30"
```

Add set with sadd <key> <value>
```bash
sadd users "John"
sadd users "Jane"
sadd users "Jane"
> 2  # number of values added last record is ignored because it is a duplicate
```

Delete set with srem <key> <value>
```bash
srem users "John"
> 1  # number of values deleted
```

Members of set with smembers <key>
```bash
smembers users
> 1) "Jane"
```

Get random member of set with srandmember <key>
```bash
srandmember users 2
> 1) "Jane"
> 2) "John"
```

Move member from one set to another with smove <source> <destination> <member>
```bash
smove users admins "Jane"
> 1  # 1 if member is moved, 0 if member is not moved
```

Difference between two sets with sdiff <key1> <key2>
```bash
sdiff users admins
> 1) "John"
```

HyperLogLog is a probabilistic data structure used to count unique values in a set. 
```bash
pfadd users "John"
pfadd users "Jane"
pfadd users "Jane"
pfcount users
> 2  # number of unique values
```

Pub with publish <channel> <message>
```bash
publish notifications "Hello"
> 0  # number of subscribers
```
Sub with subscribe <channel>
```bash
subscribe notifications
> Reading messages... (press Ctrl-C to quit)
> 1) "subscribe"
> 2) "notifications"
> 3) (integer) 1
```

Dump key with dump <key>
```bash
dump users
> "\x00\x06\x00\x00\x00\x12\x00\x00\x00\"
```

Restore key with restore <key> <ttl> <serialized-value>
```bash
restore users 0 "\x00\x06\x00\x00\x00\x12\x00\x00\x00\"
> OK
```



