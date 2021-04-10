import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"YouTube_Data/GBvideos.csv")

# print(data.columns)

x = data['channel_title'].head(4)
y1 = data['views'].head(4)
y2 = data['likes'].head(4)

plt.plot(x,y1, marker="o", linestyle="-", color="r", label="views")
plt.plot(x,y2, marker="v", linestyle="-", color="b", label="likes")
plt.title("Plot of Views and Likes per Channel")
plt.xlabel("Channel Name")
plt.ylabel("Views")
plt.legend()
plt.show()
