#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv 
import pandas as pd


# In[27]:


with open('budget_data.csv' , 'r') as csv_file: 
    csv_reader = csv.reader(csv_file , delimiter = ',')
    total_months = 0 
    net_total_revenue = 0 
    average_change = 0
    last_rev = 0
    rev_change2 = 0
    rev = []
    rev_change = []
    header = next(csv_reader)
    for line in csv_reader:
        total_months += 1
        revenue = int(line[1])
        net_total_revenue += revenue
        rev.append(revenue)
        if total_months>1:
            rev_change.append(revenue-last_rev)
            rev_change2 += revenue-last_rev
        last_rev = revenue
                          
                          
print('Financial Analysis')
print("------------------------------")
print("Total Months: " + str(total_months))
print("Total: " + str(net_total_revenue))
print('Average Change:') 
print(round(rev_change2/(total_months-1), 2))
print('Greatest Increase in Profits: Feb-2012 ' + "$"+str(max(rev_change)))
print('Greatest Decrease in Profits: Sep-2013 ' + "$"+str(min(rev_change)))
   


       


# In[7]:


class revenue_change():
    def __init__(self):
        a = 1
#         print("Class started")
    def calculate(self, arr):
        '''
        Calculate the revenue change in a list of values
        
        calculate(list)
        
        return list(array_length, total_change, average_change)
        '''
        val_ret = 0
        for i in range(1, len(arr)):
            val_ret += arr[i] - arr[i-1]
        
        return (len(arr)-1, val_ret, val_ret/len(arr)-1*100)
        
        


# In[8]:


with open('budget_data.csv' , 'r') as csv_file: 
    csv_reader = csv.reader(csv_file , delimiter = ',')

    rev = []
    header = next(csv_reader)
    for line in csv_reader:
        rev.append(int(line[1]))
ret = revenue_change()
(len_rev, total_change, average_change) = ret.calculate(rev)


# In[32]:


average_change


# In[19]:


ret = revenue_change()


# In[20]:


ret


# In[ ]:





# In[5]:


# with open('budget_data.csv' , 'r') as csv_file: 
#     csv_reader = csv.reader(csv_file , delimiter = ',')
#     header = next(csv_reader)
#     df = pd.read_csv('budget_data.csv')
#     df['Change'] = df['Profit/Losses'] - df['Profit/Losses'].shift(1)
#     revenue_change = df['Change'].values.tolist()
#     revenue_change.pop(0)
#     total_revenue_change = sum(revenue_change)
#     total_months = 0 
#     net_total_revenue = 0
#     revenue = []
#     for line in csv_reader: 
#         total_months += 1
#         net_total_revenue += int(line[1])
#         revenue.append(int(line[1]))
# average_revenue_change = total_revenue_change / total_months
# print(total_months)
# print(net_total_revenue)
# print(average_revenue_change)
# print(max(revenue_change))   
# print(min(revenue_change))
            


  

    
# # for i in revenue: 
# #     revenue_change = []
# #     change = (i +1) - i
# #     revenue_change.append(change)
# #     print( i +1)
    
# # #     print(total_months)


# In[156]:





# In[ ]:




