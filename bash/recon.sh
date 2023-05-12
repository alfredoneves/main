#!/bin/bash
# root privileges are required

# Usage: ./recon.sh [host] [output_directory]
# Example: ./recon.sh nmap.org results
# some programs may fail because of cookies and user-agent

target=$1
output_directory=$2

# check the number of arguments
if [ $# != 2 ]; then
	echo "Usage: ./recon.sh [host] [output_directory]"
	echo "Example: ./recon.sh nmap.org results"
	exit
fi

mkdir $output_directory

whois $target >> $output_directory/whois_results	# register information

dig $target -t ANY >> $output_directory/dig_results	# dns query

echo "trying zone transfer and saving results in $output_directory/zone_transfer_results"
name_servers=$(host -t ns $target | cut -d " " -f 4)
for server in $name_servers; do host -l -a $server >> $output_directory/zone_transfer_results; done

echo "testing the methods allowed (you can test for each directory in the server)"
curl -v -X OPTIONS $target >> $output_directory/options_allowed

firefox https://sitereport.netcraft.com/?url=$target	# verifies netcraft registers of host

# subdomains
subfinder -d $target >> $output_directory/subfinder_results

# crawler
gospider -s $target >> $output_directory/gospider_results

# directory enumeration (check the wordlist)
echo "extensions for directory enumeration (example: php,txt,sql,cgi,sh,html,css,js,py,bkp,pdf,bak,src,inc,old,zip):"
read extensions
gobuster dir -u $target -w /usr/share/wordlists/dirb/big.txt -x $extensions -o $output_directory/gobuster_results

# plugins and vulnerabilities
nikto -h $target -o $output_directory/nikto_results
whatweb $target $output_directory/whatweb_results

echo "recon finished"
echo "results saved in $output_directory"
