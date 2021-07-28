#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[8]:


import numpy as np
data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

grades=np.array(data)

student_data=np.array([study_hours,grades])

student_data
student_data.shape
student_data.size
student_data[0,0]
avg_study=student_data[0].mean()
avg_grades=student_data[1].mean()
print(avg_study)
print(avg_grades)


# In[ ]:




