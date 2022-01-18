# In[5]:


from array import array
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv ("E:\\sem 4\\PS\\piechart\\piechart\\data.csv")

product_data = df["Names"]   
bug_data = df["Values"]                      
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]    

plt.pie(bug_data , labels=product_data , colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.show()


# In[9]:


# Import the required library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# load the data sheet
df = pd.read_csv("E:\\sem 4\\PS\\piechart\\piechart\\data.csv")
# display 5 rows of dataset
df.head()
# Box Plot visualization MSSubClass with Pandas 
plt.boxplot(df['Values'])
plt.show()


# In[ 2]:
from statistics import mean, median, mode
from turtle import color, width
import matplotlib.pyplot as plt
import numpy as np
from array import *
u_value =array('i',[])
print("You selected pie Graph") 
while True:
        temp = input("Enter no: ")
        if temp=='x':
            break
        u_value.append(int(temp))
    
plt.pie(u_value)
plt.show()

# In[ 3]:
from statistics import mean, median, mode
from turtle import color, width
import matplotlib.pyplot as plt
import numpy as np
from array import *
u_value =array('i',[])
print("You selected bolxplot Graph") 
while True:
        temp = input("Enter no: ")
        if temp=='x':
            break
        u_value.append(int(temp))
    
plt.boxplot(u_value)
plt.show()


from statistics import mean, median, mode
from turtle import color, width
import matplotlib.pyplot as plt
import numpy as np
from array import *
u_value = array('i',[])
print("You selected Histogram Graph") 
while True:
        temp = input("Enter no: ")
        if temp=='x':
            break
        u_value.append(int(temp))
col = int(input("No of Bins : "))
plt.hist(u_value, bins=col)
plt.show()