# # Data Pre Processing and Wrangling

# In[1]:


import numpy as np
import pandas as pd


# ## Dealing with Missing Values (NAs)

# In[2]:


# create sample data
df = pd.DataFrame([[1, np.nan, 2], [2,3,5], [np.nan,4,6]]) # data has no values (NAs) in some cells
# we need to remove NA or NaN from data frame


# In[3]:


print(df)


# In[4]:


## check if the data frames contains NA
print(df.isnull())


# In[5]:


## drop NA values
## all rows with cells containing NA will be dropped
print(df.dropna())


# In[6]:


## Drop columns where cells have NAs
print(df.dropna(axis=1))


# In[7]:


print(df.dropna(axis=1,how='all'))


# In[8]:


## thresh parameter lets you specify a minimum number of non-null values for the row/column to be kept
print(df.dropna(thresh=2))


# ## Filling no values (NA) cells

# In[9]:


# fill NA entries with zero
print(df.fillna(0))


# In[10]:


# specify a forward fill to propogate the previous value forward
print(df.fillna(method='ffill'))


# In[11]:


# fill foward column wise
print(df.fillna(method='ffill', axis = 1))


# In[12]:


# back-fill to propagate the next values backward
df.fillna(method='bfill')


# ## Data Handling: Basics of Conditional Data Selection 

# In[13]:


# load the data into a DataFrame
# data of endangered languages

data = pd.read_csv(r'C:\Users\willh\Udemy\Complete Data Science Training with Python for Data Analysis\scriptsLecture\section5\endangeredLang.csv')

data.head(n=6)


# In[14]:


# isolate a column
data['Countries']


# In[16]:


# isolate 2 columns
df = data[['Countries','Name in English']]


# In[17]:


df.head()


# In[18]:


# isolate rows
data[3:10]


# In[19]:


# conditional selection
data[data['Number of speakers'] < 5000]


# ## Drop Column/Row

# In[20]:


# data of endangered languages
data = pd.read_csv(r'C:\Users\willh\Udemy\Complete Data Science Training with Python for Data Analysis\scriptsLecture\section5\endangeredLang.csv')
data.head(5)


# In[21]:


df = pd.DataFrame(data)


# In[22]:


df.drop(df.index[0], inplace = True)
df


# In[23]:


df.drop(df.index[:2], inplace = True) # remove the first 2 rows
df


# In[24]:


df.drop(['Latitude'], axis = 1, inplace = True) # drop column


# ## Subsetting and Indexing

# In[25]:


data[2:] # selecting all entries from index 2 onwards


# In[26]:


data[::2] # select entries at even index locations


# In[27]:


data.iloc[0:8, 0:7] # specify the ranges of rows and columns

# positional indexing
## iloc[row slicing, column slicing[]]


# In[28]:


# select all columns for rows of index values 0 and 10
data.loc[[0, 10], :]


# In[29]:


data.iloc[[0,10], :]


# In[30]:


# isolate rows and columns
data[['Countries', 'Name in English']][4:8]


# In[31]:


# subset data on the basis of row labels
data.head(4)


# In[32]:


data[data.Countries=='Italy']


# In[33]:


x = data.loc[data['Countries'].isin(['Italy', 'Germany'])] # isolate by two row labels


# In[34]:


y = data[data['Countries'].isin(['Italy', 'Germany'])]
y


# In[35]:


x.head(15)


# In[36]:


data[(data.Countries == 'India') & (data.Degree of endangerment == 'Vulnerable')]


# In[37]:


df = data[:] # make a copy of the data frame stored in data


# In[38]:


df.rename(columns={'Number of speakers':'Number'}, inplace = True) #replace "Number of Speakers" with "Number"


# In[39]:


df.head(5)


# In[40]:


data[(data.Countries == 'India') & (df.Number<100)]


# ## Basic Grouping

# In[41]:


# Load the data into a DataFrame
data = pd.read_csv(r'C:\Users\willh\Udemy\Complete Data Science Training with Python for Data Analysis\scriptsLecture\section5\endangeredLang.csv')

data.head(n=6)


# In[42]:


large = data.sort_values(by='Number of speakers', ascending = False)
data.head()


# In[43]:


small = data.sort_values(by = 'Number of speakers', ascending = True)
data.head()


# In[44]:


byStatus = data.groupby('Degree of endangerment')
byStatus.head(n=10)


# In[45]:


data.groupby(['Degree of endangerment']).count()


# In[46]:


bygroup_CnS = data.groupby(['Countries', 'Degree of endangerment']).count()
bygroup_CnS.head()


# In[47]:


data['vfew'] = data['Number of speakers'].apply(lambda x: x<= 5000)


# In[48]:


data.head(6)


# In[49]:


group_by_5kC = data.groupby(['vfew', 'Countries'])


# In[50]:


group_by_5kC.size()


# In[51]:


data['Degree of endangerment'].value_counts()


# ## Cross-tab

# In[53]:


