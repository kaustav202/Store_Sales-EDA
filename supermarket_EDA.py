



import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)



import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))



import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 




df=pd.read_csv('./supermarket_sales_Sheet1.csv')


# 1. checking first five records
# 2. checking last five records
# 3. checking shape
# 4. cheaking null values
# 5. checking all columns name


df.head()



df.tail()


df.shape


df.isnull().sum()



df.columns



df.head(2)






df['City'].value_counts().plot(kind='bar')



df['Gender'].value_counts()


df['Gender'].value_counts().plot(kind='bar')


gender_dummies=pd.get_dummies(df['Gender'])
gender_dummies.head()



df=pd.concat([df,gender_dummies],axis=1)


df.head(2)



plt.figure(figsize=(14,6))
sns.barplot(x='Product line',y='Female',data=df)



plt.figure(figsize=(14,6))
sns.barplot(x='Product line',y='Male',data=df)




# Payment method
df['Payment'].value_counts()





df['Payment'].value_counts().keys()




plt.pie(df['Payment'].value_counts(),labels=df['Payment'].value_counts().keys(),autopct='%1.0f%%',radius=1.5)
plt.legend()
plt.show()





#**Getting gross income plot for each product line.**
#**Which product lines earning the most profits**

plt.figure(figsize=(13,6))
sns.barplot(x="Product line",y="gross income",data=df)





#find rating
xdata=[0,1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize=(10,6))
sns.barplot(y=df['Product line'],x=df['Rating'])
plt.xticks(xdata)
plt.show()





#selling price
plt.figure(figsize=(10,5))
sns.barplot(y='Product line',x='Total',data=df)





# Quantity
df['Quantity'].value_counts()





data2=pd.DataFrame(df['Quantity'].value_counts())





data2




plt.figure(figsize=(10,6))
sns.barplot(x=data2.index,y=data2['Quantity'],palette='inferno')


# **10 quantites are sold most**

# # Result of Analysis

# * Total Customers = 1000
# * Total Females = 501
# * Total Males = 499
# * Min Rating = 4
# * Max Rating = 10
# * Average Rating = 6.97
# * Best Average Rating in Food & Beverages
# * Max Average Gross Income in Home & Lifestyle
# * Min Average Gross Income in Fashion Accessories
# * Maximum customers buys 10 quantities
# * Max Average total bill in Home and lifestyle
# * Min Average total bill in Fashion Accessories
# * Maximum People pays through e-wallet
# * Maximum people comes from Delhi
# * Max Average Sales of Fashion Accessories is from Females
# * Max Average Sales of Health & Beauty is from Males





