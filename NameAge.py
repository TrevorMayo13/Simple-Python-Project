# importing date class from datetime module
from datetime import date

# creating the date object of today's date
todays_date = date.today()

#inputs
name = input('What is your name? ')
age = int(input('How old are you? '))

#cur year - age = year born
yearBorn = todays_date.year - age

#output prompt
print('Hello {}! You were born in {}.'.format(name, yearBorn))