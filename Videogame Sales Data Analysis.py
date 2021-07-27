#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data analysis on Video Games Sales data

# This Project is to perform the analysis on the Video Games Sales dataset.
# Here we use various libraries of Python for visualization of Data.
# The Libraries I used in Project are:
# * Matplotlib 
# * Seaborn 
# * Numpy 
# * Pandas 

# In[78]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# # Data Preparation and Cleaning

# Here various modes(csv,excel,json) of displaying dataset which is in CSV format.
# First step is to load the data using pandas read_csv function. the data is stored in mutidimensional table called as dataframe.

# In[79]:


data = 'VideoGameSales.csv' #locate the CSV dataset in variable data 

videogame_df = pd.read_csv(data) #read the data using pandas and store it in videogame_df variable
videogame_df #display the data (completely )


# **This Cell is to Explain the details of all Columns :**
# 
# * Ranking -- Game ranking based on the total sales (in millions)
# * Name -- Name of the Game
# * Platform -- Game Platforms like (PS4, PC, GB etc)
# * Year -- Year of game release
# * Genre -- Simply the game genre (sports, racing ... )
# * publisher -- name of the publisher
# * NA_Sales -- Sales in north america (in millions)
# * EU_sales -- Sales in Europe (in millions)
# * JAP_sales -- Sales in Japan (in millions)
# * IND_Sales -- Sales in India (in millions)
# * Global_Sales -- Total sales world wide (in millions)

# # Statistical distribution
# 
# * Count
# * Mean
# * Minimum
# * Standard deviation
# * Maximum
# * Quartiles(25%,50%,75%)

# In[80]:


videogame_df.describe()


# **From above Dataframe, we conclude that :**
# 
# * 500 games are ranked based on their sales
# * Games released between 1980 to 2020
# * Mean/Average sales in all regions are very low compare to the Max ...

# In[81]:


videogame_df.shape #To display the shape of the data (rows, columns)


# In[82]:


videogame_df.sort_values(by = ['Name']).head(30) #Display top 30 rows and Sort by 'Name' column


# In[83]:


videogame_df.head(10) #To display top 10 rows from the dataset


# In[84]:


videogame_df.tail(10) #Display 10 rows from bottom of dataframe


# In[85]:


videogame_df[50:60] #Display the rows in range from 51 to 60


# ## To Print all Columns names

# In[86]:



# Print all col names
list(videogame_df.columns) 


# In[87]:


x = videogame_df['Name'].unique() #using numpy.ndarray to find all Names but only UNIQUE.
y = videogame_df['Genre'].unique()
z = videogame_df['Publisher'].unique()


# In[88]:


print('Total Games by `Name` count(unique) :',len(x))
print('Total Games by `Genre` count(unique) :',len(y))
print('Total Games by `Publisher` count(unique) :',len(z))


# # <center>Exploratory Analysis and Visualization</center>

#  For visualization,I am using Matplotlib, Seaborn library to visualize the Dataset of video games sales .

# In[89]:


vg_plot = videogame_df[0:25]
vg_plot


# In[90]:


x = vg_plot['Rank']
y = vg_plot['Year']
plt.figure(figsize=(25,8), dpi= 80)
plt.plot(x,y, label = 'Year', color = 'green')
plt.xlabel('Rank')
plt.ylabel('Year')
plt.title('Global Sales by Rank For 25 Rows')
plt.legend()
plt.show()


# ## Seaborn's kdeplot
# Now we can also get a smooth estimate of the distribution using a <b>kernel density estimation</b>, which Seaborn does with <i>sns.kdeplot</i>

# In[91]:


# Drawing KDEPLOT Plot
plt.figure(figsize=(25,8), dpi= 80)
sns.kdeplot(videogame_df.Global_Sales, shade=True, label = 'Global Sales', color="r", alpha=.7)


plt.title('Overall Global Sales Distribution', fontsize=16)
plt.legend()
plt.show()


# In[92]:


total = vg_plot['Global_Sales']
NA = vg_plot['NA_Sales']
EUR = vg_plot['EUR_Sales']
JAP = vg_plot['JAP_Sales']
IND = vg_plot['IND_Sales']


# In[93]:


plt.figure(figsize=(25,8), dpi= 80)
plt.grid(True)
plt.title('Comparision With all Countries with Global Sales')

plt.plot(total, label = 'Global')
plt.plot(NA, label = 'AMERICA')
plt.plot(EUR, label = 'EUROPE')
plt.plot(JAP, label = 'JAPAN')
plt.plot(IND, label = 'INDIA')
plt.legend(bbox_to_anchor =(1.0, 1.025), ncol = 2);


