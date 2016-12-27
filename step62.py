from datetime import *
import pytz

# current_utc = datetime.now(tz)
#
# print (current_utc)

def getPDXTime():
    ptz = pytz.timezone('US/Pacific')
    current_utc = datetime.now(pytz.timezone('UTC'))
    pacific_time = current_utc.astimezone(ptz)
    pdx_time = pacific_time.strftime('%H:%M:%S')
    print ("The current time in Portland is: " + pdx_time)


def getNewYorkTime():
    ptz = pytz.timezone('US/Eastern')
    current_utc = datetime.now(pytz.timezone('UTC'))
    eastern_time = current_utc.astimezone(ptz)
    nyc_time = eastern_time.strftime('%H:%M:%S')
    print ("The current time in New York City is: " + nyc_time)

    if eastern_time.hour >= 9 & eastern_time.hour <= 21:
        print ("\nThe current branch in NYC is open! We hope to see you.")
    else:
        print ("\nWe're sorry, you just missed us. We're closed for the day. We're open from 9:00am to 9:00pm daily ")

def getLondonTime():
    ptz = pytz.timezone('US/Eastern')
    current_utc = datetime.now(pytz.timezone('UTC'))
    eastern_time = current_utc.astimezone(ptz)
    nyc_time = eastern_time.strftime('%H:%M:%S')
    print ("The current time in New York City is: " + nyc_time)

    if eastern_time.hour >= 9 & eastern_time.hour <= 21:
        print ("\nThe current branch in NYC is open! We hope to see you.")
    else:
        print ("\nWe're sorry, you just missed us. We're closed for the day. We're open from 9:00am to 9:00pm daily ")



getNewYorkTime()