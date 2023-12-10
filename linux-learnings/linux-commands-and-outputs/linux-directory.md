# Binary Directory

```shell
/bin
```
Essential Executables
<List of executable files that run by system>
```shell
-rwxr-xr-x  1 root root          79 May 29  2023  pydoc3.10
lrwxrwxrwx  1 root root          13 Aug 18  2022  pygettext3 -> pygettext3.10
-rwxr-xr-x  1 root root       24195 Aug  1  2022  pygettext3.10
lrwxrwxrwx  1 root root          10 Aug 18  2022  python3 -> python3.10
-rwxr-xr-x  1 root root     5912968 May 29  2023  python3.10
lrwxrwxrwx  1 root root          34 May 29  2023  python3.10-config -> x86_64-linux-gnu-python3.10-config
```

```shell
/sbin
```
System Binaries
Essential Executables for super user (root)
```shell
/usr/local/bin
```
directory of where locally compiled binaries by a package manager
```shell
echo $PATH
```
```shell
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```
where system local variable path is registered @ 
```shell
which apt
```
```shell
/usr/bin/apt
```

target binary path of executable
```shell
/usr/bin/apt
```

```shell
/etc
```
ET Cetera Editable Text Config
User data directories
```shell
/home/<user>
```

Boot files 
```shell
/boot
```

Directory to boot systems Device file
```shell
ls dev/ | head -5
```
```shell
autofs
block
bsg
btrfs-control
bus
```

Optional or add-on software
```shell
/opt
```

Variables files | logs, caches
```shell
/var
```

temporary files
```shell
/tmp
```

A temporary file that system keep track of actions happening on kernel
```shell
/proc
```