data = pd.read_csv(r'C:\Users\willh\Udemy\Complete Data Science Training with Python for Data Analysis\scriptsLecture\section5\endangeredLang2.csv')

data.head(n=6)


# In[54]:


#data.rename(columns={'Country codes alpha 3': 'CountryCode'}, inplace = True)
#data.columns


# In[55]:


x = pd.crosstab(data['CountryCode'],data['Endangerment'], margins = True) #tabulate our data on basis of two columns


# In[56]:


x.head(4)


# In[58]:


def perConvert(var):
    return var/float(var[-1])


# In[59]:


x = pd.crosstab(data['CountryCode'], data['Endangerment'], margins = True).apply(perConvert, axis = 1)


# In[61]:


x.head(3)


# ### Reshape

# In[8]:


data = pd.read_csv(r'C:\Users\willh\Udemy\Complete Data Science Training with Python for Data Analysis\scriptsLecture\section5\endangeredLang2.csv')

data.head(n=6)


# In[9]:


dstack = data.stack() #pivot the columns as rows for each ID
# Columns become row labels
dstack


# In[10]:


x = dstack.unstack() # unstack the previous
x.head(4)


# ### Melting

# In[11]:


patient = pd.DataFrame({'FirstName': ['Bill', 'Jane'],
                       'LastName': ['Shakespeare', 'Austen'],
                       'BloodType': ['o+', 'B+'],
                       'Wt': [85, 62]})
patient


# In[12]:


# Use melt()
# you have a data that has one or more columns that are identifier variables,
# while all other columns are considered measured variables
print(pd.melt(patient, id_vars = ['FirstName', 'LastName'], var_name = 'measurements'))


# In[13]:


x = data[0:15]
x.head(3)


# In[14]:


x = x.drop('ID', axis = 1) # drop ID column


# In[15]:


x.head(4)


# In[16]:


x.drop(['EnglishNames', 'CountryCode', 'Latitude', 'Longitude'], axis = 1, inplace = True)


# In[17]:


x.head(4)


# In[18]:


melted = pd.melt(x, id_vars = ['Countries', 'Endangerment'], value_name = 'No')
melted


# In[20]:


melted = pd.melt(x, id_vars = ['Countries'], var_name = 'Endangerment', value_name = 'No')
melted


# ## Pivoting

# ### Create a new derived table out of an existing one
# 

# ### specify an index or indices to pivot on

# ### Reshape data based on column values.

# ### Uses unique values from index/ columns

# In[22]:


data = pd.read_csv(r'C:\Users\willh\Udemy\Complete Data Science Training with Python for Data Analysis\scriptsLecture\section5\GlobalFirePower.csv')
data.head(5)


# In[24]:


p = pd.pivot_table(data, index = ["ISO3"]) # specify a unique index
#ISO3 is a column with all unique values


# In[26]:


p.head(5)


# In[28]:


p = pd.pivot_table(data, index = ["Country", "ISO3"]) # specify two column indices with unique values to pivot on


# In[30]:


p.head(4)


# In[32]:


p = pd.pivot_table(data, index = ["Country", "ISO3"], values = ["Attack Aircraft"]) # include the corresponding values


# In[34]:


p.head(4)


# In[36]:


p = pd.pivot_table(data, index= ["Country", "ISO3","Rank"], values = ["Attack Aircraft","Active Personnel"]) # 3 indices to pivot on


# In[38]:


p.tail(8)


# In[40]:


df = pd.read_csv(r'C:\Users\willh\Udemy\Complete Data Science Training with Python for Data Analysis\scriptsLecture\section5\endangeredLang2.csv')


# In[42]:


df.head(6)


# In[46]:


x = pd.pivot_table(df, index = ['CountryCode', 'Endangerment'], values = ['No'], aggfunc = np.sum) # sum endangered languages according to country


# In[48]:


x


# # Rank & Sorting

# In[56]:


import pandas as pd
import numpy as np
import os
os.chdir(r'C:\Users\willh\Udemy\Complete Data Science Training with Python for Data Analysis\scriptsLecture\section5')


# In[51]:


s = pd.Series(range(4), index = ['d', 'a', 'b', 'c'])


# In[52]:


s


# In[54]:


s.sort_index() #sort index from a to d


# In[58]:


data = pd.read_csv('GlobalFirePower.csv')


# In[60]:


data.head(5)


# In[61]:


x = data.sort_index(axis=1) # index according to columns. Columns will be arranged alphabetically
#default ascending


# In[62]:


x.head(4)


# In[65]:


x = data.sort_index(axis=1, ascending = False)
x.head()


# In[67]:


x = data.sort_values(by = "ISO3")
x.head()


# In[70]:


x = data.sort_values(by=["ISO3", "Country"])
x.head()


# ### Rank

# In[73]:


x = data.rank(axis = 1) # Rank data column wise
x.head()


# In[75]:


x = data.iloc[0:8, 0:8]
x


# In[76]:


x['mRank'] = x['Fit-for-Service'].rank(ascending = 1)
x.head(6)

