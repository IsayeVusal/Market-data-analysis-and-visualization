import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt

data = pd.read_csv('marketing_campaigns.csv', sep=';')
data

data.info()
data.describe().T
pd.isnull(data).any()
campaign_week = data.groupby("Campaign")["Week"].count()
campaign_week

data.set_index('Week', inplace=True)
data.groupby('Campaign')['Visits'].plot(legend=True)
plt.ylabel("Visits")

data.groupby('Campaign')['Revenue'].plot(legend=True)
plt.ylabel("Revenue")

data.groupby('Campaign')['Cost'].plot(legend=True)
plt.ylabel("Cost")

data1 = data.loc[data['Campaign'] == 'data1']
data1 = data1[["Revenue", "Cost"]]
ax = data1.plot.bar(rot=0)
fig = plt.gcf()
plt.xlabel("Revenue vs Cost at data1")
plt.style.use("ggplot")
fig.set_size_inches(10, 5)

data2 = data.loc[data['Campaign'] == 'data2']
data2 = data2[["Revenue", "Cost"]]
ax = data2.plot.bar(rot=0)
fig = plt.gcf()
plt.xlabel("Revenue vs Cost at data2")
fig.set_size_inches(10, 5)

data3 = data.loc[data['Campaign'] == 'data3']
data3 = data3[["Revenue", "Cost"]]
ax = data3.plot.bar(rot=0)
fig = plt.gcf()
plt.xlabel("Revenue vs Cost at data3")
fig.set_size_inches(10, 5)

# How does each campaign evolve? Lets split each campaign individually.
data1 = data.loc[data['Campaign'] == 'data1']
data2 = data.loc[data['Campaign'] == 'data2']
data3 = data.loc[data['Campaign'] == 'data3']

# We need to know all visits coming from each campaign
data1_visits = data1['Visits'].sum()
data2_visits = data2['Visits'].sum()
data3_visits = data3['Visits'].sum()
print (('Visits of data1 =').format(), data1_visits)
print (('Visits of data2 =').format(), data2_visits)
print (('Visits of data3 =').format(), data3_visits)
all_visits = [data1_visits, data2_visits, data3_visits]

# We need to know all costs coming from each campaign.
data1 = data.loc[data['Campaign'] == 'data1']
data2 = data.loc[data['Campaign'] == 'data2']
data3 = data.loc[data['Campaign'] == 'data3']
data1_Cost = data1['Cost'].sum()
data2_Cost = data2['Cost'].sum()
data3_Cost = data3['Cost'].sum()
print (('Costs of data1 =').format(), data1_Cost)
print (('Costs of data2 =').format(), data2_Cost)
print (('Costs of data3 =').format(), data3_Cost)
all_cost = [data1_Cost, data2_Cost, data3_Cost]

#  We need to know all revenue coming from each campaign
data1_Revenue = data1['Revenue'].sum()
data2_Revenue = data2['Revenue'].sum()
data3_Revenue = data3['Revenue'].sum()
print (('Revenue of data1 =').format(), data1_Revenue)
print (('Revenue of data2 =').format(), data2_Revenue)
print (('Revenue of data3 =').format(), data3_Revenue)
all_revenue = [data1_Revenue, data2_Revenue, data3_Revenue]

print (('Profit of data1 =').format(), data1_Revenue - data1_Cost)
print (('Profit of data2 =').format(), data2_Revenue - data2_Cost)
print (('Profit of data3 =').format(), data3_Revenue - data3_Cost)

print (('Revenue per visitor for data1 =').format(), data1_Revenue / data1_visits)
print (('Revenue per visitor for data2 =').format(), data2_Revenue / data2_visits)
print (('Revenue per visitor for data3 =').format(), data3_Revenue / data3_visits)

