# https://www.reddit.com/r/dailyprogrammer/comments/r0r3h/3172012_challenge_27_easy/
# MINE
def whichCentury(year):
    return int(year[:len(year) - 2]) - 1


def isLeapYear(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True


print(isLeapYear(2004))

# ANSWER fromm u/bagako
import sys
is_leap_yr = 'No'

def leap_yr(year):
    if year % 4 == 0:
        is_leap_yr = 'Yes'
    elif year % 100 == 0:
        is_leap_yr = 'No'
    elif year % 400 == 0:
        is_leap_yr = 'Yes'
    else:
        is_leap_yr = 'No'
    return is_leap_yr

year = int(sys.argv[1])
print(year)
# def main():
#     year = int(sys.argv[1])
    # leap = leap_yr(year)
    # century = (year/100) if year % 100 == 0 else ((year - (year % 100))/ 100) + 1
    # print 'Century: ' + str(century)
    # print 'Leap Year: ' + leap

print(whichCentury(-54))

# BREAKDOWN
# == can be replaced with 'is' which I think is a little more readable eg
# year%100 is 0
# vs
# year%100 == 0

sys.argv[1]
# For every invocation of Python, sys.argv is automatically a list of
# strings representing the arguments (as separated by spaces) on the command-line
# It means arguments vector and it contains the arguments passed to the program
#  The first one is always the program name i.e. sys.argv[0]
# However in this version he is passing in his first arguement
# SUMMARY
# His leap year is actually incorrect however we are more interested in the programming
# One big difference between the answers is that I've treated the year as a string
# hence I am able to split it easily enough
# Converting to an int and then dividing by 100 would be more in line with the understanding
# of a century