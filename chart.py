import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_csv("C:/Users/hi/Documents/student.csv")
print(df)
social=df["social"].mean()
math=df["math"].mean()
english=df["english"].mean()
print("average of social",social)
print("average of math",math)
print("average of english",english)
#bar char
plt.figure(figsize=(5,5))
plt.bar(df["student"],df["social"],color='pink')
plt.title("social marks for student")
plt.xlabel("student")
plt.ylabel("social score")
plt.show()
#scatter plot:math vs english
plt.figure(figsize=(5,5))
plt.scatter(df["math"],df["english"],color='blue')
plt.title("math vs english score")
plt.xlabel("math")
plt.ylabel("english")
plt.show()
#heatmap
padmavathi=[89,78,76]
jayalakshmi=[90,89,89]
priya=[78,78,76]
jahnavi=[79,78,56]
vaishnavi=[69,98,90]
data=np.array([padmavathi,jayalakshmi,priya,jahnavi,vaishnavi])
sns.heatmap(data)
plt.title("heatmap for score")
plt.xlabel("score")
plt.ylabel("student")
plt.show()

