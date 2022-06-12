#To generate fake data or dummy data by using python script
from faker import Faker
fakegen = Faker()

#To generate fake names
for i in range(3):
	name = fakegen.name()
	print(name)

#To generate fake first names
for i in range(3):
	fname = fakegen.first_name()
	print(fname)

#To generate last names
for i in range(3):
	lname = fakegen.last_name()
	print(lname)

#To generate fake date
fdate = fakegen.date()
print(fdate)

#To generate fake numbers
fnumber = fakegen.random_number(5)
print(fnumber)

#To generate fake email
femail = fakegen.email()
print(femail)

#To generate fake city
fcity = fakegen.city()
print(fcity)

#To generate random int no in between specified range
random_int_no = fakegen.random_int(min=0, max=9999)
print(random_int_no) 

#To select a random element from the given list of elements
random_element = fakegen.random_element(elements=('Project Manager','Project Lead','Team Lead'))
print(random_element)
#****************************************************************

#Python Turtle graphics code

from turtle import *
bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
	color('red')
	circle(i)
	color('orange')
	circle(i*0.8)
	right(3)
	forward(3)
done()
#********************************************************************
#To generate fake phone number
from faker import Faker
from random import *
fakegen = Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

