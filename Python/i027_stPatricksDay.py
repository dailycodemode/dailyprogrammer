#
# DAILY CODE MODE
# def stParticksDay(year):
# 	import datetime
# 	import calendar
# 	my_date = datetime.datetime(year, 3, 17)
# 	return "St. Patrick's day is on a " + calendar.day_name[my_date.weekday()]
#
# print(stParticksDay(2018))
#
# Answer by jelenger
# import calendar
#
# def stPatrickDay(year):
#     return calendar.day_name[calendar.weekday(year,3,17)]
#
# year = input('Enter year: ')
# print 'St. Patricks day is on:' + stPatrickDay(year)
#
# BREAKDOWN
# datetime.datetime(year, 3, 17)
# >>> a way of putting a date into your program. Datetimes don't come up too often when practising programming but they are  extremely common in the real world and being able to handle them or use is really important.
# #
# #
# # SUMMARY
# # I'm a bit of an amateur with dealing with datetimes in python so it's approriate that my first intermediate challenge is based on it.
# # Answers are nearly identical however I didn't know that calendar module could handle the inputting of a datetime which maybe I should have expected.
# # i027.txt