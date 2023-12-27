## Nginx

```shell
cd /etc/nginx
ls -l
```

```shell
cat /etc/passwd
cat /proc/cpuinfo
ls -l /var/log/nginx/
```shell
-rw-r----- 1 www-data adm  0 Ara 27 13:58 access.log
-rw-r----- 1 www-data adm 78 Ara 27 13:58 error.log
```

```shell
drwxr-xr-x   2 root root  4096 May 30  2023 conf.d
-rw-r--r--   1 root root  1125 May 30  2023 fastcgi.conf
-rw-r--r--   1 root root  1055 May 30  2023 fastcgi_params
-rw-r--r--   1 root root  2837 May 30  2023 koi-utf
-rw-r--r--   1 root root  2223 May 30  2023 koi-win
-rw-r--r--   1 root root  3957 May 30  2023 mime.types
drwxr-xr-x   2 root root  4096 May 30  2023 modules-available
drwxr-xr-x   2 root root  4096 Ara 27 13:58 modules-enabled
-rw-r--r--   1 root root  1447 May 30  2023 nginx.conf
-rw-r--r--   1 root root   180 May 30  2023 proxy_params
-rw-r--r--   1 root root   636 May 30  2023 scgi_params
drwxr-xr-x   2 root root  4096 Ara 27 13:58 sites-available
drwxr-xr-x   2 root root  4096 Ara 27 13:58 sites-enabled
drwxr-xr-x   2 root root  4096 Ara 27 13:58 snippets
-rw-r--r--   1 root root   664 May 30  2023 uwsgi_params
-rw-r--r--   1 root root  3071 May 30  2023 win-utf
```
### nginx.conf