# In[94]:


plt.figure(figsize=(25,8))
kwargs = dict(histtype='barstacked', alpha=0.3, bins=40)
plt.hist(total, **kwargs)
plt.hist(NA, **kwargs)
plt.hist(EUR, **kwargs)
plt.hist(JAP, **kwargs)
plt.hist(IND, **kwargs)
plt.xlabel('Global Sales')
plt.ylabel('Countries')
plt.title('Stepfield type of Comparision of Global with all Countries');


# In[95]:


plt.figure(figsize=(10,7))
x = vg_plot['Year']
y = vg_plot['Global_Sales']
plt.title('Global sales occur (in Millions)')
plt.hist2d(x, y, bins=22, cmap='hot_r')
cb = plt.colorbar()
cb.set_label('counts in bin');


# # Exploring Seaborn Plots
# The main idea of Seaborn is that it provides high-level commands to create a variety of plot types useful for statistical data exploration, and even some statistical model fitting.
# Let's take a look with our dataset 'videogame_df' and plot the types available in Seaborn.

# # Maximum games sold using Countplot method

# In[96]:


plt.figure(figsize=(25,10))
sns.countplot('Year',data=videogame_df)
plt.title('Maximum Games sold on basis of Year')
plt.show();


# In[97]:


## Top 10 Platforms, Genres, Publishers with Histogram plotting


# In[98]:


#top platforms (name of the platform,total number of games developed for that platform)
topPlatforms_index = videogame_df.Platform.value_counts().head(10).index
topPlatforms_values = videogame_df.Platform.value_counts().head(10).values

#top genres (name of the genre,total number of games developed in that genre)
topGenres_index = videogame_df.Genre.value_counts().head(10).index
topGenres_values = videogame_df.Genre.value_counts().head(10).values

#top game developers/publishers (name of the publisher,total number of games published by that publisher)
topPublisher_index = videogame_df.Publisher.value_counts().head(10).index
topPublisher_values = videogame_df.Publisher.value_counts().head(10).values

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(25,8), facecolor='white')

##top platforms used for games
ax1.vlines(x=topPlatforms_index, ymin=0, ymax=topPlatforms_values, color='#AD0605', linewidth=30)
ax1.set_title('Top 10 Platforms',fontsize=16)

#top genres of Games accordingly
ax2.vlines(x=topGenres_index, ymin=0, ymax=topGenres_values, color='#AB0DD5', linewidth=30)
ax2.set_title('Top 10 Genres',fontsize=16)
plt.show()

fig, ax = plt.subplots(figsize=(25,8), facecolor='white')

#top publishers of the games
ax.vlines(x=topPublisher_index, ymin=0, ymax=topPublisher_values, linewidth=65, color='#969F79')
ax.set_title('Top 10 Publishers',fontsize=16)


# **Conclution for above Bar Graph are :**
# 
# * DS and PS2 are the most popular platforms in comparison to others platform.
# * Action is the most popular genre and the second most is the sports
# * Electronic Arts has published 1300+ products

# ## Corellating the Games Sales among Countries and Global with Seaborn
# 
# Visualizing the multidimensional relationships among the samples is as easy as calling sns.pairplot:

# # How many games have been sold between 2001 and 2010 in Millions of all Countries and Globally ?

# In[99]:


print('''Calculate total amount in millions, ranges from 2001 to 2010 and round it to Integer using round() function.''')
year_count = [i for i in range(2001, 2011)]
count_in_range = videogame_df.loc[videogame_df['Year'].isin(year_count)]

ns = sum(count_in_range.NA_Sales) #Total sales in North America
print('\nTotal Expenditure in North America from 2001 to 2010 is',round(ns),'Millions')

es = sum(count_in_range.EUR_Sales) #Total sales in Europe
print('Total Expenditure in Europe from 2001 to 2010 is',round(es),'Millions')

js = sum(count_in_range.JAP_Sales) #Total sales in Japan
print('Total Expenditure in Japan from 2001 to 2010 is',round(js),'Millions')

ins = sum(count_in_range.IND_Sales) #Sales in India
print('Total Expenditure in India from 2001 to 2010 is',round(ins),'Millions')

gs = sum(count_in_range.Global_Sales) #Global Sales
print('\nTotal Expenditure from Globally from 2001 to 2010 is',round(gs),'Millions')


# In[100]:


