#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# For this assignment you are welcomed to use other regex resources such a regex "cheat sheets" you find on the web. Feel free to share good resources with your peers in slack!
# 
# 

# Before start working on the problems, here is a small example to help you understand how to write your own answers. In short, the solution should be written within the function body given, and the final result should be returned. Then the autograder will try to call the function and validate your returned result accordingly. 

# In[24]:


def example_word_count():
    # This example question requires counting words in the example_string below.
    example_string = "Amy is 5 years old"
    
    # YOUR CODE HERE.
    # You should write your solution here, and return your result, you can comment out or delete the
    # NotImplementedError below.
    result = example_string.split(" ")
    return len(result)

    #raise NotImplementedError()


# ## Part A
# 
# Find a list of all of the names in the following string using regex.

# In[1]:


import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    result=re.findall(r'\b[A-Z]\w+',simple_string)
    return result
    # YOUR CODE HERE
    raise NotImplementedError()


# In[2]:


assert len(names()) == 4, "There are four names in the simple_string"


# ## Part B
# 
# The dataset file in [assets/grades.txt](assets/grades.txt) contains a line separated list of people with their grade in 
# a class. Create a regex to generate a list of just those students who received a B in the course.

# In[3]:


import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()
        lst=[]
        for student in re.findall('\S*\s\S*:\sB',grades):
            re.split(':',student)
            lst.append(re.split(':',student)[0])
        return lst
    raise NotImplementedError()


# In[4]:


assert len(grades()) == 16


# ## Part C
# 
# Consider the standard web log file in [assets/logdata.txt](assets/logdata.txt). This file records the access a user makes when visiting a web page (like this one!). Each line of the log has the following items:
# * a host (e.g., '146.204.224.152') 
# * a user_name (e.g., 'feest6811' **note: sometimes the user name is missing! In this case, use '-' as the value for the username.**)
# * the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
# * the post request type (e.g., 'POST /incentivize HTTP/1.1' **note: not everything is a POST!**)
# 
# Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
# ```
# example_dict = {"host":"146.204.224.152", 
#                 "user_name":"feest6811", 
#                 "time":"21/Jun/2019:15:45:24 -0700",
#                 "request":"POST /incentivize HTTP/1.1"}
# ```

# In[8]:


import re
def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
        ls=[]
        pattern="""
(?P<host>[\d{1,3}.]+)
(\s-\s)
(?P<user_name>-*\w*\d*)
(\s\[)
(?P<time>.*)
(\]\s")
(?P<request>[A-Z]*\ /\S*\s[A-Z]*/[0-9]\.[0-9]*)"""
        for item in re.finditer(pattern,logdata,re.VERBOSE):
            item.groupdict()
            ls.append(item.groupdict())
        return ls
    raise NotImplementedError()


# In[10]:


assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"

