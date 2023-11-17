> Linux File System

| File Symbol | Meaning                     |
|-------------|-----------------------------|
| -           | Regular File                |
| d           | Directory                   |
| l           | link                        |
| c           | Special File or device file |
| s           | socket                      |
| p           | Named pipe                  |
| b           | Block device                |

/root - root user home directory
:/ - root directory the very first directory in the file system

>  some commands of linux

sudo su - switch to root user
``` bash
sudo su -  # switch to root user
```
passwd - change password
``` bash
passwd  # change password
```
pwd - print working directory
``` bash
pwd  # print working directory
```
whoami - print current user
``` bash
whoami  # print current user
```
hostname - print system name
``` bash
hostname  # print system name
```
uname - kernel info
``` bash
uname -a  # print all kernel info
uname -r  # print kernel release
uname -v  # print kernel version
uname -m  # print machine hardware name
```
cd - change directory
``` bash
cd /  # change directory to root directory
cd ..  # change directory to parent directory
cd ~  # change directory to home directory
cd -  # change directory to previous directory
```
ifconfig - network interface configuration
``` bash
ifconfig  # network interface configuration
```
ip addr - network interface configuration
``` bash
ip addr  # network interface configuration
```
touch - create empty file
``` bash
touch somefile  # create empty file named somefile
```
vi - text editor
``` bash
vi somefile  # open somefile in vi editor
```
date - print date and time
``` bash
date  # print date and time
```
cp - copy file
``` bash
cp somefile somefile2  # copy somefile to same directory with name somefile2
```
cp -R - copy directory
``` bash
cp -R somedir somedir2  # copy somedir to same directory with name somedir2
```
mv - move file
``` bash
mv somefile somedir  # move somefile to somedir
```
mkdir - make directory
``` bash
mkdir somedir  # make directory named somedir
```
rmdir - remove directory
``` bash
rmdir somedir  # remove directory named somedir
```
rm -Rf - remove directory
``` bash
rm -Rf somedir  # force to remove directory and its subdirectories
```
find - find file
``` bash
find / -name somefile  # find file named somefile in root directory
```
updatedb - update locate database
``` bash
updatedb  # update locate database without updatedb locate command will not work
```
locate - find file
``` bash
locate somefile  # find file named somefile in root directory
```
> Wildcards
- ' * '   = represents zero or more characters
- ' - '   = represents a single character
- ' ? '   = represents a single character
- ' [ ] ' = represents a range of characters
> Examples
``` bash
touch text{1-5}-xyz # creates text1-xyz, text2-xyz, text3-xyz, text4-xyz, text5-xyz
text => rm te*t # matches text, teeeext, teeeeeeeeeeeee
text => rm te-t # matches te1t, te2t, te3t, te4t, te5t, te6t, te7t, te8t, te9t
text => rm te?t # matches te1t, te2t, te3t, te4t, te5t, te6t, te7t, te8t, te9t
text => rm te[1-9]t # matches te1t, te2t, te3t, te4t, te5t, te6t, te7t, te8t, te9t
rm *xyz # matches text1-xyz, text2-xyz, text3-xyz, text4-xyz, text5-xyz
rm ?ext* # matches text1-xyz, text2-xyz, text3-xyz, text4-xyz, text5-xyz
```
inode - index node
``` bash
ls -i  # print inode number
```
soft link - symbolic link
``` bash
ln -s somefile somefile2  # create soft link named somefile2 to somefile
```
hard link - hard link
``` bash
ln somefile somefile2  # create hard link named somefile2 to somefile
```
ls -ltri - list files
``` bash
ls -ltri  # list files
```
rm -r - remove directory
``` bash
rm -r somedir  # remove directory named somedir
```
help of any command
``` bash
man ls # run help for ls command
whatis ls # run help for ls command
```

File Permissions
- r - read
- w - write
- x - execute
- d - directory
- '-' - regular file
- 's' - setuid/setgid
- 't' - sticky bit
- 'l' - link
Each Permission has 3 bits
- 1st bit - owner
- 2nd bit - group
- 3rd bit - others
- '-rwx:user rwx:group rwx:Others' 
change permission

