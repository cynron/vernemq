#!/usr/bin/env python

# Test whether an anonymous connection is correctly denied.

import time

import inspect, os, sys
# From http://stackoverflow.com/questions/279237/python-import-a-module-from-a-folder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"..")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

import vmq
import mosq_test

rc = 1
keepalive = 10
connect_packet = mosq_test.gen_connect("connect-anon-test", keepalive=keepalive)
connack_packet = mosq_test.gen_connack(rc=5)

vmq.start('01-connect-anon-denied.conf')

try:
    time.sleep(0.5)

    sock = mosq_test.do_client_connect(connect_packet, connack_packet)
    sock.close()
    rc = 0
finally:
    vmq.stop()

exit(rc)