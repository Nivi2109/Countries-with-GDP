#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Assignment 01: Evaluate the GDP Dataset
# 
# *The comments/sections provided are your cues to perform the assignment. You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.*
# 
# *If at any point in time you need help on solving this assignment, view our demo video to understand the different steps of the code.*
# 
# **Happy coding!**
# 
# * * *

# #### 1: View and add the dataset

# In[4]:


#Import required library
import numpy as np


# In[5]:


#Manually add the dataset
countries= np.array(['Algeria','Angola','Argentina','Australia','Austria','Bahamas','Bangladesh','Belarus','Belgium','Bhutan','Brazil','Bulgaria','Cambodia','Cameroon','Chile','China','Colombia','Cyprus','Denmark','El Salvador','Estonia','Ethiopia','Fiji','Finland','France','Georgia','Ghana','Grenada','Guinea','Haiti','Honduras','Hungary','India','Indonesia','Ireland','Italy','Japan','Kenya', 'South Korea','Liberia','Malaysia','Mexico', 'Morocco','Nepal','New Zealand','Norway','Pakistan', 'Peru','Qatar','Russia','Singapore','South Africa','Spain','Sweden','Switzerland','Thailand', 'United Arab Emirates','United Kingdom','United States','Uruguay','Venezuela','Vietnam','Zimbabwe'])
GDP_country= np.array([2255.225482,629.9553062,11601.63022,25306.82494,27266.40335,19466.99052,588.3691778,2890.345675,24733.62696,1445.760002,4803.398244,2618.876037,590.4521124,665.7982328,7122.938458,2639.54156,3362.4656,15378.16704,30860.12808,2579.115607,6525.541272,229.6769525,2242.689259,27570.4852,23016.84778,1334.646773,402.6953275,6047.200797,394.1156638,385.5793827,1414.072488,5745.981529,837.7464011,1206.991065,27715.52837,18937.24998,39578.07441,478.2194906,16684.21278,279.2204061,5345.213415,6288.25324,1908.304416,274.8728621,14646.42094,40034.85063,672.1547506,3359.517402,36152.66676,3054.727742,33529.83052,3825.093781,15428.32098,33630.24604,39170.41371,2699.123242,21058.43643,28272.40661,37691.02733,9581.05659,5671.912202,757.4009286,347.7456605])


# #### 2: Find and print the name of the country with the highest GDP

# In[7]:


#Use the argmax() method to find the highest GDP
GDP_max= GDP_country.argmax()
GDP_max


# In[8]:


#Print the name of the country
country_with_GDP_max=countries[GDP_max]
country_with_GDP_max


# #### 3: Find and print the name of the country with the lowest GDP

# In[9]:


#Use the argmin() method to find the lowest GDP
GDP_min= GDP_country.argmin()
GDP_min


# In[11]:


#Print the name of the country
country_with_GDP_min=countries[GDP_min]
country_with_GDP_min


# #### 4: Print out text ('evaluating country') and input value ('country name') iteratively

# In[21]:


#Use a for loop to print the required output
for country in countries:
    print('evaluating country {}'.format(country))


# #### 5: Print out the entire list of the countries with their GDPs

# In[23]:


#Use a for loop to print the required list
for i in range(len(countries)):
    country=countries[i]
    country_with_gdp=GDP_country[i]
    print('country {} per capita gdp is {}'.format(country,country_with_gdp))


# #### 6: Print the following:
# 1. Highest GPD value
# 2. Lowest GDP value
# 3. Mean GDP value
# 4. Standardized GDP value
# 5. Sum of all the GDPs

# In[25]:


print(GDP_country.max())


# In[26]:


print(GDP_country.min())


# In[27]:


print(GDP_country.mean())


# In[28]:


print(GDP_country.std())


# In[29]:


print(GDP_country.sum())


# In[ ]:




