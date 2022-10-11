# this program shows the services running and permits to change their configuration

import subprocess


def exec_command(command):
            """
            :param command: command to be executed
            :return: output with errors for the command
            """
            try:
                        proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        output = (proc.stdout.read() + proc.stderr.read()).decode()
                        print(output)
            except Exception as error:
                        print(error)


command = "service --status-all"
exec_command(command)

# this block alters the services
while True:
            service_name = input("service name (q to exit): ")
            if service_name == "q":
                        break
            print("some options to alter the service:")
            alteration = input("start\nstop\nenable\ndisable\ncancel\noption:")
            if alteration == "cancel":
                        print("cancelled")
            else:
                        exec_command(f"systemctl {alteration} {service_name}")

# shows again the services to the user check the alterations
exec_command(command)
