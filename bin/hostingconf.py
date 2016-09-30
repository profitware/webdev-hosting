#!/usr/bin/env python2.7

from pwd import getpwnam
from sys import argv


FIRST_PORT = 1000
CONF_DST = '/vagrant/conf/hosting_{{ username }}.conf'

HOST_FORMAT = u"""
server {
       listen 80;
       server_name "~^{{ username }}\.(?:[0-9a-z-]+)\.(?:[a-z]+)$";

       location / {
           proxy_pass http://127.0.0.1:{{ port }}/;
       }
}
"""


if __name__ == '__main__':
    username = argv[1]

    port = getpwnam(username).pw_uid + FIRST_PORT

    with open(CONF_DST.format(username=username), 'w') as f:
        f.write(HOST_FORMAT.format(
            username=username,
            port=port
        ))
