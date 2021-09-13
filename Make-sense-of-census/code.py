# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)

census = np.concatenate((data,new_record),axis = 0)
print(census.shape)


import numpy as np 
age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)
#Code starts here

#Creating new subsets based on 'Age'
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


#Finding the length of the above created subsets
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))

#Code starts here

#Subsetting the array based on the age 
senior_citizens=census[census[:,0]>60]

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens.sum(axis=0)[6]

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))

#Code starts here

#Creating an array based on 'education' column
high=census[census[:,1]>10]

#Finding the average pay
avg_pay_high=high[:,7].mean()

#Printing the average pay
print(avg_pay_high)

#Creating an array based on 'education' column
low=census[census[:,1]<=10]

#Finding the average pay
avg_pay_low=low[:,7].mean()

#Printing the average pay
print(avg_pay_low)
#Code starts here