# Corellating among all Continents/Countries using Seaborn to perform pairplot and to plot the graph with matplotlib:

sns.pairplot(videogame_df.loc[0:,['NA_Sales','EUR_Sales','JAP_Sales','IND_Sales','Global_Sales']])
plt.show()


# **Conclution Upon performing the correlation among various countries :**
# * North America is the major market as the Global sales are highly correlated with it.
# * Europe is also an important region.
# * One intresting thing is Japanies sales are not correlated with any region's sales,We can assume that JAPANIES people have different taste, when it's about games.

# # TOP 15 GAMES IN INDIA USING BAR CHART (HORIZONTALLY)

# In[101]:


top15 = videogame_df[0:15]
top15


# In[102]:


plt.figure(figsize = (18,8))
plt.barh(top15["Name"],top15["IND_Sales"], label = 'Top Games')
plt.title("Top 15 games sold in India",fontdict = {"fontsize":20})

plt.legend()
plt.show()


# # How to Plot using pointplot between the range of Year 2003 and 2010 ?

# In[103]:


#2003-2010
first_filter=videogame_df.Year>2002
second_filter=videogame_df.Year<2011
newdata=videogame_df[first_filter&second_filter]

#visualization
sns.catplot(x="Year",y="NA_Sales",kind="point",
            data=newdata,
            hue = "Platform",
            palette='Set1',
            ci = None,
            edgecolor=None,
            height=8.27, 
            aspect=11.7/8.27)
plt.show()


# # TOP 10 PUBLISHERS OF GAMES USING PIE CHART

# In[104]:


Publisher = list(videogame_df.Publisher.unique())
global_sale_of_every_Publisher = pd.Series(dtype = float)
for pub in Publisher :
    data = videogame_df.loc[videogame_df.Publisher == pub]
    global_sale = sum(data.Global_Sales)
    global_sale_of_every_Publisher[pub] = global_sale


# In[105]:


top_10 = global_sale_of_every_Publisher[:10]


# In[106]:


plt.figure(figsize = (10.5,9))
plt.pie(top_10,labels = top_10.index,autopct = "%.2f%%",textprops = {"fontsize":13},labeldistance = 1.05)
plt.legend(loc = 4,fontsize  = 12, bbox_to_anchor =(1.75, 0.82), ncol = 2)
plt.title("Top 10 Publisher of Games",fontdict = {"fontsize":25,"fontweight":100})
plt.show()


# ## Percentage of Each Genre of Games 

# In[107]:


Genre = videogame_df.Genre
Genre = Genre.value_counts()


# In[108]:


plt.figure(figsize = (8,8))
labels = Genre.index
colors = ["#eeff00","#51ff00","#00ffdd","#ff9d00","#0033ff","#ff0800","#f700ff","#850012","#c7714a","#04615b","#ab8d5e","#00004a"]
plt.pie(Genre,labels = labels,colors = colors,autopct = "%.2f%%") 
plt.title("Percentage of Top Genres of Games",fontdict = {"fontsize":17})
plt.show()


# # Create the Dataframe for Platforms and Publishers have been in top in maximum counts , sort it accordingly ?

# In[109]:


top_platform = videogame_df.Platform.value_counts().head(15)
top_publisher = videogame_df.Publisher.value_counts().head(15)
#Top Platforms are Under 15
top_platform.to_frame()


# In[110]:


#Top Publishers are Under 15
top_publisher.to_frame()


# ## Best Selling Games in  Countries

# In[111]:


#Pie Plot

# For North America
df1 = pd.DataFrame(videogame_df.groupby('Name')['NA_Sales'].sum())
df1.sort_values(by=['NA_Sales'], inplace=True)
df1 = df1.tail(5)
df1.plot.pie(y='NA_Sales', autopct='%1.1f%%', figsize=(6, 6))
plt.title("Best selling games in North America")

# For Europe Sales
df1 = pd.DataFrame(videogame_df.groupby('Name')['EUR_Sales'].sum())
df1.sort_values(by=['EUR_Sales'], inplace=True)
df1 = df1.tail(5)
df1.plot.pie(y='EUR_Sales', autopct='%1.1f%%', figsize=(6, 6))
plt.title("Best selling games in Europe")

# For India Sales
df1 = pd.DataFrame(videogame_df.groupby('Name')['IND_Sales'].sum())
df1.sort_values(by=['IND_Sales'], inplace=True)
df1 = df1.tail(5)
df1.plot.pie(y='IND_Sales', autopct='%1.1f%%', figsize=(6, 6))
plt.title("Best selling games in INDIA")

