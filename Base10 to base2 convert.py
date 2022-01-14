#!/usr/bin/env python
# coding: utf-8

# In[26]:


import math as m

#take input from user, should add validation
x = input("Enter Base 10 number: ")
x = int(x)

#creating an empty list to store my 1's and 0's
base2 = []

#jsut a formated print of the starting base 10 number
print("2 | " + str(x) + " |")

#while loop to to keep dividing base 10 by 2 until 0 is reached
while x > 0:
    #modulus to see if there is a remainder
    y = x % 2
    y = int(y)
    # if else to determine if a 0 or 1 should be placed
    if y > 0:
        z = 1
    else:
        z = 0
    #divides by 2 and truncates because decimals are dumb
    x /= 2
    x = m.trunc(x)
    #append my z value to a list
    base2.append(z)
    #prints out each step if I have to show work, should format so it lines up nicely
    print("2 | " + str(x) + " | " + str(z))

#reverse my list so the binary number is in the correct order
base2 = base2[::-1]

print("\nBase 2")
print("------")
#prints list with no brackets or commas and cuts out spaces
print(*base2, sep='')


# In[ ]:





# In[ ]:




