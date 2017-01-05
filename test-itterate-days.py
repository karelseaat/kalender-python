#!/usr/bin/python

from dateutil.rrule import rrule, DAILY
from datetime import datetime

def months(start_month, start_year, end_month, end_year):
    start = datetime(start_year, start_month, 1)
    end = datetime(end_year, end_month, 1)
    return [(d.month, d.year, d.day) for d in rrule(DAILY, dtstart=start, until=end)]


print months(2, 2008, 2 , 2011)