"""
Website Blocker
- This is a practice program that I'm getting from hacker.io/blog/python-projects
"""
import time
from datetime import datetime as dt

hosts_path = r"/etc/hosts"     # r == raw string
hosts_temp = 'hosts'
redirect = '127.0.0.1'

# The list of websites that the program blocks. Users can add URLs as needed.
websites_list = ['www.facebook.com', 'facebook.com', 'www.reddit.comm', 'reddit.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now),year,
        dt.now().month, dt.now().day,22):
            print('Working hours:')
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in websites_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+" "+website+"\n")
    
    