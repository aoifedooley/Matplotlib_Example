import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(r"YouTube_Data/USvideos.csv")

x = data['channel_title'].head(4)
y1 = data['views'].head(4)
y2 = data['likes'].head(4)
sns.lineplot(x=x,y=y1)
sns.lineplot(x=x,y=y2)
plt.show()

data['category_name'] = np.nan

data.loc[(data["category_id"] == 1),"category_name"] = 'Film and Animation'
data.loc[(data["category_id"] == 2),"category_name"] = 'Cars and Vehicles'
data.loc[(data["category_id"] == 10),"category_name"] = 'Music'
data.loc[(data["category_id"] == 15),"category_name"] = 'Pets and Animals'
data.loc[(data["category_id"] == 17),"category_name"] = 'Sport'
data.loc[(data["category_id"] == 19),"category_name"] = 'Travel and Events'
data.loc[(data["category_id"] == 20),"category_name"] = 'Gaming'
data.loc[(data["category_id"] == 22),"category_name"] = 'People and Blogs'
data.loc[(data["category_id"] == 23),"category_name"] = 'Comedy'
data.loc[(data["category_id"] == 24),"category_name"] = 'Entertainment'
data.loc[(data["category_id"] == 25),"category_name"] = 'News and Politics'
data.loc[(data["category_id"] == 26),"category_name"] = 'How to and Style'
data.loc[(data["category_id"] == 27),"category_name"] = 'Education'
data.loc[(data["category_id"] == 28),"category_name"] = 'Science and Technology'
data.loc[(data["category_id"] == 29),"category_name"] = 'Non Profits and Activism'
data.loc[(data["category_id"] == 25),"category_name"] = 'News & Politics'

plt.figure(figsize = (15,10))

g = sns.countplot('category_name', data=data, palette="Set1",order=data['category_name'].value_counts().sort_values(ascending=False).index)
g.set_xticklabels(g.get_xticklabels(),rotation=45)
g.set_title("Counting the Video Category's ", fontsize=15)
g.set_xlabel("", fontsize=12)
g.set_ylabel("Count", fontsize=12)

plt.show()