| Number | Permission             |
|--------|------------------------|
| 0      | No Permission          |
| 1      | Execute                |
| 2      | Write                  |
| 3      | Write + Execute        |
| 4      | Read                   |
| 5      | Read + Execute         |
| 6      | Read + Write           |
| 7      | Read + Write + Execute |
chmod - change permission user:group:others <file_name>
``` bash
chmod 777 somefile  # change permission to 777 for all user
chmod g-w somefile  # remove write permission from group
chmod o-r somefile  # remove read permission from others
chmod u+x somefile  # add execute permission to owner
chmod a+x somefile  # add execute permission to all
```
change owner
``` bash
chown root somefile  # change owner to root
```
change group
``` bash
chgrp root somefile  # change group to root
```
setfacl - set file access control list
``` bash
setfacl -m u:root:rwx somefile  # set file access control list for user root
```
getfacl - get file access control list
``` bash
getfacl somefile  # get file access control list
```
echo - print or set system variable
``` bash
echo $PATH  # print system variable PATH
echo "some text" # print some text
echo "some text" > somefile  # print some text to somefile and overwrite if somefile exists
echo "some text" >> somefile  # append some text to somefile
echo "some text" | tee somefile  # print some text to somefile and stdout
echo "some text" | tee -a somefile  # append some text to somefile and stdout
```
stdin 0 - standard input
``` bash
cat > somefile  # write to somefile
```
stdout 1 - standard output
``` bash
cat somefile  # print somefile
```
stderr  - standard error
``` bash
cat somefile 2> errorfile  # print error to errorfile
```
wc -c - count characters
``` bash
wc -c somefile  # count characters in somefile
```
more and less - print file
``` bash
ls -l | more  # print file page by page
ls -l | less  # print file in a new file
```
'|' - pipe for combining commands
``` bash
ls -l | grep somefile  # print file named somefile
```
tail - print last -1 lines of file
``` bash
ls -l | tail -1  # print last 10 lines of file
```
head - print first -1 lines of file
``` bash
ls -l | head -1  # print first 10 lines of file
```
cut - cut section from each line of file
``` bash
ls -l | cut -d " " -f 1  # cut first column from each line of file
```
awk - pattern scanning and processing language
``` bash
ls -l | awk '{print $1}'  # print first column from each line of file
```
grep and egrep - print lines matching a pattern -c to count 
-i to ignore case-sensitive -n to print line number
-v to print lines NOT matching pattern
egrep keyword1|keyword2 to print lines matching keyword1 or keyword2
``` bash
ls -l | grep sometext somefile  # print lines matching sometext in somefile
ls -l | egrep somefile  # print lines matching somefile
```
sort - sort lines of text file
sort -r - sort lines of text file in reverse order
sort -n - sort lines of text file in numeric order
sort -u - sort lines of text file and remove duplicates
``` bash
ls -l | sort  # sort lines of text file
ls -l | sort -r  # sort lines of text file in reverse order
ls -l | sort -n  # sort lines of text file in numeric order
ls -l | sort -u  # sort lines of text file and remove duplicates
ls -l | sort -k 5  # sort lines of text file by 5th column
```
uniq - report or omit repeated lines
``` bash
ls -l | uniq  # report or omit repeated lines
ls -l | uniq -c  # report or omit repeated lines and count
ls -l | uniq -d  # report or omit repeated lines and print only duplicates
```
diff - compare files line by line
``` bash
diff somefile somefile2  # compare files line by line
```
cmp - compare two files byte by byte
``` bash
cmp somefile somefile2  # compare two files byte by byte
```
tar - tape archive
``` bash
tar -cvf somefile.tar somefile  # create somefile.tar from somefile
tar -xvf somefile.tar  # extract somefile.tar
```
gzip - compress or expand files
``` bash
gzip somefile  # compress somefile
gzip -d somefile.gz  # decompress somefile.gz
```
gunzip - compress or expand files
``` bash
gunzip somefile  # compress somefile
gunzip -d somefile.gz  # decompress somefile.gz
```
truncate - shrink or extend the size of a file to the specified size
``` bash
truncate -s 10 somefile  # shrink somefile to 10 bytes
truncate -s +10 somefile  # extend somefile to 10 bytes
```
split - split a file into pieces
``` bash
split -b 10 somefile  # split somefile into 10 bytes pieces
```
systemctl - control the systemd system and service manager
``` bash
systemctl status somefile  # show status of somefile
systemctl start somefile  # start somefile
systemctl stop somefile  # stop somefile
systemctl restart somefile  # restart somefile
systemctl enable somefile  # enable somefile
systemctl disable somefile  # disable somefile
```
journalctl - query the systemd journal
``` bash
journalctl  # query the systemd journal
journalctl -f  # query the systemd journal and follow
journalctl -u somefile  # query the systemd journal for somefile
journalctl -u somefile -f  # query the systemd journal for somefile and follow
```
ps - report a snapshot of the current processes
``` bash
ps  # report a snapshot of the current processes
ps -e # report a snapshot of the current processes
ps -ef  # report a snapshot of the current processes
ps -ef | grep somefile  # report a snapshot of the current processes
ps -u user # process used by user
```
top - display Linux processes
``` bash
top  # display Linux processes
top -u user  # display Linux processes used by user
top -p pid  # display Linux processes used by pid
top -f somefile  # display Linux processes used by somefile
top -c  # display Linux processes with command
top -o %MEM  # display Linux processes with memory usage
top -o %CPU  # display Linux processes with cpu usage
```
kill - terminate a process
``` bash
kill pid  # terminate a process by pid
kill -1 pid  # terminate a process and restart
kill -2 pid  # interrupt a process adn terminate
kill -9 pid  # kill a process force
kill -15 pid  # terminate a process gracefully
```
nohup - run a command immune to hangups
``` bash
nohup somefile  # run somefile immune to hangups
```
netstat - print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships
``` bash
netstat 
netstat -a  # print all network connections
netstat -l  # print all listening network connections
netstat -s  # print all network statistics
netstat -i  # print all network interfaces
netstat -r  # print all network routing tables
netstat -p  # print all network process
netstat -n  # print all network connections without resolving
netstat -au  # print all udp network connections
netstat -at  # print all tcp network connections
netstat -lu  # print all listening udp network connections
netstat -nt  # print all tcp network connections without resolving
netstat -nu  # print all udp network connections without resolving
netstat -nl  # print all listening network connections without resolving
netstat -lt  # print all listening tcp network connections
netstat -ns  # print all network statistics without resolving
netstat -ni  # print all network interfaces without resolving
netstat -nr  # print all network routing tables without resolving
netstat -np  # print all network process without resolving
netstat -nlt  # print all listening tcp network connections without resolving
netstat -nlu  # print all listening udp network connections without resolving
```
xyz.sh - shell script
``` bash
chmod g-w xyz.sh  # remove write permission from group
chmod o-r xyz.sh  # remove read permission from others
chmod u+x xyz.sh  # add execute permission to owner
chmod a+x xyz.sh  # add execute permission to all
```
alias - create an alias
``` bash
xyz="ls -la"  # create an alias xyz for ls -l
xyz  # run xyz
```
unalias - remove an alias
``` bash
unalias xyz  # remove an alias xyz
```
history - display the history list
``` bash
history  # display the history list
history -c  # clear the history list
```
nslookup - query Internet name servers interactively
``` bash
nslookup www.google.com  # query Internet name servers interactively
nslookup 192.1.1811 # query Internet name servers interactively
nslookup -type=mx www.google.com  # query Internet name servers interactively for mx record
nslookup -type=ns www.google.com  # query Internet name servers interactively for ns record
```
timedatectl - control the system time and date
``` bash
timedatectl  # control the system time and date
timedatectl set-timezone Asia/Kolkata  # set timezone to Asia/Kolkata
timedatectl set-time 10:10:10  # set time to 10:10:10
timedatectl set-time 2021-10-10  # set date to 2021-10-10
timedatectl set-time 2021-10-10 10:10:10  # set date and time to 2021-10-10 10:10:10
```
lsblk - list block devices
``` bash
lsblk  # list block devices
lsblk -a  # list all block devices
lsblk -d  # list only block devices
lsblk -f  # list filesystems
lsblk -i  # list all block devices with info
lsblk -l  # list all block devices without tree
lsblk -m  # list all block devices with size in MB
lsblk -n  # list all block devices without header
lsblk -o  # list all block devices with specific columns
lsblk -p  # list all block devices with full path
lsblk -r  # list all block devices with raw output
lsblk -S  # list all block devices with size in sectors
lsblk -t  # list all block devices with filesystem type
lsblk -x  # list all block devices without filesystem type
lsblk -z  # list all block devices with size in bytes
```