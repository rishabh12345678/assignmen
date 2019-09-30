

#reading the excel file

import pandas as pd
import datetime
x = pd.read_excel("C:\\Users\\Rishabh\\Desktop\\Sample - Superstore.xls")
df = pd.DataFrame(x)
df




#1.Find out Month wise profit

df.groupby(df['Order Date'].dt.strftime('%B'))['Profit'].sum()




#2. Find out Profit by delivery time wise

y = pd.Series(df['Ship Date'])
y


z = pd.Series(df['Order Date'])
z


from datetime import timedelta
g = pd.Series(y-z)
g


df['diff'] = g
df

df.groupby('diff')['Profit'].groups




#3. Find out the Customer who generates max profit by Category wise

df.groupby('Category')['Customer Name'].agg({"Profit":max})




#4.Find out the month in which more loss to business and also which category contributes max loss in that

x = df.groupby(df['Order Date'].dt.strftime('%B'))["Profit"].min()
x


x.min()


filter = df['Order Date'].dt.strftime('%B') == 'November'
l = df['Category'].where(filter)
l


s = pd.Series(l)
s

e = s.value_counts()
e
e.max()




#5.Find out the profit lost by order returns

 
sum(df['Profit'] < 0)






