import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(r"YouTube_Data/GBvideos.csv")

x = data['channel_title'].head(4)
y1 = data['views'].head(4)
y2 = data['likes'].head(4)

fig, (ax1,ax2) = plt.subplots(1,2)

ax1.plot(x,y1, marker="o", linestyle="-", color="r", label="views")
ax1.set_title("Plot of Views per channel")
ax1.set_xlabel("Channel Name")
ax1.set_ylabel("Views in millions")
ax1.grid(True)

ax2.plot(x,y2,marker="*", linestyle="-.", color="b", label='likes')
ax2.set_title("Plot of likes per channel")
ax2.set_xlabel("Channel Name")
ax2.set_ylabel("Views in millions")
plt.tight_layout()
plt.grid(True)

plt.show()