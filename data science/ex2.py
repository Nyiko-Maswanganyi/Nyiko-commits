#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

grades=np.array(data)
global student_data
student_data=np.array([study_hours,grades])


student_data.shape
student_data.size
student_data[0,0]
avg_study=student_data[0].mean()
avg_grades=student_data[1].mean()
print(avg_study)
print(avg_grades)

import pandas as pd


df_students=pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],'StudyHours':student_data[0],
                            'Grade':student_data[1]})
#getting the data for row 5
df_students.loc[5]

#instruction to compute the first 6 rows,remember the index starts from 0
df_students.loc[0:5]
#get data from the first 5 rows
df_students.iloc[0:5]
#get the first 5 rows of the first 2 columns of data together
df_students.iloc[0:5,[1,2]]

#iloc can only index by location so we use loc to index by column
df_students.loc[0,'Grade']

#checking if a specific name exists in the name column and all the other column data associated with it
df_students.loc[df_students['Name']=='Anila']
#Another alternative to the previous line of code
df_students[df_students['Name']=='Anila']
#another alternative besides loc is a DataFrame method
df_students.query('Name =="Anila"') 

#wget lets you download file from the net
get_ipython().system('wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv')
df_students = pd.read_csv('grades.csv',delimiter=',',header='infer')
# Get first 5 rows of your Pandas DataFrame
df_students.head()

df_students.isnull()
#how many rows with missing values in each column
df_students.isnull().sum()
#shows rows with empty column entries
df_students[df_students.isnull().any(axis=1)]


# Get the mean study hours using to column name as an index
mean_study = df_students['StudyHours'].mean()

# Get the mean grade using the column name as a property (just to make the point!)
mean_grade = df_students.Grade.mean()
# Print the mean study hours and mean grade
print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))
df_students[df_students.Grade>mean_grade]

passes=pd.Series(df_students["Grade"]>=50)

df_students=pd.concat([df_students,passes.rename("passed")],axis=1)
df_students


# In[ ]:




