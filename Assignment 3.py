#!/usr/bin/env python
# coding: utf-8

# # Merna Mansour

# # Assignment 3

# ### Write a function to count the number 4 in a given list.

# In[8]:


def counter():
    c=0
    x=int(input('please enter the length of the list'))
    z=[]
    for i in range(0,x,1):
        nums=int(input(' please enter number {} '.format(i+1)))
        z.append(nums)    
    for i in z:  
        if i==4:
            c+=1
    print(c)

counter()


# ### write a  function to check whether a number is divisible by another number.

# In[10]:


def divisible(x,y):
    if x%y==0:
        print('divisible')
    else:
        print('not divisible')
divisible(15,2)


# ### write a function to find the maximum and minimum numbers from a sequence of numbers.

# In[14]:


def nums():
    l=int(input('please enter the length of the list'))
    f=[]
    maxim=0
    minim=0
    for i in range(0,l,1):
        m=int(input(' please enter number {} '.format(i+1)))
        f.append(m) 
    for i in f:
        if i>maxim:
            maxim=i
        if i<minim:
            minim=i
    print('the heighst number is {} and the lowest number is {}'.format(maxim,minim))
nums()


# ### Write a Python function that takes two lists and returns True if they have at least one common member.

# In[ ]:


def two_lists():
    r=False
    l=int(input('please enter the length of the first list'))
    f=[]
    for i in range(0,l,1):
        m=int(input(' please enter number {} '.format(i+1)))
        f.append(m)
    s=int(input('please enter the length of the second list'))
    k=[]
    for i in range(0,s,1):
        d=int(input(' please enter number {} '.format(i+1)))
        k.append(d)
    for i in f:
        for j in k:
            if i==j:
                r=True
                return r
         
            
two_lists()


# In[3]:


#another solution
def two_list(list1,list2):
    r=False
    for i in list1:
        for j in list2:
            if i==j:
                r=True
                return r
two_list([1,2,3,4],[4,5,6,7])


# ### Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number from the user

# In[8]:


def fact():
    x=int(input('please enter the number'))
    F=1
    for i in range(1,x+1,1):
        F=F*i
    print(F)
fact()


# ### Write a Python function to check whether a number is in a given range.
# 
# ### The range is from 3 to 11
# 

# In[10]:


minim=int(input('enter the min range'))
maxim=int(input('enter the max range'))
num=int(input())
def rangee(x,y,z):
    if num>=x and num<=y:
        print('in range')
    else:
        print('not in range')
rangee(minim,maxim,num)


# ### Write a  program to create the multiplication table (from 1 to 10) of a number.

# In[ ]:


def mult ():
    for i in range(0,11,1):
        print('{} *{}={}'.format(i,x,i*x))

mult()


# #### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
#     lesser_of_two_evens(2,4) --> 2
#     lesser_of_two_evens(2,5) --> 5

# In[4]:


def nums(x,y):
    if x%2==0 and y%2==0:
        if x<y:
            print('lesser_of_two_evens ({},{})-->{}'.format(x,y,x))
        else:
            print('lesser_of_two_evens ({},{})-->{}'.format(x,y,y))
    elif x%2==0 and y%2!=0:
        if x<y:
            print('lesser_of_two_evens({},{}) --> {}'.format(x,y,y))
        else:
            print('lesser_of_two_evens({},{}) --> {}'.format(x,y,x))
    elif x%2!=0 and y%2==0:
         if x<y:
            print('lesser_of_two_evens({},{}) --> {}'.format(x,y,y))
    else:
            print('lesser_of_two_evens({},{}) --> {}'.format(x,y,x))
    
nums(2,5)


# #### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#     animal_crackers('Levelheaded Llama') --> True
#     animal_crackers('Crazy Kangaroo') --> False

# In[4]:


def animal_crackers(string):
    x1=string.split(' ')[0]
    x2=string.split(' ')[1]
    if x1[0] == x2[0]:
        return True
    else:
        return False
                

animal_crackers('Levelheaded Llama')


# #### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
# 
#     makes_twenty(20,10) --> True
#     makes_twenty(12,8) --> True
#     makes_twenty(2,3) --> False

# In[8]:


def Makes_twenty(l1,l2):
    if l1+l2==20 or l1==20 or l2==20:
        return True
    else:
        return False
Makes_twenty(2,18)


# #### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# 
#     almost_there(90) --> True
#     almost_there(104) --> True
#     almost_there(150) --> False
#     almost_there(209) --> True
#     
# NOTE: `abs(num)` returns the absolute value of a number

# In[11]:


def ALMOSTTHERE(n):
    if n in range(0,200):
        return True
    else:
        return False
ALMOSTTHERE(201)


# #### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum  exceeds 21, return 'BUST'
#     blackjack(5,6,7) --> 18
#     blackjack(9,9,9) --> 'BUST'
#     blackjack(9,9,11) --> 19

# In[16]:


def BLACKJACK(a,b,c):
    for i in range(0,12):
        if (a+b+c)<=21 :
            return a+b+c
        elif (a+b+c)>21 and 11 in (a,b,c) :
            return a+b+c-10
        elif (a+b+c)>21:
            return 'Bust'
BLACKJACK(4,7,11)

