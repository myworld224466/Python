'''
Date Time module
-----------------

'''
import os
os.system('clear')
from datetime import *

cDate=datetime.now()
print(cDate)
print(cDate.year)
print(cDate.month)
print(cDate.day)


#Showing Time in fragment
print(cDate.hour)
print(cDate.minute)
print(cDate.second)

#Formating Date  
print(cDate.strftime('week day Short : %a'))
print(cDate.strftime('week day Full : %A'))
print(cDate.strftime('week day Number : %w'))

print('='*80)


#Formating Month & Year 
print(cDate.strftime('Day of Month : %d'))
print(cDate.strftime('Month short : %b'))
print(cDate.strftime('Month Full : %B'))
print(cDate.strftime('Month Number : %m'))
print(cDate.strftime('Year without century : %y'))
print(cDate.strftime('Year with century : %Y'))

print('='*80)


#Formating Time in Hours, Minutes & Seconds 
print(cDate.strftime('Hour 24 : %H'))
print(cDate.strftime('Hour 12 : %I'))
print(cDate.strftime('Hour AM/PM : %p'))
print(cDate.strftime('Minutes 60 : %M'))
print(cDate.strftime('Second 60 : %S'))
print(cDate.strftime('Micro Second 60 : %f'))

print('='*80)


print(cDate.strftime('Full time: %T'))
print(cDate.strftime('Full date: %D'))


#Custom Formating Time & Date
print(cDate.strftime('Custome Time: %I:%M:%S %p'))
print(cDate.strftime('Custome Date: %Y-%m-%d'))
print(cDate.strftime('Custome Date: %A,%B %d, %Y'))