x = "this is the right way, right"

#using the find method to get postion of 'right' in x
f = x.find('right', 0, 50)
print("the position of x is", f)

#using the capitalize method to capitalize x
c = x.capitalize()
print(c)

#using the len method to find the lenth of x
print('lenth of x is ', len(x))

#using the lower method to make x all lower case
print(x.lower())

#using the upper method to make x all upper case
print(x.upper())

#using the replace method to make changes to x
print(x.replace('right', 'correct'))

#using the split method to divide x
print(x.split(','))

#using to join method to add to x
j = "|".join(x)
print(j)

#string operations
s = "good"
r = "morning"

#adds the strings together using the '+' operator
output1 = s + r 

#repeats the string using the '*' operator
output2 = s * 3

#checks if "oo" is in s using the 'in' operator
output3 = "oo" in s

print(output1)
print(output2)
print(output3)

#gets "ing" chars from r variable using their indexes
output4 = r[4:7]

#gets "d" char from s variable using its index position
output5 = s[3]

#gets "or" chars from r variable
output6 = r[-6:-4]

print(output4)
print(output5)
print(output6)

#uses "\" to escape special chars in this case the double quotes
d = "This is an \"escaping\" demo"

#uses "\n" to create a new line
f = "This is a \nmulti line \ndemo"

#uses "\r" to replace first word in string
g = "1234 is a carriage return demo\rThis"

#uses "\t" to tab
h = "This is a \ttap demo"

#uses "\f" to feed a new page
i = "This is a \fform feed demo"

#uses "r" to print the raw string
j = r"This is a \rraw \nstring \fdemo"


print(d)
print(f)
print(g)
print(h)
print(i)
print(j)

k = 2
l = 5

#uses str() method to convert int's to str's and uses "+" operator to concatenate the strings
a1 = "(k and l) are ("+str(k)+' and '+str(l)+")"

print(a1)

#uses % placeholders to format the stiring adding vars
oc1 = ("This is a %s demo." % ("formatting"))

print(oc1)

from datetime import datetime, date, timedelta

#uses datetime() function to set the date and time
m = datetime(2013, 5, 17, 16, 21, 18)
print(m)

#uses the strptime method to convert a string into a datetime object
n = datetime.strptime("20130517@162118", "%Y%m%d@%H%M%S")
print(n)

#uses the strftime method to format the string
o = m.strftime("%m/%d/%Y")
print(o)

#using the minute and day methods to output said data
q = m.minute
r = m.day
print(q)
print(r)

#using the today and now methods to output current date&time
s = datetime.today()
t = datetime.now()
print(s)
print(t)

#uses the replace method to update the data
u = s.replace(minute=0,second=0)
print(u)

#returns a time delta object
d1 = date (2013, 5, 17)
d2 = date (2013, 5, 13)
diff1 = d1 - d2
print(diff1)

#uses timedelta() function to add time
v = timedelta(hours=7)
print(m)
print(m + v)