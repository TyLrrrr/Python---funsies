#!/usr/bin/env python
# coding: utf-8

# In[23]:


# take in user input as a string
a = input("enter base 2 number: ")

#seperates string so each digit has its own index in a list
a_list = [int(x) for x in str(a)]

#reverses my list so i could use an increment variable to get the value for the power
a_list = a_list[::-1]

#Setting the variable to 0
power = 0
answer = 0

#creating a loop to iterate over the list
for x in a_list:
    #if the digit is 0 its going to set z to 0 and prints out the step
    if x == 0:
        z = 0
        print("0*2^" + str(power) + "=" + str(z))
    #if the digit is 1 it will preform the operation 1 * 2^ power and set z to that and print out the step
    else:
        z = 1 * (2**power)
        print("1*2^" + str(power) + "=" + str(z))
    #running total of each step    
    answer += z
    #increments the power for the next step
    power += 1

#prints out answer
print("-------")
print("Binary: " + str(a) + " --> Decimal: " + str(answer))


# In[ ]:





# In[ ]:




