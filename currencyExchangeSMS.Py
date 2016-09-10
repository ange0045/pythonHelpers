    
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FILENAME:       currencyExchangeSMS.py
DESCRIPTION:    Through the use of openexchangerates api this code checks the current exchange rate and last week's value. 
                Provides the difference, and a specific converted amount and sends an SMS with Twilio every day. 
                Review openexchangerates documentation for list of currencies. 
                This code is built using: Openexchangerates: openexchangerates.org // Twilio: www.twilio.com
DEPENDENCIES:   Accounts are required to be created for both Openexchangerates and Twilio
AUTHOR:         Andre Angelino - https://github.com/ange0045

| --- IMPORTANT --- |
VARIABLES:      The following variables need to be changed before using script:
                accountSID:...Needs to be updated to user's account SID 
                authToken:....Needs to be updated to show users Twilio's authorization token 
                twNumber:.....Needs to be updated to device number provided by Twilio
                myNumber:.....Needs to be updated to destination phone number
                url:..........Needs to be updated to show user's openexchangerates ID
                curEx:........Needs to be updated to the currency code in openexchangerates (Below uses Canadian dollars)
                valTot:.......If calculation on a specific amount is required, the 500 would need to be udpated to reflect new value. If not, valTot variable can be removed from code. 
"""

import sys
import json, requests
import datetime

try:
    from twilio.rest import TwilioRestClient
    
    # -- Variables that require update
    accountSID = '<TWILIOACCOUNTSID>'
    authToken = '<TWILIOAUTHTOKEN>' 
    OERID   = '<OPENEXCHANGERATESID>'
    twNumber = '<TWILIODEVICENUMBER>'
    myNumber = '<DESTINATIONPHONENUMBER>'
  
    # -- Calculates the rate 7 days before
    prevDate = datetime.date.today()-datetime.timedelta(7)
    
    url     = 'https://openexchangerates.org/api/latest.json?app_id='+OERID
    urlPrev = 'https://openexchangerates.org/api/historical/'+str(prevDate)+'.json?app_id='+OERID

    def getRate(url):
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        curr = data["rates"]
        curEx = curr["CAD"]
        return curEx

    todVal = getRate(url)
    yesVal = getRate(urlPrev)
    
    # 500 is value provided to get a custom amount. Change or delete if not needed.
    valTot = todVal * 500 

    totVal = round(valTot,2)
    difVal = todVal-yesVal
    formVal = round(difVal,5)
    
    # -- Sets how the information will be provided in the SMS
    smsFormat = "\n Today: "+str(todVal)+" | Last Week: "+str(yesVal)+" | Difference: "+str(formVal)+" | Total: "+str(totVal)
    twilioCli = TwilioRestClient(accountSID, authToken)
    message = twilioCli.messages.create(body=smsFormat, from_=twNumber, to=myNumber)
