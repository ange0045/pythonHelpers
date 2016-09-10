#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FILENAME:       logLibrary.py
DESCRIPTION:    Library used to update log and ftp log file to web server.
AUTHOR:         Andre Angelino - github.com/ange0045
"""

import sys
import os.path
import os
from ftplib import FTP
from datetime import datetime
curDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# // LOG FUNCTION - CREATES AND UPDATES log.txt FILE ON RASPBERRY PI
def logFuncs(msg):
    def updateLog(msg):
        file.write(curDateTime + ' - ' + str(msg) + '\n')
        
    def createFile(name):
        file = open(name,'w')
        file.close()
        
    def readFile(name):                  
        try:
            if os.path.isfile(name) == False:
                createFile(name)
            file = open(name,'rb')
            return file   
        except:
            sys.exit(0)
    
    name = '/home/<USER>/log.txt'
    file = readFile(name)                   
    s = file.readlines()                  
    file.close()                           
    file = open(name, "wb")
    updateLog(msg)                         
    
    s.sort(reverse = True)
    for index in s:
        file.write(index)
    file.close()



# // LOG FTP FUNCTION - SENDS THE LOG FILE TO THE SERVER
def ftpLog():
    srv = '<FTP.SERVER.URL>'
    lgn = "ftpUser@SERVER.URL"
    pwd = "<FTPPASSWORD>"
    ftp = FTP(srv)
    ftp.login(lgn,pwd)
    file = "log.txt"
    fname = open('/home/<USER>/log.txt', 'r')
    ftp.storbinary('STOR ' + file, fname)
    fname.close()
    ftp.quit()
