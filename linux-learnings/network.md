> Network comminication commands

wget - download files or apps from the internet
```bash
wget https://www.google.com
```

curl - download files or apps from the internet
```bash
curl https://www.google.com
curl -O https://www.google.com  # download
```

ping - check if a server is up
```bash
ping google.com
```

default FTP port is 21

FTP Transfer connect to a server and transfer files
```bash
ftp someIP # connect to a server
ftp> ls # list files
ftp> get someFile # download file
ftp> put someFile # upload file
ftp> bye # exit
```

scp - secure copy
```bash
scp someFile user@someIP:/home/user # copy file to remote server
scp user@someIP:/home/user/someFile . # copy file from remote server
```
