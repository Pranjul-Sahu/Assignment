#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program to count the number of even and odd numbers from a series of numbers.



my_list=[1,2,5,7,8,4,9]
even_number = 0
odd_number = 0
for i in my_list:
    if (i%2==0):
        even_number+=1

    else:
        odd_number+=1
        
print("Number of even number -",even_number) 
print("Number of odd number -",odd_number)

