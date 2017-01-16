#!/usr/bin/python

from dateutil.rrule import rrule, DAILY
from datetime import datetime, date
import pprint



pp = pprint.PrettyPrinter(depth=6)

def months(start_month, start_year, end_month, end_year):
    start = datetime(start_year, start_month, 1)
    end = datetime(end_year, end_month, 1)
    return [(d.month, d.year, d.day) for d in rrule(DAILY, dtstart=start, until=end)]

def makeittree(alist):
	temp = {}
	for x in alist:

		damm = date(x[1], x[0], x[2])

		if x[1] not in temp:
			temp.update({x[1]:{}})
		
		if x[0] not in temp[x[1]]:
			temp[x[1]].update({x[0]:{'days':None, 'name':damm.strftime("%B")}})

		if x[2] not in temp[x[1]][x[0]]:
			temp[x[1]][x[0]].update({x[2]:damm.strftime("%A")})

	return temp


pp.pprint( makeittree( months(2, 2008, 2 , 2011)))

