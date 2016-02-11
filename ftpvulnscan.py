#!/usr/bin/env python
import subprocess
import sys
import os

if len(sys.argv) != 3:
    print "Usage: ftpvulnscan.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()
print "INFO: This would perform nmap scan for " + ip_address + ":" + port
SCAN = "nmap -sV -Pn -vv -p %s --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221 -oN '/root/scripts/recon_enum/results/exam/%s_ftp.nmap' %s" % (port, ip_address, ip_address)
results = subprocess.check_output(SCAN, shell=True)
outfile = "results/exam/" + ip_address + "_ftpvulnscan.txt"
f = open(outfile, "w")
f.write(results)
f.close
