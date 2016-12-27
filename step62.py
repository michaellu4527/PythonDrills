from datetime import *
import pytz

# current_utc = datetime.now(tz)
#
# print (current_utc)

# Function obtains the current time in Portland and returns whether the store branch is open or not

def getPDXTime():
    ptz = pytz.timezone('US/Pacific')
    current_utc = datetime.now(pytz.timezone('UTC'))
    pacific_time = current_utc.astimezone(ptz)
    pdx_time = pacific_time.strftime('%H:%M:%S')
    print ("\nThe current time in Portland is: " + pdx_time)

    if pacific_time.hour >= 9 & pacific_time.hour < 21:
        print ("\nThe current branch in Portland HQ is open! We hope to see you.")
    else:
        print ("\nWe're sorry, you just missed us. We're closed for the day. We're open from 9:00am to 9:00pm daily ")

# Function obtains the current time in NYC and returns whether the store branch is open or not

def getNewYorkTime():
    ptz = pytz.timezone('US/Eastern')
    current_utc = datetime.now(pytz.timezone('UTC'))
    eastern_time = current_utc.astimezone(ptz)
    nyc_time = eastern_time.strftime('%H:%M:%S')
    print ("\nThe current time in New York City is: " + nyc_time)

    if eastern_time.hour >= 9 & eastern_time.hour < 21:
        print ("\nThe current branch in NYC is open! We hope to see you.")
    else:
        print ("\nWe're sorry, you just missed us. We're closed for the day. We're open from 9:00am to 9:00pm daily ")

# Function obtains the current time in London and returns whether the store branch is open or not

def getLondonTime():
    ptz = pytz.timezone('Europe/London')
    current_utc = datetime.now(pytz.timezone('UTC'))
    gmt_time = current_utc.astimezone(ptz)
    london_time = gmt_time.strftime('%H:%M:%S')
    print ("\nThe current time in London is: " + london_time)

    if gmt_time.hour >= 9 & gmt_time.hour < 21:
        print ("\nThe current branch in London is open! We hope to see you.")
    else:
        print ("\nWe're sorry, you just missed us. We're closed for the day. We're open from 9:00am to 9:00pm daily ")

# Function that will obtain user input and run the corresponding function to get the user their requested
# information

def getBranchInfo():
    flag = 1
    while (flag == 1):
        choice = raw_input("\nWe have a branch in 3 cities (Portland [HQ], New York City, and London)."
                           "\nTo see if the branch is currently open, please enter (p, n, or l): ")
        if choice == 'p':
            getPDXTime()
            anotherChoice()
            if (anotherChoice() == 'y'):
                flag = 1
            elif (anotherChoice() == 'n'):
                flag = 0
        elif choice == 'n':
            getNewYorkTime()
            if (anotherChoice() == 'y'):
                flag = 1
            elif (anotherChoice() == 'n'):
                flag = 0
        elif choice == 'l':
            getLondonTime()
            if (anotherChoice() == 'y'):
                flag = 1
            elif (anotherChoice() == 'n'):
                flag = 0
        else:
            print ("Invalid choice! Please try again...")

# Function that handles the possibility of the user wanting to view if another store is open or not

def anotherChoice():
    choice = raw_input("\nDo you want to see if another branch is open? [y/n] ")
    return choice

getBranchInfo()