#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FILENAME:       restartApache.py
DESCRIPTION:    Used to restart an apache server on a schedule
DEPENDENCIES:   logLibrary.py
AUTHOR:         Andre Angelino - github.com/ange0045
"""
import logLibrary as logLib
import os

try:
    msg = 'Restarted Apache Server'
    os.system("sudo /etc/init.d/apache2 reload")
    os.system("sudo /etc/init.d/apache2 restart")
    logLib.logFuncs(msg)
    logLib.ftpLog()

except:
    msg = 'restartApache.py failed'
    logLib.logFuncs(msg)
