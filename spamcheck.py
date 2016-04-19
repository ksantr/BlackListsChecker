#! /usr/bin/env python
import socket
import string

from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()


class BlacklistsChecker:
    def __init__(self, threads=1):
        self.threads = threads
        self.serverlist = [
            "truncate.gbudb.net",
            "bad.psky.me",
            "0spam.fusionzero.com",
            "access.redhawk.org",
            "b.barracudacentral.org",
            "bhnc.njabl.org",
            "bl.deadbeef.com",
            "bl.spamcannibal.org",
            "bl.spamcop.net",
            "bl.technovision.dk",
            "blackholes.five-ten-sg.com",
            "blackholes.mail-abuse.org",
            "blacklist.sci.kun.nl",
            "blacklist.woody.ch",
            "bogons.cymru.com",
            "cbl.abuseat.org",
            "cdl.anti-spam.org.cn",
            "combined.abuse.ch",
            "combined.rbl.msrbl.net",
            "db.wpbl.info",
            "dnsbl-1.uceprotect.net",
            "dnsbl-2.uceprotect.net",
            "dnsbl-3.uceprotect.net",
            "dnsbl.cyberlogic.net",
            "dnsbl.inps.de",
            "dnsbl.kempt.net",
            "dnsbl.njabl.org",
            "dnsbl.solid.net",
            "dnsbl.sorbs.net",
            "drone.abuse.ch",
            "duinv.aupads.org",
            "dul.ru",
            "dyna.spamrats.com",
            "dynip.rothen.com",
            "forbidden.icm.edu.pl",
            "hil.habeas.com",
            "images.rbl.msrbl.net",
            "ips.backscatterer.org",
            "ix.dnsbl.manitu.net",
            "korea.services.net",
            "mail-abuse.blacklist.jippg.org",
            "no-more-funn.moensted.dk",
            "noptr.spamrats.com",
            "ohps.dnsbl.net.au",
            "omrs.dnsbl.net.au",
            "orvedb.aupads.org",
            "osps.dnsbl.net.au",
            "osrs.dnsbl.net.au",
            "owfs.dnsbl.net.au",
            "owps.dnsbl.net.au",
            "phishing.rbl.msrbl.net",
            "probes.dnsbl.net.au",
            "proxy.bl.gweep.ca",
            "proxy.block.transip.nl",
            "psbl.surriel.com",
            "rbl.interserver.net",
            "rbl.orbitrbl.com",
            "rbl.schulte.org",
            "rdts.dnsbl.net.au",
            "relays.bl.gweep.ca",
            "relays.bl.kundenserver.de",
            "relays.nether.net",
            "residential.block.transip.nl",
            "ricn.dnsbl.net.au",
            "rmst.dnsbl.net.au",
            "short.rbl.jp",
            "spam.abuse.ch",
            "spam.dnsbl.sorbs.net",
            "spam.rbl.msrbl.net",
            "spam.spamrats.com",
            "spamguard.leadmon.net",
            "spamlist.or.kr",
            "spamrbl.imp.ch",
            "spamsources.fabel.dk",
            "spamtrap.drbl.drand.net",
            "t3direct.dnsbl.net.au",
            "tor.dnsbl.sectoor.de",
            "torserver.tor.dnsbl.sectoor.de",
            "ubl.lashback.com",
            "ubl.unsubscore.com",
            "virbl.bit.nl",
            "virus.rbl.jp",
            "virus.rbl.msrbl.net",
            "wormrbl.imp.ch",
            "zen.spamhaus.org",
        ]

    def is_spam(self, host):
        """Check hosts in blaclists"""
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
        Check host in the server's blacklis

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
    sp = BlacklistsChecker(threads=10)
    print sp.is_spam('109.163.234.7')
