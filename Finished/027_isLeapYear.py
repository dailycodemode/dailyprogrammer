def is_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return "Leap year"
        elif year % 100 == 0:
            return "Regular year"
        else:
            return "Leap year"
    else:
        return "Regular year"

def what_century(year):
    return str(int(year/100 + 1)) + " centry"

print(is_leap_year(1992), ",", what_century(1992))

# ANSWER by bagako
year=int(input('enter a year:'))
if year % 100 == 0:
    x = year/100
    print('Century: %d' % x)
else:
    y=(year/100)+1
    print('Century: %d' % y)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year: Yes')
        else:
            print('Leap year: No')
    else:
        print('Leap year: Yes')
else:
    print('Leap year: No')

# Summary
# No big differences between the answers