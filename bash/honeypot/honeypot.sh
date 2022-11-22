#!/bin/bash

nc -lnvkp 21 < ftp.banner 1>>ftp.log 2>>ftp.log &
netstat -nlpt | grep ":21"
echo "fake ftp initialized, saving results in ftp.log"
