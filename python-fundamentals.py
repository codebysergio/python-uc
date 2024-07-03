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