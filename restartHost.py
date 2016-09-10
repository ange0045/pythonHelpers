#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FILENAME:       restartHost.py
DESCRIPTION:    Reboots ssh host using pxssh
DEPENDENCIES:   logLibrary.py
AUTHOR:         Andre Angelino - github.com/ange0045
"""
import logLibrary as logLib
from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh()
    hostN = '<IPorURLofHOST>'
    userN = '<USER>'
    passW = '<PASSWORD>'
    s.login(hostN, userN, passW)
    s.sendline('reboot')
    msg = 'Host rebooted'
    logLib.logFuncs(msg)
    logLib.ftpLog()

except:
    msg = 'restartHost.py failed'
    logLib.logFuncs(msg)

