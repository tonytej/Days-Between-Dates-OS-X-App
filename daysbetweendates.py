
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Compensate for leap days.
# Assume that the birthday and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012
# you are 1 day old.
#
# Hint
# A whole year is 365 days, 366 if a leap year.
from Tkinter import *

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isLeapYear(year) == True:
            return 29
        else:
            return 28

def nextDay(year, month, day):
    if day < 30:
        if daysInMonth(year, month) == 28:
            if day == 28:
                return year, month +1, 1
        if daysInMonth(year, month) == 29:
            if day == 29:
                return year, month +1, 1
        return year, month, day + 1
    if day == 30:
        if daysInMonth(year, month) == 30:
            return year, month +1, 1
        elif daysInMonth(year, month) == 31:
            return year, month, day + 1
    if day == 31:
        if daysInMonth(year, month) == 31:
            if month == 12:
                return year +1, 1, 1
            return year, month +1 , 1

def dateIsAfter(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is after year2-month2-day2.  Otherwise, returns False."""
    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False

def daysBetweenDates(day1, month1, year1, day2, month2, year2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!

    days = 0
    while dateIsAfter(year2, month2, day2, year1, month1, day1):
        days += 1
        year1, month1, day1 = nextDay(year1, month1, day1)
    return days





root = Tk()
root.title('Days Between Dates')

l1 = Label(root, text='/')
l2 = Label(root, text='/')

e = Entry(root, justify = 'center', width = 6)
e1 = Entry(root, justify = 'center', width = 6)
e2 = Entry(root, justify = 'center', width = 6)

e.insert(0, 'dd')
e1.insert(0, 'mm')
e2.insert(0, 'yyyy')

l1.grid(row=1, column=1)
l2.grid(row=1, column=3)

e.grid(row=1, column=0)
e1.grid(row=1, column=2)
e2.grid(row=1, column=4)

l1a = Label(root, text='/')
l2a = Label(root, text='/')

ea = Entry(root, justify = 'center', width = 6)
e1a = Entry(root, justify = 'center', width = 6)
e2a = Entry(root, justify = 'center', width = 6)

ea.insert(0, 'dd')
e1a.insert(0, 'mm')
e2a.insert(0, 'yyyy')

l1a.grid(row=3, column=1)
l2a.grid(row=3, column=3)

ea.grid(row=3, column=0)
e1a.grid(row=3, column=2)
e2a.grid(row=3, column=4)

l = Label(root, text="Date 1:")
l.grid(row=0, columnspan = 5)

l1 = Label(root, text='Date 2:')
l1.grid(row=2, columnspan=5)

#def calculate():
 #   result = daysBetweenDates(int(e.get()), int(e1.get()), int(e2.get()), int(ea.get()), int(e1a.get()), int(e2.get())
  #  l1 = Label(root, text=str(result))
   # l1.grid(row = 5, columnspan = 5)

def calculate():
    l = Label(root, text = str(daysBetweenDates(int(e.get()), int(e1.get()), int(e2.get()),
                                         int(ea.get()), int(e1a.get()), int(e2a.get()))))
    l.grid(row=5, columnspan =5)

b = Button(root, text='Calculate', command = calculate)
b.grid(row = 4, columnspan = 5)

root.mainloop()









