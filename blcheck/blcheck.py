#! /usr/bin/env python
import socket
import sys
import string

from gevent.pool import Pool
from gevent import monkey
from servers import SERVER_LIST
monkey.patch_all()


class BlackListsChecker:
    def __init__(self, threads=1):
        self.threads = threads
        self.serverlist = SERVER_LIST

    def is_spam(self, host):
        """Check hosts in blacklists"""
        """
        Run async spam checking on host

        :param host: domain or ip address
        :return: None
        """
        # Severs where host is blacklisted
        self.blacklisted = []
        # Generate ars for checker
        args = [(host, i) for i in self.serverlist]
        # Init Pool
        self.pool = Pool(self.threads)
        # Spawn pool
        self.pool.map(self.check, args)
        return self.blacklisted

    def check(self, args):
        """
        Check host in the server's blacklist

        :param *args: tuple with host name for check and
            blacklist server address
        :return: None
        """
        host, server = args

        try:
            host_addr = socket.gethostbyname(host)
        except socket.error:
            return

        # Reverse ip addr
        addr_parts = string.split(host_addr, '.')
        addr_parts.reverse()
        host_addr = string.join(addr_parts, '.')

        check_host = '{0}.{1}'.format(host_addr, server)

        try:
            check_addr = socket.gethostbyname(check_host)
        except socket.error:
            check_addr = None

        if check_addr is not None and "127.0.0." in check_addr:
            self.blacklisted.append(server)


if __name__ == "__main__":
    sp = BlackListsChecker(threads=20)
    if len(sys.argv) > 1:
        result = sp.is_spam(sys.argv[1])
        if result:
            for r in result:
                print r
