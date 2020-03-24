#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[2]:


#Declare Variables
UniquePlayers = 0
UniqueItems = 0
PurchaseAverage = 0.00
TotalPurchases = 0
TotalRevenue = 0.00


# In[3]:


#Unique Players
UniquePlayers = purchase_data["SN"].nunique()
UniquePlayers


# In[4]:


# of unique items
UniqueItems = purchase_data["Item ID"].nunique()
UniqueItems


# In[5]:


#Total Purchases Count
TotalPurchases = len(purchase_data)
TotalPurchases


# In[6]:


#Total Sales Revenue
TotalRevenue = purchase_data["Price"].sum()
print(f"$" + str(TotalRevenue.round(2)))


# In[7]:


#Average Purchase Price
PurchaseAverage = TotalRevenue / len(purchase_data)
print(f"$" + str(PurchaseAverage.round(2)))


# In[8]:


#Calculate Unique Player counts based on Gender
GCounts_df = purchase_data.groupby("Gender")["SN"].nunique()
GCounts_df.head()


# In[9]:


#Calculate Percentage of Total based on Gender
GPercent_df = GCounts_df / UniquePlayers * 100
GPercent_df.round(2)


# In[10]:


#Calculate Unique Player Purchases based on Gender
GPurchases_df = purchase_data.groupby("Gender")["Item Name"]
GPurchaseCount = GPurchases_df.count()
GPurchaseCount


# In[11]:


#Calculate Average Price based on Gender
GAverage_df = purchase_data.groupby("Gender")["Price"].mean()
GAverageValues = GAverage_df.round(2)
GAverageValues


# In[12]:


#Calculate Total Purchase Values based on Gender
GTPurchase_df = purchase_data.groupby("Gender")["Price"].sum()
GTPurchase = GTPurchase_df.round(2)
GTPurchase


# In[13]:


#Create bins for storing the age breakdown data. Bins are as follows: Under 10, 10 to 14, 15 to 19, 20 to 24, 25 to 29, 30 to 34, 35 to 39, Over 39.

bins = [0,10,15,20,25,30,35,40,45]
age_ranges = ["Under 10", "10 to 14","15 to 19", "20 to 24", "25 to 29", "30 to 34", "35 to 39", "40 and Up"]


# In[14]:


#Place Age data into bins
pd.cut(purchase_data["Age"], bins, labels=age_ranges)


# In[15]:


#Calculate Average Purchase Prices based on Age Group
PurchasesWithAgeBins_df = purchase_data
PurchasesWithAgeBins_df["Age Range"] = pd.cut(PurchasesWithAgeBins_df["Age"], bins, labels= age_ranges)
PurchasesWithAgeBins_df.head()


# In[16]:


#Calculate Unique Player counts based on Age Range
ACounts_df = PurchasesWithAgeBins_df.groupby("Age Range")["SN"].nunique()
ACounts_df


# In[17]:


#Calculate Percentage of Total based on Age Group
APercent_df = round(PurchasesWithAgeBins_df["Age Range"].value_counts() / TotalPurchases * 100,2)
APercent_df


# In[18]:


#Calculate Total Purchase Counts based on Age Group
ATPurchases_df = PurchasesWithAgeBins_df.groupby("Age Range")["Item Name"]
ATPurchasesCounts = ATPurchases_df.count()
ATPurchasesCounts


# In[19]:


#Calculate Average Purchase Price based on Age Group
AAverage_df = PurchasesWithAgeBins_df.groupby("Age Range")["Price"].mean()
AAverageValues = AAverage_df.round(2)
AAverageValues


# In[20]:


#Calculate Total Purchase Value based on Age Group
ATPurchasePrices_df = PurchasesWithAgeBins_df.groupby("Age Range")["Price"]
ATPurchasePricesCounts = ATPurchasePrices_df.sum()
ATPurchasePricesCounts


# In[21]:


#Calculate Player Sales Data
PPurchaseCount_df = purchase_data.groupby("SN").count()["Price"].rename("Purchase Count")
PPurchasePrice_df = round(purchase_data.groupby("SN").mean()["Price"].rename("Average Purchase Price"),2)
PPurchaseValue_df = purchase_data.groupby("SN").sum()["Price"].rename("Total Purchase Value")


# In[22]:


#Create and display Total Player Sales Summary DF
TotalPSales_df = pd.DataFrame({"Purchase Count":PPurchaseCount_df,
                         "Average Purchase Price":PPurchasePrice_df,
                         "Total Purchase Value":PPurchaseValue_df
                          })
TotalPSales_df


# In[23]:


#Calculate Item Sales Data
IPurchaseCount_df = purchase_data.groupby(["Item ID", "Item Name"]).count()["Price"].rename("Purchase Count")
IAveragePrice_df = round(purchase_data.groupby(["Item ID", "Item Name"]).mean()["Price"].rename("Average Purchase Price"),2)
IValueTotal_df = purchase_data.groupby(["Item ID", "Item Name"]).sum()["Price"].rename("Total Purchase Value")


# In[24]:


#Create and display Total Items Sales Summary DF
TotalISales_df = pd.DataFrame({"Purchase Count":IPurchaseCount_df,
                         "Average Item Price":IAveragePrice_df,
                         "Total Purchase Value":IValueTotal_df
                          })
TotalISales_df


# In[25]:


#Create and display Buyer Summary DF
BuyerSummary_df = pd.DataFrame({"Number of Unique Players":[UniquePlayers],
                                "Number of Unique Items":[UniqueItems],
                                "Average Purchase Price":[PurchaseAverage.round(2)],
                                "Total Number of Purchases":[TotalPurchases],
                                "Total Revenue":[TotalRevenue.round(2)]    
                              })
BuyerSummary_df


# In[26]:


#Create and display Gender Summary DF
GSummary_df = pd.DataFrame({"Unique Players":GCounts_df,
                            "Percent of Total":GPercent_df,
                            "Total Purchases":GPurchaseCount,
                            "Avg. Price per Gender":GAverageValues,
                            "Tot. Purchases per Gender":GTPurchase
                          })
GSummary_df


# In[27]:


#Create and display Age Range Summary DF
ASummary_df = pd.DataFrame({"Unique Players":ACounts_df,
                            "Percent of Total":APercent_df,
                            "Total Purchases":ATPurchasesCounts,
                            "Avg. Price per Age Range":AAverageValues,
                            "Tot. Purchase Values per Age Range":ATPurchasePricesCounts
                          })
ASummary_df


# In[28]:


#Display Top 5 Spenders Data
Top5Spenders = TotalPSales_df.sort_values("Total Purchase Value", ascending=False)
Top5Spenders.head(5)


# In[29]:


#Display Top 5 Most Popular Items, by Purchase Count
Top5PurchasedItems_df = TotalISales_df.sort_values("Purchase Count", ascending=False)
Top5PurchasedItems_df.head(5)


# In[30]:


#Display Top 5 Most Profitable Items, by Purchase Value
Top5ProfitableItems_df = TotalISales_df.sort_values("Total Purchase Value", ascending=False)
Top5ProfitableItems_df.head(5)


# In[ ]:




