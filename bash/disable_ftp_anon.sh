#!/bin/bash
# this script disables the anonymous login in ftp

mv /etc/vsftpd.conf /etc/vsftpd.conf.bkp
cat /etc/vsftpd.conf.bkp | sed "s/anonymous_enable=YES/anonymous_enable=NO/g" > /etc/vsftpd.conf
