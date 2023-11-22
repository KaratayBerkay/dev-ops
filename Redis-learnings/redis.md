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



