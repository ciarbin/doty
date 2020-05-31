#Author: Marcin Olko

#TODO:
    #Function from RFC3339 to time
    #Function from readable text to time???

import time

def from_time_to_readable(timedata = None):
    if timedata == None:
        timedata = time.localtime()
    timedata = time.strftime("%d %B", timedata)
    return timedata

def from_time_to_RFC3339(timedata = None):
    if timedata == None:
        timedata = time.localtime()
    timedata = time.gmtime(time.mktime(timedata))               #transferring into UTC date
    timestring = time.strftime("%Y-%m-%dT%H:%M:%S%z", timedata)   #Formatting to RFC3339
    return timestring