# For Japan Sales
df1 = pd.DataFrame(videogame_df.groupby('Name')['JAP_Sales'].sum())
df1.sort_values(by=['JAP_Sales'], inplace=True)
df1 = df1.tail(5)
df1.plot.pie(y='JAP_Sales', autopct='%1.1f%%', figsize=(6, 6))
plt.title("Best selling games in Japan");


# # How to create a new dataframe with column name 'Name Of Game Which are Unique' and display all Unique Games and in which index starts from 1  ?

# In[112]:


uni_array = videogame_df.Name.unique()
ind = [i for i in range(1,len(uni_array)+1)]

ddff = pd.DataFrame(data = uni_array,  
                  index = ind,  
                  columns = ['Name Of Game Which are Unique'])
ddff


# # How to aggregate the mean, minimum, maximum of games based on Publisher For Global Sales Column ?

# In[113]:


aggr_result = videogame_df.groupby('Publisher').agg({'Global_Sales': ['mean', 'min', 'max']})
aggr_result


# ## Displaying the trend of Analysis using Seaborn's Scatterplot and Distplot method

# In[114]:


#Scatterplot Method
plt.figure(figsize=(20,8))
sns.scatterplot(videogame_df.IND_Sales[200:450], 
                videogame_df.Global_Sales[200:450], 
                hue=videogame_df.Rank,  # Dot color
                s=75)
plt.title("Scatterplot view of Global vs. India Sales", fontdict={'fontsize':26});


# ### Histograms and KDE can be combined using distplot

# In[115]:


#Displot Method

df_name = ['Global','North America', 'Europe', 'India', 'Japan']
j = 0
df_lst = [videogame_df.Global_Sales,
          videogame_df.NA_Sales,
          videogame_df.EUR_Sales,
          videogame_df.IND_Sales,
          videogame_df.JAP_Sales]

for i in df_lst:
    plt.figure(figsize=(20,8), dpi= 80)
    sns.distplot(i)
    plt.title('Displot Method for '+str(df_name[j])+' Sales', fontdict={'fontsize':26})
    j += 1


# ## Heatmap view of Games

# In[116]:


plt.figure(figsize=(20,30), dpi= 50)
avg_stats = videogame_df.groupby('Publisher').mean()
gamesample = videogame_df.filter(like = 'Sales')[0:50]  
plt.title("Stats")
sns.heatmap(gamesample, annot=True, cmap='Set1')
plt.ylim(0,51)
plt.ylabel('Total count of Publishing in Mean');


# # Games sold based on all Columns

# In[117]:


plt.figure(figsize=(20,12), dpi= 50)
sns.heatmap(videogame_df.corr('pearson'),annot=True, cmap = 'jet');


# ## Swarmplot with Sample color palette

# In[118]:


mycolors = ['#78C850',  # Grass
            '#F08030',  # Fire
            '#6890F0',  # Water
            '#A8B820',  # Bug
            '#A8A878',  # Normal
            '#A040A0',  # Poison
            '#F8D030',  # Electric
            '#E0C068',  # Ground
            '#EE99AC',  # Fairy
            '#C03028',  # Fighting
            '#F85888',  # Psychic
            '#B8A038',  # Rock
            '#705898',  # Ghost
            '#98D8D8',  # Ice
            '#7038F8',  # Dragon
           ]


# In[119]:


plt.figure(figsize=(15,15), dpi= 70)
sns.swarmplot(x='Year',
              y='Publisher',
              data=videogame_df,
              palette=mycolors)
plt.title('Swarmplotting implementation for Year vs. Publisher', fontdict = {"fontsize":17});


# ## Trend of Publisher with maximum Games sold using Seaborn's Swarmplot

# In[120]:


plt.figure(figsize=(17,9), dpi= 70)
sns.swarmplot(x='Global_Sales',
              y='Name',
              data=videogame_df[1:50], 
              hue='Publisher')
plt.title('Trend of Publisher that how much games have been sold');


# # <center>Conclusion </center>

# The dataset contains immense possibilities to improve Analytical study and research values and have a positive impact. It is not limited to the problem taken into consideration for this project. Many other interesting possibilities can be explored using this dataset.
# 
# The ways in which questions can be asked varies, so does the way of tackling a problem. Only the one that has been minutely observed and tested will provide results worth trusting.
# 
# The plots which have been built in this project can be used in Various Analysis fields like educational, business related, Technical and Many other fields.

# In[ ]:





# In[ ]:




